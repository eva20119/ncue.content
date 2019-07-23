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
        request = self.request
        portal = api.portal.get()

        self.event = api.content.find(context=portal['department'], depth=2, sort_on='effective', sort_limit=10, portal_type='News Item', sort_order='descending')
        return self.template()

    def formatDate(self, date):
        return date.strftime('%Y-%m-%d %H:%m')
        # return self.plone_view.toLocalizedTime(time, long_format, time_only)


class ContactUs(BrowserView):
    tmplate = ViewPageTemplateFile("templates/contact_us.pt")
    def __call__(self):
        request = self.request
        portal = api.portal.get()

        name = request.get('name')
        email = request.get('email')
        subject = request.get('subject')
        message = request.get('message')

        if name and email:
            api.portal.show_message(message='您的留言已收到會盡快回覆'.decode('utf-8'), request=request)
            request.response.redirect(portal.absolute_url() + '/contact_us')
        else:
            return self.tmplate()


class CustomNewsitemView(BrowserView):
    template = ViewPageTemplateFile("templates/custom_newsitem_view.pt")
    def __call__(self):
        return self.template()


class TeacherDetail(BrowserView):
    template = ViewPageTemplateFile("templates/teacher_detail.pt")
    def __call__(self):
       return self.template()
