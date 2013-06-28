from five import grok
from zope import schema

from plone.directives import form, dexterity
from plone.app.uuid.utils import uuidToURL

from collective.fliptiles import _

class IFlipFolder(form.Schema):
    """A Folder to hold and display flip tiles. Uses dublin core.
    """

    tileColumns = schema.Int(
            title=_(u"Tiles Per Row"),
            description=_(u"What is the maximum number of tiles to display per row"),
            required=False,
        )

class View(grok.View):
    grok.context(IFlipFolder)
    grok.require('zope2.View')

    def getTiles(self):
    	folder_contents = self.context.items()
    	tiles = []
    	for item in folder_contents:
    		tiles.append(item[1])
    	
    	return tiles

    def getTileTemplate(self):
        folder_contents = self.context.items()
        tiles = []
        column_width = self.context.tileColumns
        if not column_width:
            column_width = 4

        theHTML = []
        for item in folder_contents:
            tiles.append(item[1])

        tile_segments = [tiles[x:x+column_width] for x in range(0,len(tiles),column_width)]
        row_number = 0
        for segment in tile_segments:
            theHTML.append('<ul id=tilerow-%s>'%(row_number))
            for tile in segment:
                theHTML.append('<li>')
                theHTML.append('<img src="%s/@@download/picture" />'%(tile.absolute_url()))
                theHTML.append('<h3>%s</h3>'%(tile.title))
                if tile.internal_link_uuid:
                    theHTML.append('<p><a href="%s">%s</a></p>'%(uuidToURL(tile.internal_link_uuid), tile.description))
                elif tile.external_url:
                    theHTML.append('<p><a href="%s">%s</a></p>'%(tile.external_url, tile.description))
                else:
                    theHTML.append('<p>%s</p>'%(tile.description))
                theHTML.append('</li>')
            theHTML.append('</ul>')
            ++row_number

        return ('').join(theHTML)

