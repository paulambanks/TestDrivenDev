from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service_args=['--verbose',
                                         '--log-path=/Users/pbanks/Documents/Programming/Python/Development/TestDrivenDev/chromedriver.log'])

    def tearDown(self):
        self.browser.quit()

    # Helper method
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # I want to create a cool online to-do-app. I go to check out its homepage
        self.browser.get(self.live_server_url)

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

        self.check_for_row_in_list_table('1: Buy a display cable for the PC')

        # A text box to add another item should be still visible. I should be able to add another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Connect the PC with a new cable')

        # On Enter I should see both items on to-do page.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy a display cable for the PC')
        self.check_for_row_in_list_table('2: Connect the PC with a new cable')

        # The site should remember my list even if I close the browser.
        self.fail('Finish the test!')
    # Site should generate a unique URL for the user and explanatory text

    # Visiting the URL opens my to-do list with all added items
