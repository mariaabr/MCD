import re # regex

totalwords = 0
distinctwords = []
file = open("FCD/file.txt")
lines = file.readlines() # reads all lines
for line in lines: # we need to go for each line so we can split it by ' '
    lowerLine = line.lower()
    newLine = re.sub(r'[^\w\s]', '', lowerLine) # replace the punctuation
    words = newLine.split()

    for word in words:
        if word not in distinctwords: # if it is an distinct word
            distinctwords.append(word)
        totalwords += 1 # count all words readed

file.close()

# print results
print('Total words:', totalwords)
print('Distinct words:', len(distinctwords))