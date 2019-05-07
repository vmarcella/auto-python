"""
    Automating browsing with selenium web browsing
"""

from selenium import webdriver

# Instantiate selenium
browser = webdriver.Chrome()

# Grab the form that we want
browser.get("https://httpbin.org/forms/post")

# Grab the customer name input field by it's name attribute
customer_name = browser.find_element_by_name("custname")
# Clear the input field
customer_name.clear()
# Send keys to the input field
customer_name.send_keys("Yeetcenzo")

# Repeat the previous process for the telephone
customer_telephone = browser.find_element_by_name("custtel")
customer_telephone.clear()
customer_telephone.send_keys("888-777-6666")

# Repeat the previous process for the email
customer_email = browser.find_element_by_name("custemail")
customer_email.clear()
customer_email.send_keys("contact@me.com")

# Iterate through all of our size inputs select the medium size pizza
for size_input in browser.find_elements_by_name("size"):
    if size_input.get_attribute("value") == "medium":
        size_input.click()

# define the wanted toppings and then search through the topping inputs
# till we find the ones that we're looking for.
wanted_toppings = ["bacon", "onion"]
for topping_input in browser.find_elements_by_name("topping"):
    if topping_input.get_attribute("value").lower() in wanted_toppings:
        topping_input.click()

# Submit the form and close the browser
browser.find_element_by_tag_name("form").submit()
browser.quit()
