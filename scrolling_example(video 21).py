from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class at_least_n_elements_found:
	def __init__(self, locator, n):
		self.locator = locator
		self.n = n

	def __call__(self, driver):
		elements = driver.find_elements(*self.locator)
		if len(elements) >= self.n:
			return elements
		else:
			return False

c = webdriver.Chrome()
c.get('http://www.webscrapingfordatascience.com/complexjavascript/')
c.implicitly_wait(10)
div_element = c.find_element_by_class_name('infinite-scroll')
quote_locator = (By.CSS_SELECTOR, '.quote')

nr_quotes = 0
while True:
	chain = ActionChains(c)
	chain.move_to_element(div_element)
	chain.click()
	chain.send_keys([Keys.PAGE_DOWN for i in range(10)])
	chain.perform()

	try:
		all_quotes = WebDriverWait(c, 10).until(
			at_least_n_elements_found(quote_locator, nr_quotes+1)
		)
	except TimeoutException:
		print('Done...!!!')
		break

	nr_quotes = len(all_quotes)
	print('Now seeing ', nr_quotes, ' Quotes')

print(len(all_quotes), 'Quotes Found....!!!')

for q in all_quotes:
	print(q.text)

input('Enter to Exit...')
c.quit()