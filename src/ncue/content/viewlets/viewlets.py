# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection
from plone import api


class CoverImgBanner(base.ViewletBase):
    def update(self):
        portal = api.portal.get()
        self.banner_left = api.content.find(context=portal['banner']['banner_left'])[0]
        self.banner_right_1 = api.content.find(context=portal['banner']['banner_right_1'])[0]
        self.banner_right_2 = api.content.find(context=portal['banner']['banner_right_2'])[0]


class CoverNewsBanner(base.ViewletBase):
    def update(self):
        request = self.request
        portal = api.portal.get()

        self.news = api.content.find(context=portal['department']['department_news'], depth=1, sort_on='effective_date', sort_limit=10)