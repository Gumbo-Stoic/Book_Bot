# main.py ties everything together and prints the final report

# Import system tools and helper functions from stats.py
import sys
from stats import get_each_ch_count, get_book_text, list_of_dict


# Check that exactly two command-line argument was provided
# so the program knows which book file to analyze
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

# If a valid book path was provided, generate and print the report
else:
	def main():
		text = get_book_text(sys.argv[1])
		char_count = get_each_ch_count(text)
		sorted_keys = list_of_dict(char_count)
		word_lenght = len(text.split())
		print(f"============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print(f"----------- Word Count ----------")
		print(f"Found {word_lenght} total words")
		print(f"--------- Character Count -------")
	
		for key in sorted_keys:
			if key["char"].isalpha():
				print(f"{key["char"]}: {key["num"]}")

		print("============= END ===============")

	main()
