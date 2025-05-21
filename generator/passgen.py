import random
import string

WORDS = ['tiger', 'mango', 'wave', 'frost', 'sun', 'dog', 'cloud', 'stone', 'river', 'mountain']
SPECIALS = '!@#$%^&*()-_=+[]{}<>?'
NUMBERS = string.digits
SEPARATORS = ['_', '-', '.', '*', '#', '!']

CHAR_SUBSTITUTIONS = {
    'a': '@',
    'o': '0',
    'i': '1',
    'e': '3',
    's': '$',
    't': '7',
}

def random_case(word):
    return ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in word)

def substitute_chars(word):
    result = []
    for c in word:
        if c.lower() in CHAR_SUBSTITUTIONS and random.random() < 0.5:
            result.append(CHAR_SUBSTITUTIONS[c.lower()])
        else:
            result.append(c)
    return ''.join(result)

def insert_random_separators(parts):
    password = parts[0]
    for part in parts[1:]:
        sep = random.choice(SEPARATORS + [''])  
        password += sep + part
    return password

def generate_strong_password(min_words=3, max_words=5):
    num_words = random.randint(min_words, max_words)
    words = random.sample(WORDS, num_words)
    
    styled_words = []
    for w in words:
        w = random_case(w)
        w = substitute_chars(w)
        styled_words.append(w)
    
    password = insert_random_separators(styled_words)
    
    extras = []
    extras.append(''.join(random.choices(NUMBERS, k=2)))
    extras.append(''.join(random.choices(SPECIALS, k=2)))
    
    positions = ['start', 'middle', 'end']
    random.shuffle(positions)
    
    for pos, extra in zip(positions, extras):
        if pos == 'start':
            password = extra + password
        elif pos == 'middle':
            mid = len(password) // 2
            password = password[:mid] + extra + password[mid:]
        else:  
            password = password + extra
    
    return password

if __name__ == "__main__":
    for _ in range(10):
        print(generate_strong_password())
