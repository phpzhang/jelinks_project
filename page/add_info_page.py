from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddinfoPage(BaseAction):
    send_message = By.ID, "com.android.mms:id/action_compose_new"
    def page_click_addmessage(self):
        print(self.find_element(self.send_message))
        self.find_element(self.send_message).click()
