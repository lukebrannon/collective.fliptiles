from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.namedfile.field import NamedImage
from zope import schema

from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.contenttree import ContentTreeFieldWidget
from plone.formwidget.contenttree import UUIDSourceBinder

from collective.fliptiles import _

class IFlipTile(form.Schema):
    """A flip tile.  Uses dublin core.
    """

    picture = NamedImage(
            title=_(u"Tile Picture"),
            description=_(u"Please upload an image for the front of your tile."),
            required=False,
        )

    form.widget(internal_link_uuid=ContentTreeFieldWidget)
    internal_link_uuid = schema.Choice(
            title=_(u"Target Page"),
            source=UUIDSourceBinder(),
            required=False,
        )

    external_url = schema.URI(
            title=_(u"External Link"),
            description=_(u"Please provide a valid external URL"),
            required=False,
        )
    