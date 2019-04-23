import re

# very simple regex searches
print(re.search(r"LOG", "LOGs"))
print(re.search(r"LOG", "NOT A MATCH"))
