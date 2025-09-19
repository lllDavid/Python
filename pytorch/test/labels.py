import random
from itertools import combinations

from data.data_generator import generate_data_dict  


def generate_pairs(num_devices=70, samples_per_device=30, balance_pairs=True):
    all_samples = []
    all_labels = []

    for device_id in range(num_devices):
        for _ in range(samples_per_device):
            sample = generate_data_dict(device_id)
            all_samples.append(sample)
            all_labels.append(device_id)

    pos_pairs = []
    neg_pairs = []

    total_pairs = (len(all_samples) * (len(all_samples) - 1)) // 2
    pair_count = 0

    for (i, sample_i), (j, sample_j) in combinations(enumerate(all_samples), 2):
        pair_count += 1
        label = 1 if all_labels[i] == all_labels[j] else 0
        print(f"Creating pair {pair_count} of {total_pairs}")
        pair = (sample_i, sample_j)
        if label == 1:
            pos_pairs.append(pair)
        else:
            neg_pairs.append(pair)

    pairs = []
    pair_labels = []

    if balance_pairs:
        for pos_pair in pos_pairs:
            pairs.append(pos_pair)
            pair_labels.append(1)
            neg_pair = random.choice(neg_pairs)
            pairs.append(neg_pair)
            pair_labels.append(0)
    else:
        pairs = pos_pairs + neg_pairs
        pair_labels = [1] * len(pos_pairs) + [0] * len(neg_pairs)

    return pairs, pair_labels
