#!/usr/bin/python3


from jk_simplexml import *


root = HElement("ROOT")
root.setAttributeValue("foo", "bar")
root.setChildText("Foo bar")
x = HElement("SomeElement")
x.setAttributeValue("x", "y")
x.setAttributeValue("y", "123")
root.children.append(x)
root.children.append(HText("We < are > going & walking"))


#HToolkit_Write_PlainText.writeAsPlainText(root)

xmlWriteSettings = XMLWriteSettings()
hwrite = HSerializer.printHTML
#hwrite = HSerializer.printXML
#hwrite = HSerializer.printDump



xmlWriteSettings.printStyle = EnumXMLPrintStyle.Pretty
hwrite(root, xmlWriteSettings)

print()

xmlWriteSettings.printStyle = EnumXMLPrintStyle.SingleLine
hwrite(root, xmlWriteSettings)

print()
print()

xmlWriteSettings.printStyle = EnumXMLPrintStyle.Simple
hwrite(root, xmlWriteSettings)

print()
print()

xmlWriteSettings.printStyle = EnumXMLPrintStyle.Pretty
xmlWriteSettings.textEncoding = EnumXMLTextOutputEncoding.AlwaysAsIs
hwrite(root, xmlWriteSettings)

print()

xmlWriteSettings.printStyle = EnumXMLPrintStyle.SingleLine
xmlWriteSettings.textEncoding = EnumXMLTextOutputEncoding.AlwaysAsIs
hwrite(root, xmlWriteSettings)

print()
print()

xmlWriteSettings.printStyle = EnumXMLPrintStyle.Simple
xmlWriteSettings.textEncoding = EnumXMLTextOutputEncoding.AlwaysAsIs
hwrite(root, xmlWriteSettings)

print()
print()



