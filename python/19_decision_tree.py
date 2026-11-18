# Experiment 19: Decision Tree (ID3 algorithm using information gain, from scratch)
import math
from collections import Counter

# Play-Tennis dataset
features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
data = [
    ('Sunny', 'Hot', 'High', 'Weak', 'No'),
    ('Sunny', 'Hot', 'High', 'Strong', 'No'),
    ('Overcast', 'Hot', 'High', 'Weak', 'Yes'),
    ('Rain', 'Mild', 'High', 'Weak', 'Yes'),
    ('Rain', 'Cool', 'Normal', 'Weak', 'Yes'),
    ('Rain', 'Cool', 'Normal', 'Strong', 'No'),
    ('Overcast', 'Cool', 'Normal', 'Strong', 'Yes'),
    ('Sunny', 'Mild', 'High', 'Weak', 'No'),
    ('Sunny', 'Cool', 'Normal', 'Weak', 'Yes'),
    ('Rain', 'Mild', 'Normal', 'Weak', 'Yes'),
    ('Sunny', 'Mild', 'Normal', 'Strong', 'Yes'),
    ('Overcast', 'Mild', 'High', 'Strong', 'Yes'),
    ('Overcast', 'Hot', 'Normal', 'Weak', 'Yes'),
    ('Rain', 'Mild', 'High', 'Strong', 'No'),
]
rows = [dict(zip(features + ['Play'], r)) for r in data]


def entropy(rows):
    counts = Counter(r['Play'] for r in rows)
    total = len(rows)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def info_gain(rows, attr):
    total = len(rows)
    remainder = 0
    for v in set(r[attr] for r in rows):
        subset = [r for r in rows if r[attr] == v]
        remainder += len(subset) / total * entropy(subset)
    return entropy(rows) - remainder


def id3(rows, attrs):
    labels = [r['Play'] for r in rows]
    if len(set(labels)) == 1:
        return labels[0]
    if not attrs:
        return Counter(labels).most_common(1)[0][0]
    best = max(attrs, key=lambda a: info_gain(rows, a))
    tree = {best: {}}
    for v in set(r[best] for r in rows):
        subset = [r for r in rows if r[best] == v]
        tree[best][v] = id3(subset, [a for a in attrs if a != best])
    return tree


def print_tree(tree, indent=0):
    if not isinstance(tree, dict):
        print(' ' * indent + '-> ' + tree)
        return
    for attr, branches in tree.items():
        for value, sub in branches.items():
            print(' ' * indent + f'[{attr} = {value}]')
            print_tree(sub, indent + 4)


def predict(tree, sample):
    while isinstance(tree, dict):
        attr = next(iter(tree))
        tree = tree[attr][sample[attr]]
    return tree


print("Information gain of each attribute:")
for a in features:
    print(f"  {a:12} {info_gain(rows, a):.4f}")

tree = id3(rows, features)
print("\nDecision Tree:")
print_tree(tree)

test = {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'}
print("\nNew sample:", test)
print("Prediction (Play Tennis?):", predict(tree, test))
