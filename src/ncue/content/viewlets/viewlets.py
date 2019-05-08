# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection
from plone import api


class CoverImgBanner(base.ViewletBase):
    pass


class CoverNewsBanner(base.ViewletBase):
    def update(self):
        request = self.request
        portal = api.portal.get()

        self.news = api.content.find(context=portal['department']['department_news'], depth=1, sort_on='effective_date', sort_limit=10)