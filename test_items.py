import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_basket(browser):
	browser.get(link)
	time.sleep(30)
	button = browser.find_element_by_class_name("btn-add-to-basket")
	assert button, "Basket button not found"
