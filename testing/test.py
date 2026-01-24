

import jk_logging

from jk_simplexml import *




with jk_logging.wrapMain() as log:

	xRoot = HElement("root")
	xRoot.setAttributeValue("bar", "äöüÄÖÜ ß & <>")
	xRoot.createChildComment("This is a comment")
	xRoot.setChildText("foo äöüÄÖÜ ß & <>")

	ws = XMLWriteSettings()
	ws.attributeEncoding = EnumXMLTextOutputEncoding.EncodeReservedCharsAsEntities
	ws.textEncoding = EnumXMLTextOutputEncoding.EncodeReservedCharsAsEntities

	HSerializer.printXML(xRoot, ws)


