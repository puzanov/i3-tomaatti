# -*- coding: utf-8 -*-
# Copyright (C) 2017 - 2018 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.

from tomaatti.internal.confighelper import ConfigHelper
from unittest import TestCase


class ConfigHelperTest(TestCase):
	def testTrueResultsInYes(self):
		self.assertEqual('yes', ConfigHelper.bool_to_config_str(True))

	def testFalseResultsInNo(self):
		self.assertEqual('no', ConfigHelper.bool_to_config_str(False))
