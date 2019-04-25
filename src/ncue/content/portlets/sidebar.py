# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from ncue.content import _
from plone import schema
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import field
from zope.component import getMultiAdapter
from zope.interface import implements
from plone import api

import json
import urllib
import urllib2


class ISidebarPortlet(IPortletDataProvider):
    place_str = schema.TextLine(
        title=_(u'Name of your place with country code'),
        description=_(u'City name along with country code i.e Delhi,IN'),  # NOQA: E501
        required=True,
        default=u'delhi,in'
    )

class Assignment(base.Assignment):
    implements(ISidebarPortlet)
    schema = ISidebarPortlet

    def __init__(self, place_str='delhi,in'):
        self.place_str = place_str.lower()

    @property
    def title(self):
        return _(u'Weather of the place')


class AddForm(base.AddForm):
    schema = ISidebarPortlet
    form_fields = field.Fields(ISidebarPortlet)
    label = _(u'Add Place weather')
    description = _(u'This portlet displays weather of the place.')
    def create(self, data):
        return Assignment(
            place_str=data.get('place_str', 'delhi,in'),
        )


class EditForm(base.EditForm):
    schema = ISidebarPortlet
    form_fields = field.Fields(ISidebarPortlet)
    label = _(u'Edit Place weather')
    description = _(u'This portlet displays weather of the place.')


class Renderer(base.Renderer):
    schema = ISidebarPortlet
    _template = ViewPageTemplateFile('sidebar.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)
        portal_state = getMultiAdapter(
            (context, self.request),
            name=u'plone_portal_state'
        )
        self.anonymous = portal_state.anonymous()

    def render(self):
        return self._template()
    # @property
    # def available(self):
    #     """Show the portlet only if there are one or more elements and
    #     not an anonymous user."""
    #     return not self.anonymous and self._data()

    # def weather_report(self):
    #     self.result = self._data()
    #     return self.result['description']

    # def get_humidity(self):
    #     return self.result['humidity']

    # def get_pressure(self):
    #     return self.result['pressure']

