from selenium import webdriver
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
        self.fail('Finish the test!')

    # I should be invited to enter a to-do item straight away

    # A text box should allow me to type a task

    # When I hit Enter, the page should update , and I should see my new item listed on the page of to-do list.

    # A text box to add another item should be still visible.

    # I should be able to add another item

    # On Enter I should see both items on to-do page.

    # The site should remember my list even if I close the browser.
    # Site should generate a unique URL for the user and explanatory text

    # Visiting the URL opens my to-do list with all added items


if __name__ == '__main__':
    unittest.main(warnings='ignore')