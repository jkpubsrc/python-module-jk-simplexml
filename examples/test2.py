#!/usr/bin/python3


from jk_simplexml import *


xRoot = HElement("ROOT")
xRoot.setAttributeValue("foo", "bar")
xRoot.setChildText("Foo bar")
x = HElement("SomeElement")
x.setAttributeValue("x", "y")
x.setAttributeValue("y", "123")
xRoot.children.append(x)
xRoot.children.append(HText("We < are > going & walking"))


with open("test2.html", "w") as f:
	f.write(HSerializer.toHTMLDocStr(xRoot))



