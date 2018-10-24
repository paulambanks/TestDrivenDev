from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # I want to create a cool online to-do-app. I go to check out its homepage
        self.browser.get(self.live_server_url)

        # I should notice the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # I should be invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # A text box should allow me to type a task
        inputbox.send_keys('Buy a display cable for the PC')

        # When I hit Enter, the page should update and I should see my new item
        # '1: Buy a display cable for the PC' listed on the page of to-do list table.
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy a display cable for the PC')

        # A text box to add another item should be still visible. I should be able to add another item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Connect the PC with a new cable')

        # On Enter I should see both items on to-do page.
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy a display cable for the PC')
        self.wait_for_row_in_list_table('2: Connect the PC with a new cable')

        # The site should remember my list even if I close the browser.
        # Site should generate a unique URL for the user and explanatory text
        # Visiting the URL opens my to-do list with all added items

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # I want to start another to-do list
        self.browser.get(self.live_server_url)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy a display cable for the PC')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy a display cable for the PC')

        # Site should generate a unique URL for the user and explanatory text
        paula_list_url = self.browser.current_url
        self.assertRegex(paula_list_url, '/lists/.+')

        # -------------------------------------------------
        # Now Nigel - new user, comes along to the site.

        # New browser session should be used to make sure that *no information* of
        # Paula's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Nigel visits the home page. There is no sign of Paula's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy a display cable for the PC', page_text)
        self.assertNotIn('Connect the PC', page_text)

        # Nigel starts a new list by entering a new item. He is less interesting than Paula
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Nigel gets his own unique URL
        nigel_list_url = self.browser.current_url
        self.assertRegex(nigel_list_url, '/lists/.+')
        self.assertNotEqual(nigel_list_url, paula_list_url)

        # Again, there is no trace of Paula's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy a display cable for the PC', page_text)
        self.assertIn('Buy milk', page_text)
