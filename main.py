import sys
from stats import count_words, count_characters, sorted_char_report

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    
    # Word count
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    
    # Character count
    char_counts = count_characters(book_text)
    
    # Sorted character report
    report = sorted_char_report(char_counts)
    
    # Print results
    for entry in report:
        print(f"{entry['char']}: {entry['num']}")

# ✅ Only run main() if script is executed directly
if __name__ == "__main__":
    main()
