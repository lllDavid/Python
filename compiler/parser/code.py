from tokenizer.code import Tokenizer

def parse_number(pairs: list):
    digits = []
    for pair in pairs:
        for token in pair:  
            if token and (token.isdigit() or token[0] == '-' and token[1:].isdigit()):  
                digits.append(int(token))
            elif token and '.' in token:  
                digits.append(float(token))
    print(type(digits[0]))
    print(digits)
    return digits

# *, /, %
def parse_term():
     pass
# +, -
def parse_expression():
     pass

if __name__ == "__main__":
    code = "1.2 + 2 - 3 * -4.5 / 5"
    tk = Tokenizer(code)
    tk.tokenize()  
    pairs = tk.display_number_operator_pairs()  
    parse_number(pairs)  

