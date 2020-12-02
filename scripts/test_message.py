import os,sys
from datetime import datetime

sys.path.append(os.getcwd())
import allure
from base.base_analyze import analyze_file
import time
import pytest
from base.base_driver import init_driver
from page.page import Page


class TestMessage:

    def setup(self):
#         self.driver = init_driver()
#         print(self.driver)
#         self.page = Page(self.driver)
        pass

    def teardown(self):
        pass
#         time.sleep(3)
#         self.driver.quit()

    # [("18888888888", "hello"), ("13333333333", "abc")]
    @pytest.mark.parametrize("args", analyze_file("message_data.yaml","test_send_message"))
    @allure.step(title="测试用例01")
    @allure.severity("critical")
    def test_send_message(self, args):
        assert 1 == 1
#         allure.attach('hello', 'hello', allure.attachment_type.TEXT)
#         phone = args["phone"]
#         content = args["content"]
#         # 主页 - 点击 新建短信
#         self.page.page_addinfo().page_click_addmessage()
#         # 新建短信 - 输入 接收人
#         self.page.page_sendinfo().page_input_receiver(phone)
#         # 新建短信 - 输入 内容
#         self.page.page_sendinfo().page_input_message(content)
#         # 新建短信 - 点击 发送
#         self.page.page_sendinfo().page_click_sendbtn()




    # @allure.step(title="测试用例02")
    # def test_send_message2(self):
    #     assert 2 == 1
