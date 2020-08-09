import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checking_the_stores_button (browser):
    browser.get(link)
    addToCartButton = browser.find_elements_by_css_selector(".add-to-basket .btn")
    assert len(addToCartButton) > 0, 'There is no add to cart button'

