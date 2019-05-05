import datetime

import delorean
import feedparser
import requests

# Parse the RSS feed
rss = feedparser.parse("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")

# Print when the rss feed was last updated
print(rss.updated)

# Get all articles that have been posted within the last six hours
time_limit = delorean.parse(rss.updated) - datetime.timedelta(hours=6)

# Get all of the entries that have been posted within the last six hours
entries = [
    entry for entry in rss.entries if delorean.parse(entry.published) > time_limit
]

# Diff the amount of time-filtered entries vs all available entries
print(len(entries))
print(len(rss.entries))

# Print out all the titles and links of our filtered entries
for entry in entries:
    print("--New entry--")
    print(entry["title"])
    print(entry["link"] + "\n")

# The title of the rss feed, all information about the feed can be
# found within the feed object
print(rss.feed.title)
