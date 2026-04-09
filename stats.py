# stats.py contains the helper functions used to analyze a book's text

# Read and return the contents of a file
def get_book_text(path_to_file):

        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents

# Count how many times each character appears in the text
def get_each_ch_count(text):
        lower_text = text.lower()
        counts = {}
        for character in lower_text:
                if character in counts:
                        counts[character] += 1
                else:
                        counts[character] = 1
        return counts

# Return the value used to sort character-count dictionaries
def sort_on(item):
        return item["num"]

# Convert the character-count dictionary into a sorted list of dictionaries
def list_of_dict(char_count):
        new_counts = []
        for char, num in char_count.items():
                dictionary = {"char": char, "num": num}
                new_counts.append(dictionary)
        new_counts.sort(reverse=True, key=sort_on)
        return new_counts
