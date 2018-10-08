from selenium import webdriver

browser = webdriver.Chrome(service_args=['--verbose',
                                         '--log-path=/Users/pbanks/Documents/Programming/Python/Development/TestDrivenDev/chromedriver.log'])
browser.get('http://localhost:8000')

assert 'Django' in browser.title
