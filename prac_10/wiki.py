import wikipedia

while True:
    search_phrase = input("Enter a page title or search phrase (or leave blank to quit): ")

    if not search_phrase:
        print("Exiting...")
        break

    try:
        page = wikipedia.page(search_phrase, autosuggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        print("Disambiguation Error: Wikipedia page for '{}' could refer to multiple topics. Please be more specific.".format(
                search_phrase))
    except wikipedia.PageError as e:
        print("Page Error: Wikipedia page for '{}' does not exist.".format(search_phrase))
    except Exception as e:
        print("An error occurred:", e)
