from .base_page import BasePage
from .locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        assert get_url == "login", "Url is not correct"

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
