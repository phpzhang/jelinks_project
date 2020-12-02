from page.add_info_page import AddinfoPage
from page.send_info_page import SendinfoPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def page_addinfo(self):
        return AddinfoPage(self.driver)

    def page_sendinfo(self):
        return SendinfoPage(self.driver)