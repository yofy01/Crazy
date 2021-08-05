# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):
	# _baseurl = 'https://work.weixin.qq.com/wework_admin/frame'

	def add_member(self, name, account, phone):
		# sendkeys 添加成员
		self.find_element(By.CSS_SELECTOR, '#username').send_keys(name)
		self.find_element(By.CSS_SELECTOR, '#memberAdd_english_name').send_keys('yofy')
		self.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(account)
		self.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
		self.find_element(By.CSS_SELECTOR, '#memberAdd_title').send_keys('IT支持')
		self.find_elements(By.CSS_SELECTOR,'.js_btn_save')[1].click()
		# 必填字段都写上
		sleep(5)
		# self._driver.quit() # 调试期间，复用浏览器，需要注释掉
		return True


	def get_member(self):
		'''获取到整个成员列表的数据，再从中抽取属性title(姓名)的列
		1、添加成员在分页里，怎么获取？
		'''
		elements = self.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
		# 获取所有姓名
		# list = []
		# for elment in elements:
		# 	list.append(element.get_attribute("title"))
		list = [element.get_attribute('title') for element in elements] # 列表生成式
		# print(list)
		return list

	def update_page(self):
		# 刷新数据
		content: str = self.find_elements(By.CSS_SELECTOR, '.ww_pageNav_info_text')[0].text
		return [int(x) for x in content.split('/', 1)] # 分割单/ ，只分割一次

	def get_members(self, value):
		'''改造，如果验证的值在其他分页，计思想：
		1、获取当前页/总页数的元素
		2、获取当前页的值，遍历，加判断，传入的参数是否在当前页的数据中，在 return True
		3、不在，点击下一页，则刷新获取，获取当前页/总页数，重复步骤2
		'''
		self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
		cur_page, total_page = self.update_page()
		while True:
			elements = self.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
			for element in elements:
				if value == element.get_attribute('title'):
					return True
			# 刷新数据
			cur_page = self.update_page()[0]
			if cur_page == total_page:
				return False
			# 点击下一页
			# sleep(3)
			self.find_elements(By.CSS_SELECTOR, '.js_next_page')[0].click()

