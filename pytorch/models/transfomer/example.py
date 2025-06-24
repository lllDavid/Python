import torch
import torch.nn as nn

# Creates a Transformer encoder that outputs vocabulary logits for each token in a batch of sequences
class Transformer(nn.Module):
    def __init__(self, d_model, nhead, num_layers, vocab_size, max_len=512):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_embedding = nn.Parameter(torch.zeros(1, max_len, d_model))
        
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        seq_len = x.size(1)
        x = self.embedding(x) + self.pos_embedding[:, :seq_len, :]
        out = self.transformer(x)
        return self.fc_out(out)

model = Transformer(d_model=512, nhead=8, num_layers=6, vocab_size=10000)
src = torch.randint(0, 10000, (32, 20)) 
logits = model(src)
print(logits.shape) 