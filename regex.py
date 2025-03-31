import re

def main(pattern, test_string):
    try:
        compiled_pattern = re.compile(pattern)
        matches = list(compiled_pattern.finditer(test_string))
        
        if not matches:
            print("No matches found.")
            return
        
        print("Matches found:")
        for match in matches:
            print(f"Match: {match.group()} at position {match.start()}-{match.end()}")
            
        highlighted = test_string
        for match in reversed(matches):
            start, end = match.start(), match.end()
            highlighted = highlighted[:start] + "[" + highlighted[start:end] + "]" + highlighted[end:]
        
        print("\nHighlighted string:")
        print(highlighted)
    
    except re.error as e:
        print(f"Invalid regex pattern: {e}")

if __name__ == "__main__":
    pattern = input("Enter regex pattern: ")
    test_string = input("Enter test string: ")
    main(pattern, test_string)