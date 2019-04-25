# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contenttypes.browser.folder import FolderView
from ncue.content import _
from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection
# from email.mime.text import MIMEText
import json
import datetime
# from db.connect.browser.views import SqlObj
#from db.connect.browser.base_inform_configlet import IInform
# from Products.CMFPlone.utils import getSiteLogo
# import time


class Debug(BrowserView):
    def __call__(self):
        import pdb; pdb.set_trace()


class CoverView(BrowserView):
    template = ViewPageTemplateFile("templates/cover_view.pt")
    def __call__(self):
        return self.template()