from itertools import product, permutations
from multiprocessing import freeze_support

def insert_separators_in_word(word, separators):
    if len(word) == 1:
        return [word]
    slots = len(word) - 1
    sep_choices = list(product(separators, repeat=slots))
    results = []
    for seps in sep_choices:
        pieces = []
        for i in range(len(word)):
            pieces.append(word[i])
            if i < slots:
                pieces.append(seps[i])
        results.append(''.join(pieces))
    return results

def generate_all_usernames_all_combos(full_name):
    separators = ["", "_", "-", "."]
    parts = full_name.lower().split()
    parts_len = len(parts)
    all_usernames = set()
    expanded_parts = []
    for p in parts:
        variants = insert_separators_in_word(p, separators)
        variants.append(p[0])  
        expanded_parts.append(variants)
    perms = permutations(range(parts_len))
    for perm in perms:
        permuted_expanded_parts = [expanded_parts[i] for i in perm]
        for chosen_parts in product(*permuted_expanded_parts):
            for part_seps in product(separators, repeat=parts_len-1):
                username_pieces = []
                for i, part_str in enumerate(chosen_parts):
                    username_pieces.append(part_str)
                    if i < parts_len-1:
                        username_pieces.append(part_seps[i])
                username = ''.join(username_pieces)
                all_usernames.add(username)
    return sorted(all_usernames)

if __name__ == '__main__':
    freeze_support()
    
    name = "Username" # Name to generate from
    usernames = generate_all_usernames_all_combos(name)
    print(f"Generated {len(usernames)} usernames!")

    with open("usernames.txt", "w", encoding="utf-8") as f:
        for username in usernames:
            f.write(username + "\n")
