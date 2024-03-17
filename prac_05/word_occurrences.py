"""
CP1404/CP5632 Practical

"""
def main():
    text = input("Enter the text: ")
    word_counts = count_words(text)
    for word, count in sorted(word_counts.items()):
        print(f"{word} : {count}")

def count_words(text):
    word_counts = {}
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

main()