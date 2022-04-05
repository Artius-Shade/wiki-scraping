# wiki-scraping
These two functions scrape wikipedia using the Beautiful Soup & Requests Libraries.

## 1. short_def
This function takes a search string and returns a short defenition or a not found message if defenition was not found.

## 2. wiki
This function takes a search string and returns an iterator containing the short definition of the search string and defenitons of
all related terms occuring in the definiton of search string.

 ## Sample Execution
 ```python
from wiki import short_def, wiki

definiton = short_def('apple')
print(definiton)
"""
>>>Apple
An apple is an edible fruit produced by an apple tree (Malus domestica). Apple trees are cultivated worldwide 
and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild 
ancestor, Malus sieversii, is still found today. Apples have been grown for thousands of years in Asia and 
Europe and were brought to North America by European colonists. Apples have religious and mythological significance
in many cultures, including Norse, Greek, and European Christian tradition.
"""

definitions = wiki('fusion')
for definition in definitions:
     print(definition)
""" 
>>>Fusion
Fusion, or synthesis, is the process of combining two or more distinct entities into a new whole.

>>>Syntheses
synthesis (countable and uncountable, plural syntheses)
"""
