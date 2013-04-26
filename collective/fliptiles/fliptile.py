from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.namedfile.field import NamedImage


from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.fliptiles import _

class IFlipTile(form.Schema):
    """A flip tile.  Uses dublin core.
    """

    picture = NamedImage(
            title=_(u"Tile Picture"),
            description=_(u"Please upload an image for the front of your tile."),
            required=False,
        )    

    relatedItem = RelationChoice(
            title=_(u"Target Page"),
            source=ObjPathSourceBinder(object_provides=IPresenter.__identifier__),
            required=False,
        )