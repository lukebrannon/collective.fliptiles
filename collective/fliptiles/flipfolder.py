from five import grok
from zope import schema

from plone.directives import form, dexterity

from collective.fliptiles import _

class IFlipFolder(form.Schema):
    """A Folder to hold and display flip tiles. Uses dublin core.
    """