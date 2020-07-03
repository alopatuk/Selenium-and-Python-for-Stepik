from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empt"

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Product is present in basket, but " \
                                                                             "should not be "
