from bs4 import BeautifulSoup
import requests

# The results from the function can be made 'prettier' by using string formatting


def short_def(search_):
    """Scrapes wikipedia to return a short definition of string as argument."""
    source = requests.get(f'https://en.wikipedia.org/wiki/{search_}').text

    soup = BeautifulSoup(source, 'lxml')
    # Narrowing the way down to item of intrest (first paragraph of wikipedia page) in the html text from internet
    intrs = soup.body
    intrs = intrs.find('div', class_='mw-body')
    intrs = intrs.find('div', class_='vector-body')
    intrs_list = intrs.find_all('p', class_='')
    # By observations, it was found that only that the paragraph tag containing nested bold tag is the item of interest.
    # but that may not be true always as I only tested the program on few pages.
    for item in intrs_list:
        if item.b:
            intrs = item
            break
    heading = intrs.b.text
    # When the search is not found the server responds with "Other reasons this message may be displayed:",
    # which is quite ambiguous of an 'not found message' so, this function returns this not found which gives better
    # idea of what went wrong.
    if heading.startswith('Other reasons this'):
        return "Sorry, your search can't be found. Try again with different words."

    if intrs.text.endswith('may refer to:\n'):
        return "Sorry, your search can't be found. Try again with different words."

    return f">>>{heading.title()}\n{intrs.text}"


def wiki(search_):
    """A modified version of short_def, which returns the definition of argument as well as
    definitions of all the keywords found within the definition of argument."""
    source = requests.get(f'https://en.wikipedia.org/wiki/{search_}').text

    soup = BeautifulSoup(source, 'lxml')
    intrs = soup.body
    intrs = intrs.find('div', class_='mw-body')
    intrs = intrs.find('div', class_='vector-body')
    intrs_list = intrs.find_all('p', class_='')
    for item in intrs_list:
        if item.b:
            intrs = item
            break
    sl = [search_]
    # On some pages there can be a tags which does not have a title key, and can causes the function to
    # return an error. This for loop filters out the tags without exceptions.
    for x in intrs.find_all('a'):
        try:
            sl.append(x['title'])
        except KeyError:
            continue
    for s in sl:
        yield short_def(s)
