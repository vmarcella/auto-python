import re

# very simple regex searches
print(re.search(r"LOG", "LOGs"))

# Will print none, no match is found.
print(re.search(r"LOG", "NOT A MATCH"))

# Search for LOG at the beginning of the string (Returns NOne)
print(re.search(r"^LOG", "SOME LOGS"))

# Serach for LOG at the end of a string
print(re.search(r"LOG$", "SOME LOGS"))

# Match the first "thing" occurence within our rand_string
rand_string = "something in the things she shows me"
match = re.search(r"thing", rand_string)

# Print out str and match
print("Printing random string")
print(rand_string)
print("\nPrinting match within the string")
print(match)

# Print out up to where the match is found
# then from where it starts till where it stops
# then from the end until the
print("\nPrinting the string sliced")
print(rand_string[: match.start()])
print(rand_string[match.start() : match.end()])
print(rand_string[match.end() :])

# Search for a pattern that contains numbers and dashes
phone_num = "the phone number is 1234-567-890"
print("\nMatching any pattern that contains either numbers or dashes")
print(phone_num)
print(re.search(r"[0123456789-]+", phone_num))

# Naively search for a pattern that matches an email.
email_address = "my email is email.123@test.com"
print("\nMatching any pattern that resembles a basic email address format")
print(email_address)
print(re.search(r"\S+@\S+", email_address))
