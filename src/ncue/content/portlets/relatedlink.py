# -*- coding: utf-8 -*-
from __future__ import absolute_import
from Acquisition import aq_inner
from ncue.content import _
from plone import schema
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import field
from zope.component import getMultiAdapter
from zope.interface import implementer

import json
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
import six.moves.urllib.request, six.moves.urllib.error, six.moves.urllib.parse


class IRelatedlinkPortlet(IPortletDataProvider):

    portlet_title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )


@implementer(IRelatedlinkPortlet)
class Assignment(base.Assignment):
    schema = IRelatedlinkPortlet

    def __init__(self, portlet_title='delhi,in'):
        self.portlet_title = portlet_title.lower()

    @property
    def title(self):
        return _(u'Related Links')


class AddForm(base.AddForm):
    schema = IRelatedlinkPortlet
    form_fields = field.Fields(IRelatedlinkPortlet)
    label = _(u'Related Links')

    def create(self, data):
        return Assignment(
            portlet_title=data.get('portlet_title', 'portlet title'),
        )


class EditForm(base.EditForm):
    schema = IRelatedlinkPortlet
    form_fields = field.Fields(IRelatedlinkPortlet)
    label = _(u'Related Links')


class Renderer(base.Renderer):
    schema = IRelatedlinkPortlet
    _template = ViewPageTemplateFile('relatedlink.pt')

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

    @property
    def available(self):
        """Show the portlet only if there are one or more elements and
        not an anonymous user."""
#        return not self.anonymous #and self._data()
        return True # Show the portlet for everyone, even anonymous.

    """
    def weather_report(self):
        self.result = self._data()
        return self.result['description']

    def get_humidity(self):
        return self.result['humidity']

    def get_pressure(self):
        return self.result['pressure']

    @memoize
    def _data(self):
        baseurl = 'https://query.yahooapis.com/v1/public/yql?'
        yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="{0}")'.format(  # NOQA: E501
            self.data.place_str,
        )
        yql_url = baseurl + six.moves.urllib.parse.urlencode(
            {'q': yql_query},
        ) + '&format=json'
        result = six.moves.urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        result = {}
        result['description'] = data['query']['results']['channel']['description']  # NOQA: E501
        result['pressure'] = data['query']['results']['channel']['atmosphere']['pressure']  # NOQA: E501
        result['humidity'] = data['query']['results']['channel']['atmosphere']['humidity']  # NOQA: E501
        return result """
