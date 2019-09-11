################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Programming Language :: Python :: 3",
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module provides a simple XML implementation. This is intentionally simple in order to give programmers more control over white spaces used for indentation.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-simplexml/tarball/0.2019.9.11",
	include_package_data = False,
	install_requires = [
		"jk_hwriter",
		"jk_rawhtml",
	],
	keywords = [
		"utilities",
		"xml",
		"html",
	],
	license = "Apache 2.0",
	name = "jk_simplexml",
	packages = [
		"jk_simplexml",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-simplexml",
	version = "0.2019.9.11",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)