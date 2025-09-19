import torch
from torch.utils.data import TensorDataset, DataLoader

from labels import generate_pairs
from encode import encode_sample


def compute_feature_stats(pairs):
    encoded_list = []
    for s1, s2 in pairs:
        encoded_list.append(encode_sample(s1))
        encoded_list.append(encode_sample(s2))
    all_encoded = torch.stack(encoded_list)  
    mean = all_encoded.mean(dim=0)           
    std = all_encoded.std(dim=0)
    std_safe = std.clone()
    std_safe[std_safe < 1e-6] = 1.0
    return mean, std_safe


def create_pair_dataset(pairs, pair_labels, mean, std_safe):
    normalized_pairs_1 = []
    normalized_pairs_2 = []
    for s1, s2 in pairs:
        enc1 = encode_sample(s1)
        enc2 = encode_sample(s2)
        norm1 = (enc1 - mean) / std_safe
        norm2 = (enc2 - mean) / std_safe
        normalized_pairs_1.append(norm1)
        normalized_pairs_2.append(norm2)
    X1 = torch.stack(normalized_pairs_1)
    X2 = torch.stack(normalized_pairs_2)
    y = torch.tensor(pair_labels, dtype=torch.float)
    return TensorDataset(X1, X2, y)


'''
def verify_pairs(pairs, pair_labels):
    for i, (pair, label) in enumerate(zip(pairs, pair_labels)):
        sample1, sample2 = pair
        device1 = sample1.get('device_id')
        device2 = sample2.get('device_id')
        
        if label == 1 and device1 != device2:
            print(f"Error at pair {i}: Label is 1 but devices differ ({device1} != {device2})")
        elif label == 0 and device1 == device2:
            print(f"Error at pair {i}: Label is 0 but devices are the same ({device1})")
    print("Verification complete.")
'''

pairs, pair_labels = generate_pairs()
# verify_pairs(pairs, pair_labels)

mean, std_safe = compute_feature_stats(pairs)
dataset = create_pair_dataset(pairs, pair_labels, mean, std_safe)

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
bx1, bx2, by = next(iter(train_loader))
bx1 = bx1.float()
fm = bx1.mean(dim=0).mean().item()
fs = bx1.std(dim=0).mean().item()
mn = bx1.min().item()
mx = bx1.max().item()
val_loader = DataLoader(val_dataset, batch_size=32)