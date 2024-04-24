
import wikipedia

def main():
    while True:
        # Prompt the user for input
        search_input = input("Enter a page title or search phrase (press Enter to quit): ").strip()

        # If the user enters blank input, exit the loop
        if not search_input:
            break

        try:
            # Search for the page
            page_title = wikipedia.search(search_input)[0]  # Assuming the first search result
            page = wikipedia.page(page_title, auto_suggest=False)

            # Print page title, summary, and URL
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
            print()
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation Error: Please specify your search term further.")
        except wikipedia.exceptions.PageError:
            print("Page Error: The page does not exist.")

if __name__ == "__main__":
    main()
