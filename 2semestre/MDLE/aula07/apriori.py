from itertools import combinations

# Dataset
transactions = [
    ['milk', 'bread', 'nuts', 'apple'],
    ['milk', 'bread', 'nuts'],
    ['milk', 'bread'],
    ['milk', 'apple'],
    ['bread', 'apple'],
]

min_support = 0.6
min_confidence = 0.7
transaction_count = len(transactions)

# First pass: count support for 1-itemsets in a single pass
item_counts = {}
for transaction in transactions:
    for item in transaction:
        item_counts[item] = item_counts.get(item, 0) + 1

frequent_1_itemsets = []
support_data = {}

# Compute support and filter by min_support
for item, count in item_counts.items():
    support = count / transaction_count
    if support >= min_support:
        itemset = (item,)
        frequent_1_itemsets.append(itemset)
        support_data[itemset] = support

# Step 2: Generate candidate 2-itemsets and compute support
candidate_2_itemsets = list(combinations(frequent_1_itemsets, 2))
frequent_2_itemsets = []

for pair in candidate_2_itemsets:
    itemset = tuple(sorted(set(pair[0] + pair[1])))
    
    # Manual support count 
    count = 0
    for transaction in transactions:
        match = True
        for item in itemset:
            if item not in transaction:
                match = False
                break
        if match:
            count += 1

    support = count / transaction_count
    if support >= min_support:
        frequent_2_itemsets.append(itemset)
        support_data[itemset] = support

# Combine itemsets
frequent_itemsets = frequent_1_itemsets + frequent_2_itemsets

# Step 3: Association Rules
rules = []
for itemset in frequent_2_itemsets:
    for i in range(len(itemset)):
        antecedent = (itemset[i],)
        consequent = tuple(item for j, item in enumerate(itemset) if j != i)
        if support_data.get(antecedent):
            confidence = support_data[itemset] / support_data[antecedent]
            if confidence >= min_confidence:
                rules.append((antecedent, consequent, confidence))

# Output
print("Frequent Itemsets (k=1,2):")
for itemset in frequent_itemsets:
    print(f"{itemset} -> support: {support_data[itemset]:.2f}")

print("\nAssociation Rules:")
for antecedent, consequent, confidence in rules:
    print(f"{antecedent} -> {consequent} (confidence: {confidence:.2f})")