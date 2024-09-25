from locators import Locators
from pages.change_password_page import ChangePasswordPage
from constants import Constants


class TestChangePasswordPage:

    def test_go_to_change_password_page(self, driver):
        change_password_page = ChangePasswordPage(driver)
        change_password_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        change_password_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        change_password_page.click_on_element(Locators.CHANGE_PASSWORD_LINK)
        change_password_page.wait_for_page(Constants.CHANGE_PASSWORD_URL)
        result = change_password_page.find_element_with_wait(Locators.CHANGE_PASSWORD_TITLE)
        assert result

    def test_input_imail_on_change_password_page(self, driver):
        change_password_page = ChangePasswordPage(driver)
        change_password_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        change_password_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        change_password_page.click_on_element(Locators.CHANGE_PASSWORD_LINK)
        change_password_page.wait_for_page(Constants.CHANGE_PASSWORD_URL)
        change_password_page.find_element_with_wait(Locators.CHANGE_PASSWORD_TITLE)
        change_password_page.fill_email_form()
        result = change_password_page.find_element_with_wait(Locators.SAVE_NEW_PASSWORD_BTN)
        assert result

    def test_show_password(self, driver):
        change_password_page = ChangePasswordPage(driver)
        change_password_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        change_password_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        change_password_page.click_on_element(Locators.CHANGE_PASSWORD_LINK)
        change_password_page.wait_for_page(Constants.CHANGE_PASSWORD_URL)
        change_password_page.find_element_with_wait(Locators.CHANGE_PASSWORD_TITLE)
        change_password_page.fill_email_form()
        change_password_page.find_element_with_wait(Locators.SAVE_NEW_PASSWORD_BTN)
        assert change_password_page.is_password_invisible()
        change_password_page.fill_password_form()

        change_password_page.click_on_element(Locators.SHOW_PASSWORD_BTN)
        assert change_password_page.is_password_visible()









