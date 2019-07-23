# -*- coding: utf-8 -*-
from ncue.content import _


def moveObjectsToTop(obj, event):
    """
    Moves Object to the top of its folder
    """

    folder = obj.getParentNode()
    if folder is not None and hasattr(folder, 'moveObjectsToTop'):
        if obj.portal_type in ['Document', 'News Item', 'Event']:
            folder.moveObjectsToTop(obj.id)

