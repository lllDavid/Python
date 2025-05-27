import numpy as np
from main import CharEncoder

class Embedding:
    def __init__(self, vocab_size, embedding_dim):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.weights = np.random.randn(vocab_size, embedding_dim) * 0.01

    def forward(self, indices):
        return self.weights[indices]

    def __call__(self, indices):
        return self.forward(indices)

sample_text = "Example text for embedding."
encoder = CharEncoder(sample_text)

embedding_dim = 8  
embed = Embedding(vocab_size=len(encoder.unique_chars), embedding_dim=embedding_dim)

encoded_indices = encoder.encode("Example")

embeddings = embed(encoded_indices)

print("Encoded indices:", encoded_indices)
print("Embeddings shape:", embeddings.shape)
print("Embeddings:", embeddings)
