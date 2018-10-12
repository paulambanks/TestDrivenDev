from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service_args=['--verbose',
                                         '--log-path=/Users/pbanks/Documents/Programming/Python/Development/TestDrivenDev/chromedriver.log'])

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # I want to create a cool online to-do-app. I go to check out its homepage
        self.browser.get('http://localhost:8000')

        # I should notice the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # I should be invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # A text box should allow me to type a task
        inputbox.send_keys('Buy a display cable for the PC')

        # When I hit Enter, the page should update and I should see my new item
        # '1: Buy a display cable for the PC' listed on the page of to-do list table.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy a display cable for the PC' for row in rows),
            git ad"New to-do item did not appear in the table"
        )

        # A text box to add another item should be still visible. I should be able to add another item
        self.fail('Finish the test!')

    # On Enter I should see both items on to-do page.

    # The site should remember my list even if I close the browser.
    # Site should generate a unique URL for the user and explanatory text

    # Visiting the URL opens my to-do list with all added items


if __name__ == '__main__':
    unittest.main(warnings='ignore')