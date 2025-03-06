def map(word):
    pair = (word, 1)
    pairs.append(pair)
    return pairs

def groupKey(pairs):

    for pair in pairs:
        word = pair[0]
        if word not in listGroup:
            listGroup[word] = [pair]
        else:
            listGroup[word].append(pair)

    group = list(listGroup.values())
    return group

def reduce(group):
    for list in group:
        word = list[0][0]
        count = len(list)
        output[word] = count
    return output

input = ["hello world", "hello python", "world of python", "hello again", "python is great"]
words = [] # list of words
pairs = []
listGroup = {}
output = {}

# get words from the input
for sent in input:
    wordsList = sent.split()
    for i in wordsList:
        words.append(i)

# map the input to key-value pairs - initialize all words found to 1
for word in words:
    pairs = map(word)
print("Pairs:", pairs, "\n")

# group all the key-value pairs with the same key
group = groupKey(pairs)
print("Grouping:", group, "\n")

# reduce the group list and create the output dictionary - count the number of equal tuples from the group
output = reduce(group)
print("ouput = ", output)

# output = {"hello" : 3, "python" : 3, "world" : 2, "again" : 1, "of" : 1, "is" : 1, "great" : 1} > gives the right answer