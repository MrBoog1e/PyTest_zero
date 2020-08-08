import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checking_the_stores_button (browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('#add_to_basket_form > button')
    assert button, 'The button is missing :('

