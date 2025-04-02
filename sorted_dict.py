input_text = "Some random text without much sense"

def letter_count(text):
    char_counts = {}
    
    lowercase_text = text.lower()
    words = lowercase_text.split()

    for word in words:
        for char in word:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
    
    sorted_counts = dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
    return sorted_counts

print(letter_count(input_text))