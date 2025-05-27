class CharEncoder:
    def __init__(self, corpus):
        self.unique_chars = sorted(list(set(corpus)))
        self.char_to_index = {char: idx for idx, char in enumerate(self.unique_chars)}
        self.index_to_char = {idx: char for idx, char in enumerate(self.unique_chars)}

    def encode(self, text):
        return [self.char_to_index[char] for char in text]

    def decode(self, indices):
        return ''.join([self.index_to_char[idx] for idx in indices])

sample_text = "AJICSJBDBB(bdjbf+#+#+ä1+289zuHUjqfjqi0ß234ß59ß0IEJIFJÜJü239i40ßi+4kt+#+#+iifmawefH9dß90"
encoder = CharEncoder(sample_text)

encoded_text = encoder.encode("ABC")
decoded_text = encoder.decode(encoded_text)

print("Encoded:", encoded_text)
print("Decoded:", decoded_text)
