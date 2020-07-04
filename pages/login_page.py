from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Button for login is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Email for registration is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Password for registration is not " \
                                                                                  "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_REPLAY_PASSWORD), "Replay password for " \
                                                                                         "registration is not " \
                                                                                         "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Button for registration is not " \
                                                                                "presented "

    def register_new_user(self, email, password):
        new_user_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        new_user_email.send_keys(email)
        new_user_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        new_user_password.send_keys(password)
        new_user_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPLAY_PASSWORD)
        new_user_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()

