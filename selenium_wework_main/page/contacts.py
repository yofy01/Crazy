# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Contacts(BasePage):

	def get_member(self):
		'''获取到整个成员列表的数据，再从中抽取属性title(姓名)的列
		1、添加成员在分页里，怎么获取？
		'''
		locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_td")
		WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))

		elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
		# 获取所有姓名
		# list = []
		# for elment in elements:
		# 	list.append(element.get_attribute("title"))
		list = [element.get_attribute('title') for element in elements]  # 列表生成式
		# print(list)
		return list

	def goto_add_member(self):
		locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member")
		WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))

		self._driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()

		return AddMember(self._driver)