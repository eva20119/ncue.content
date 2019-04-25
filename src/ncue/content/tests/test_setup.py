# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ncue.content.testing import NCUE_CONTENT_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that ncue.content is properly installed."""

    layer = NCUE_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ncue.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ncue.content'))

    def test_browserlayer(self):
        """Test that INcueContentLayer is registered."""
        from ncue.content.interfaces import (
            INcueContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            INcueContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NCUE_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ncue.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ncue.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ncue.content'))

    def test_browserlayer_removed(self):
        """Test that INcueContentLayer is removed."""
        from ncue.content.interfaces import \
            INcueContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            INcueContentLayer,
            utils.registered_layers())
