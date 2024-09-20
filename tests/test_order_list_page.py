import pytest
from locators import Locators
from pages.orders_list_page import OrdersListPage
from constants import Constants


class TestOrdersListPage:

    # def test_orders_list_poppup_with_ingredients_details(self, driver):
    #     orders_list_page = OrdersListPage(driver)
    #     orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_LIST_TITLE)
    #     orders_list_page.click_on_element(Locators.ORDER)
    #     popup = orders_list_page.wait_for_element_invisible(Locators.ORDERS_POPUP)
    #     assert not popup.is_displayed()

    # def test_users_orders_displayed(self, driver):
    #     orders_list_page = OrdersListPage(driver)
    #     orders_list_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
    #     orders_list_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
    #     orders_list_page.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
    #     orders_list_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
    #     orders_list_page.drag_and_drop_item(Locators.BUN, Locators.BASKET_LOCATOR)
    #     orders_list_page.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
    #     orders_list_page.click_on_element(Locators.MAKE_ORDER_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_SUBTITLE)
    #     user_order_number = '#0' + orders_list_page.get_text_from_element(Locators.ORDER_NUMBER)
    #     orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
    #     orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
    #     order_number = orders_list_page.get_text_from_element(Locators.ORDER_NUMBER_IN_LIST)
    #     assert user_order_number == order_number


    # def test_count_of_all_orders(self, driver):
    #     orders_list_page = OrdersListPage(driver)
    #     orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_LIST_TITLE)
    #     before_order = int(orders_list_page.get_text_from_element(Locators.ALL_ORDERS))
    #     orders_list_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
    #     orders_list_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
    #     orders_list_page.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
    #     orders_list_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
    #     orders_list_page.drag_and_drop_item(Locators.BUN, Locators.BASKET_LOCATOR)
    #     orders_list_page.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
    #     orders_list_page.click_on_element(Locators.MAKE_ORDER_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_SUBTITLE)
    #     orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
    #     orders_list_page = OrdersListPage(driver)
    #     orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_LIST_TITLE)
    #     after_order = int(orders_list_page.get_text_from_element(Locators.ALL_ORDERS))
    #     assert before_order < after_order

    # def test_count_of_today_orders(self, driver):
    #     orders_list_page = OrdersListPage(driver)
    #     orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_LIST_TITLE)
    #     before_order = int(orders_list_page.get_text_from_element(Locators.TODAY_ORDERS))
    #     orders_list_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
    #     orders_list_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
    #     orders_list_page.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
    #     orders_list_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
    #     orders_list_page.drag_and_drop_item(Locators.BUN, Locators.BASKET_LOCATOR)
    #     orders_list_page.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
    #     orders_list_page.click_on_element(Locators.MAKE_ORDER_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_SUBTITLE)
    #     orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
    #     orders_list_page = OrdersListPage(driver)
    #     orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
    #     orders_list_page.find_element_with_wait(Locators.ORDER_LIST_TITLE)
    #     after_order = int(orders_list_page.get_text_from_element(Locators.TODAY_ORDERS))
    #     assert before_order < after_order

    def test_order_in_progress(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        orders_list_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        orders_list_page.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
        orders_list_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
        orders_list_page.drag_and_drop_item(Locators.BUN, Locators.BASKET_LOCATOR)
        orders_list_page.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
        orders_list_page.click_on_element(Locators.MAKE_ORDER_BTN)
        orders_list_page.find_element_with_wait(Locators.ORDER_SUBTITLE)
        orders_list_page.driver.implicitly_wait(5)
        user_order_number = '#0' + orders_list_page.get_text_from_element(Locators.ORDER_NUMBER)
        orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
        orders_list_page.click_on_element(Locators.ORDERS_LIST_BTN)
        orders_list_page.driver.implicitly_wait(5)
        order_number = '#' + orders_list_page.get_text_from_element(Locators.ORDER_IN_PROGRESS)
        assert user_order_number == order_number




