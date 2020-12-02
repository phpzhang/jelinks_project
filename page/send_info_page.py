from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SendinfoPage(BaseAction):
    information = By.ID, "com.android.mms:id/embedded_text_editor"
    accept_person = By.ID, "com.android.mms:id/recipients_editor"
    send_btn = By.ID, "com.android.mms:id/send_button_sms"

    def page_input_receiver(self, phone):
        self.find_element(self.accept_person).send_keys(phone)

    def page_input_message(self, content):
        self.find_element(self.information).send_keys(content)

    def  page_click_sendbtn(self):
        self.find_element(self.send_btn).click()

