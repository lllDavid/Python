from re import findall
from itertools import zip_longest

class Tokenizer:
    def __init__(self, code: str):
        self.code = code
        self.tokens = []
        self.numbers = []
        self.operators = []

    def tokenize(self):
        self.tokens = [
           ("Number", findall(r"-?\d+\.\d+|-?\d+", self.code)),
            ("Operator", findall(r"[+\-*/%^=<>!&|]+", self.code))
        ]
        # TODO: Dont match "-" if negative number
        self.numbers = self.tokens[0][1]  
        self.operators = self.tokens[1][1]  

    def display_tokens(self):
        for token_type, matches in self.tokens:
            print(f"{token_type}: {matches}")

    def display_number_operator_pairs(self):
        pairs = []
        for num, op in zip_longest(self.numbers, self.operators):
            print(f"Number: {num} \nOperator: {op}")
            pairs.append((num, op))
        return pairs  
'''
code = "1 + 2 - 3 * 4 / 5"
tokenizer = Tokenizer(code)
tokenizer.tokenize()  
tokenizer.display_tokens() 
tokenizer.display_number_operator_pairs() 
'''
