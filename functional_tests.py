from selenium import webdriver
import unittest

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')       
        
# assert 'To-Do' in browser.title, "Browser title was " + browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box 

# When she hits enter, the page updates, and now the page 
# lists
# 1. Buy peacock feathers as an item in a to-do list

# There is a still a txt box inviting her to add another item.
# She enters "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. 
# Then she sees that teh sites has generated a unique URL  for her
# There is some explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()