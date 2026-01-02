# stats.py

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sorted_char_report(char_counts):
    """
    Converts a char_counts dictionary into a sorted list of dictionaries
    with {"char": <char>, "num": <count>}, sorted descending by count.
    Non-alphabetical characters are skipped.
    """
    report = []
    
    # Convert dictionary to list of dicts, filter alphabetic
    for char, count in char_counts.items():
        if char.isalpha():  # skip non-alphabet characters
            report.append({"char": char, "num": count})
    
    # Define a helper function to sort by "num"
    def sort_key(entry):
        return entry["num"]
    
    # Sort in-place, descending by count
    report.sort(key=sort_key, reverse=True)
    
    return report
