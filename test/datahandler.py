#!/usr/bin/env python

#
# Revelation 0.4.0 - a password manager for GNOME 2
# http://oss.codepoet.no/revelation/
# $Id$
#
# Unit tests for DataHandler module
#
#
# Copyright (c) 2003-2005 Erik Grinaker
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

import unittest

from revelation import datahandler



class detect_handler(unittest.TestCase):
	"detect_handler()"

	def test_detect(self):
		"detect_handler() returns a correct handler type"

		xml = """<?xml version="1.0" encoding="iso-8859-1" ?><revelationdata version="0.4.0" dataversion="1"></revelationdata>"""
		self.assertEquals(datahandler.detect_handler(xml), datahandler.RevelationXML)


	def test_unknown(self):
		"detect_handler() raises DetectError on unknown type"

		data = "this is just junk data"
		self.assertRaises(datahandler.DetectError, datahandler.detect_handler, data)



class get_export_handlers(unittest.TestCase):
	"get_export_handlers()"

	def test_handlers(self):
		"get_export_handlers() returns only export handlers"

		for handler in datahandler.get_export_handlers():
			self.assertEqual(handler.exporter, True)



class get_import_handlers(unittest.TestCase):
	"get_import_handlers()"

	def test_handlers(self):
		"get_import_handlers() returns only import handlers"

		for handler in datahandler.get_import_handlers():
			self.assertEqual(handler.importer, True)



if __name__ == "__main__":
	unittest.main()