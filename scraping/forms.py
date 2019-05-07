import re

import requests
from bs4 import BeautifulSoup


def get_fields():
    """
        Get all of the available inputs from our form
    """
    # Fetch the form
    response = requests.get("https://httpbin.org/forms/post")
    # Parse the page
    page = BeautifulSoup(response.text, "html.parser")
    # grab the form
    form = page.find("form")

    # A regexp for grabbing the fields that we want from the form
    wanted_fields = re.compile("(input|textarea)")

    # A set for all the unique input names in the  form
    input_names = set()

    # Find all occurences of either input or textarea in the
    # forma dn grab the name of the element
    for field in form.find_all(wanted_fields):
        input_names.add(field.get("name"))

    print(input_names)


def send_data():
    """
        send form data to httpbin using the input names we gathered
        from before
    """

    # Create the form data based on what we observed with the input
    # fields
    form_data = {
        "custname": "Yeetcenzo",
        "custtel": "888-777-6666",
        "custemail": "contact@contact.com",
        "size": "small",
        "topping": ["bacon", "onion"],
        "delivery": "203:30",
        "comments": "nada",
    }
    # Send our form data to httpbin
    response = requests.post("https://httpbin.org/post", form_data)

    # Print the response status and what was returned from the server.
    print(response)
    print(response.json())


if __name__ == "__main__":
    get_fields()
    send_data()
