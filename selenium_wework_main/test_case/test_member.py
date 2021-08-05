# -*- coding:utf-8 -*-
import pytest
from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.main import Main


class TestMember:
	def setup(self):
		self.main = Main()
		self.add_member = AddMember()

	# @pytest.mark.skip
	def test_member(self):
		name = 'c1brd34'
		account = 'c1bg3d4'
		phone = '13125122414'

		add_member = self.main.goto_add_member()
		add_member.add_member(name, account, phone)
		assert add_member.get_members(name) # 很简单的验证，但不严谨



