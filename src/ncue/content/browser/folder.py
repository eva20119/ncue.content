# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.app.dexterity import _
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import ISecuritySchema
from Products.CMFPlone.PloneBatch import Batch
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.component import getUtility
from plone import api


class FolderListing(BrowserView):
    def __init__(self, context, request):
        super(FolderListing, self).__init__(context, request)

        self.plone_view = getMultiAdapter(
            (context, request), name=u'plone')
        self.portal_state = getMultiAdapter(
            (context, request), name=u'plone_portal_state')
        self.pas_member = getMultiAdapter(
            (context, request), name=u'pas_member')

        limit_display = getattr(self.request, 'limit_display', None)
        limit_display = int(limit_display) if limit_display is not None else 10
        b_size = getattr(self.request, 'b_size', None)
        self.b_size = int(b_size) if b_size is not None else limit_display
        b_start = getattr(self.request, 'b_start', None)
        self.b_start = int(b_start) if b_start is not None else 0
        self.sort_order = self.request.get('sort_order', '')
        self.sort_on = self.request.get('sort_on', '')

    def results(self, **kwargs):
        kwargs.update(self.request.get('contentFilter', {}))
        if 'object_provides' not in kwargs:  # object_provides is more specific
            kwargs.setdefault('portal_type', self.friendly_types)
        kwargs.setdefault('batch', True)
        kwargs.setdefault('b_size', self.b_size)
        kwargs.setdefault('b_start', self.b_start)
        kwargs.setdefault('sort_order', self.sort_order)
        kwargs.setdefault('sort_on', self.sort_on)

        listing = aq_inner(self.context).restrictedTraverse(
            '@@folderListing', None)
        if listing is None:
            return []
        results = listing(**kwargs)
        return results

    def batch(self):
        batch = Batch(
            self.results(),
            size=self.b_size,
            start=self.b_start,
            orphan=1
        )
        return batch

    @property
    def friendly_types(self):
        return self.portal_state.friendly_types()

    def pdb(self):
        import pdb;pdb.set_trace()

    def toLocalizedTime(self, time, long_format=None, time_only=None):
        return self.plone_view.toLocalizedTime(time, long_format, time_only)