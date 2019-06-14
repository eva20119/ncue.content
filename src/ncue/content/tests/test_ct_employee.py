# -*- coding: utf-8 -*-
from ncue.content.content.employee import IEmployee  # NOQA E501
from ncue.content.testing import NCUE_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class EmployeeIntegrationTest(unittest.TestCase):

    layer = NCUE_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_employee_schema(self):
        fti = queryUtility(IDexterityFTI, name='Employee')
        schema = fti.lookupSchema()
        self.assertEqual(IEmployee, schema)

    def test_ct_employee_fti(self):
        fti = queryUtility(IDexterityFTI, name='Employee')
        self.assertTrue(fti)

    def test_ct_employee_factory(self):
        fti = queryUtility(IDexterityFTI, name='Employee')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IEmployee.providedBy(obj),
            u'IEmployee not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_employee_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Employee',
            id='employee',
        )

        self.assertTrue(
            IEmployee.providedBy(obj),
            u'IEmployee not provided by {0}!'.format(
                obj.id,
            ),
        )

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertIn('employee', self.parent.objectIds())

    def test_ct_employee_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Employee')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
