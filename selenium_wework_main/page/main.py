# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
	_baseurl = 'https://work.weixin.qq.com/wework_admin/frame'

	def goto_add_member(self):
		# 点击tab通讯录页面进入通讯录页面
		self.find_element(By.CSS_SELECTOR, '#menu_contacts>span').click()

		# 点击【添加成员】进入添加成员页面
		self.find_element(By.CSS_SELECTOR, ".js_has_member > div:nth-child(1) > a:nth-child(2)").click()

		return AddMember(self._driver)
