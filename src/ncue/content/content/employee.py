# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from ncue.content import _
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


organizers = SimpleVocabulary(
   [
     SimpleTerm(value=u'male', title=_(u'男')),
     SimpleTerm(value=u'female', title=_(u'女')),
   ]
)
class IEmployee(model.Schema):
    """ Marker interface and Dexterity Python Schema for Employee
    """
    fieldset('Basic', fields=['title', 'img', 'job', 'sex', 'arrvialDate', 'graduaction', 'occupation', 'code', 'email', 'specialty'])
    title = schema.TextLine(
        title=_(u'title'),
        required=True
    )
    img = namedfile.NamedBlobImage(
        title=_(u'teacher image'),
        required=False
    )
    job = schema.TextLine(
        title=_(u'job'),
        required=False
    )
    sex = schema.Choice(
        title=_(u'sex'),
        vocabulary=organizers,
        required=False
    )
    arrvialDate = schema.Date(
        title=_(u'arrvialDate'),
        required=False
    )
    graduaction = schema.TextLine(
        title=_(u'graduaction'),
        required=False
    )
    occupation = schema.TextLine(
        title=_(u'occupation'),
        required=False
    )
    code = schema.TextLine(
        title=_(u'code'),
        required=False
    )
    email = schema.TextLine(
        title=_(u'email'),
        required=False
    )
    specialty = schema.TextLine(
        title=_(u'specialty'),
        required=False
    )
 
    fieldset(_(u'experienceList'), fields=['experience'])
    experience = RichText(
        title=_(u'experience'),
        required=False
    )
    fieldset(_(u'writeList'), fields=['write'])
    write = RichText(
        title=_(u'write'),
        required=False
    )
    fieldset(_(u'planeList'), fields=['plane'])
    plane = RichText(
        title=_(u'plane'),
        required=False
    )
    fieldset(_(u'awardList'), fields=['award'])
    award = RichText(
        title=_(u'award'),
        required=False
    )
    fieldset(_(u'inventionList'), fields=['invention'])
    invention = RichText(
        title=_(u'invention'),
        required=False
    )
    fieldset(_(u'licenseList'), fields=['license'])
    license = RichText(
        title=_(u'license'),
        required=False
    )
    fieldset(_(u'eventList'), fields=['event'])
    event = RichText(
        title=_(u'event'),
        required=False
    )
    fieldset(_(u'trainList'), fields=['train'])
    train = RichText(
        title=_(u'train'),
        required=False
    )
    fieldset(_(u'promoList'), fields=['promo'])
    promo = RichText(
        title=_(u'promo'),
        required=False
    )
    fieldset(_(u'teachList'), fields=['teach'])
    teach = RichText(
        title=_(u'teach'),
        required=False
    )
    fieldset(_(u'serverList'), fields=['server'])
    server = RichText(
        title=_(u'server'),
        required=False
    )


@implementer(IEmployee)
class Employee(Item):
    """
    """
