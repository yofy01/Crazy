# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
	_driver = None
	_baseurl = ''
	def __init__(self, driver:WebDriver = None):
		if driver is None:
			options = Options()
			options.debugger_address = '127.0.0.1:8888'
			self._driver = webdriver.Chrome(options=options)
			# self._driver.maximize_window()
			self._driver.implicitly_wait(5)
		else:
			self._driver = driver

		if self._baseurl != '':
			self._driver.get(self._baseurl)

	def wait_for_element(self, locator):
		# 显示等待
		WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located(locator))

	def find_element(self,locate_type, locator):
		# 查找单个元素
		self.wait_for_element((locate_type, locator))
		return self._driver.find_element(locate_type, locator)

	def find_elements(self,locate_type, locator):
		# 找多个元素
		self.wait_for_element((locate_type, locator))
		return self._driver.find_elements(locate_type, locator)


	def wait_for_click(self, locator):
		# 显示等待
		WebDriverWait(self._driver, 30).until(expected_conditions.element_to_be_clickable(locator))

	def find(self,locate_type, locator):
		# 查找单个元素
		# self.wait_for_element((locate_type, locator))
		return self._driver.find_element(locate_type, locator)

	def finds(self,locate_type, locator):
		# 找多个元素
		# self.wait_for_element((locate_type, locator))
		return self._driver.find_elements(locate_type, locator)
