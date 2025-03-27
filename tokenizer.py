import re

class Tokenizer:
    def __init__(self):
        self.pattern = r'''(?x)          
            (?:[A-Za-z]+(?:[''-][A-Za-z]+)*)  
            | \d+(?:\.\d+)?             
            | [][.,;:!?()"'`{}<>]      
            | \s+                       
        '''

    def tokenize(self, text):
        tokens = re.findall(self.pattern, text)

        return [token for token in tokens if not token.isspace()]

    def tokenize_with_positions(self, text):
        tokens_with_pos = []
        for match in re.finditer(self.pattern, text):
            token = match.group()
            if not token.isspace():  
                tokens_with_pos.append((token, match.start(), match.end()))
        return tokens_with_pos

def main():
    # Sample text
    text = "Hello, world! How's it going? 123.45"
    
    tokenizer = Tokenizer()
    
    tokens = tokenizer.tokenize(text)
    print("Simple tokenization:")
    print(tokens)
    
    tokens_pos = tokenizer.tokenize_with_positions(text)
    print("\nTokenization with positions:")
    for token, start, end in tokens_pos:
        print(f"Token: {token:10} Start: {start:2} End: {end:2}")

if __name__ == "__main__":
    main()