from tokenizer import code

def parse_factor(liste: list):
    for i in liste:
        print(i)
        for j in i:
            print(j)
            if j.isdigit():
                return int(j)
            else:
                raise ValueError("Error")

code2 = "1 + 2 - 3 * 4 / 5"
tk = code.Tokenizer(code2)

parse_factor(tk.display_number_operator_pairs())