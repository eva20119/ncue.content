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
    title = schema.TextLine(
        title=_(u'title'),
        required=True
    )
    list = RichText( 
        title=_(u'teacher list word'),
        required=False
    )
    detail = RichText( 
        title=_(u'teacher detail'),
        required=False
    )
    img = namedfile.NamedBlobImage(
        title=_(u'teacher image'),
        required=False
    )



@implementer(IEmployee)
class Employee(Item):
    """
    """
