# Maria Rafaela Abrunhosa - 107658
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
from nltk.util import ngrams
import numpy as np

# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')

df = pd.read_csv('tripadvisor_hotel_reviews.csv') # load the data from the given csv

# BASIC EDA
print("Data Shape: ", df.shape) # return data shape
print("Data Initial Sample: \n", df.head()) # return first lines of data
print("Data Final Sample: \n", df.tail()) # return last lines of data
print("Data Information: \n", df.info()) # return data datatypes
print("Data Description: \n", df.describe()) # return the summary statistics

# DATA CLEANING
print("Missing values: \n", df.isnull()) # check for missing values
print("Count of missing values in each field: \n", df.isnull().sum()) # CONCLUSION: there are no missing values so we skip the missing values addressing

# all text is in lower case, no need to convert
# check if there is need to remove non-alphabetic characters due to the expectation

# sentence tokenization
df['sentences'] = df['Review'].apply(sent_tokenize)
print("Sentences:", df['sentences'].head())

df['cleanedSentences'] = df['Review'].apply(lambda x: re.sub(r'[^\w\s]', '', x.lower())) # remove pontuation

# word tokenization > break-done sentences into words
df['words'] = df['cleanedSentences'].apply(word_tokenize)
print("Words:", df['words'].head())

# method to remove stopwords
stopwords = set(stopwords.words('english')) # english because the text is in english
df['filteredWords'] = df['words'].apply(lambda words: [word for word in words if word not in stopwords])
print("Filtered Words:", df['filteredWords'].head())

# stemming and lemmatization
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
df['stemmedWords'] = df['filteredWords'].apply(lambda filteredWords: [stemmer.stem(word) for word in filteredWords])
df['lemmatizedWords'] = df['filteredWords'].apply(lambda filteredWords: [lemmatizer.lemmatize(word) for word in filteredWords])
print("Stemmed Words:", df['stemmedWords'].head())
print("Lemmatized Words:", df['lemmatizedWords'].head())

# VISUALIZATION
fig, axes = plt.subplots(1, 3, figsize=(12, 6))

# review length plot distribution
df['reviewLen'] = df['Review'].apply(len)

sns.histplot(df['reviewLen'], kde=True, color='skyblue', bins=30, ax=axes[0])
# plt.title('Review Length Distribution')
# plt.xlabel('Word Count')
# plt.ylabel('Frequency')
# plt.show()

# words count plot distribution
# df['wordsCount'] = df['filteredWords'].apply(len)
df['wordsCount'] = df['words'].apply(len)

sns.histplot(df['wordsCount'], kde=True, color='blue', bins=30, ax=axes[1])
# plt.title('Word Count Distribution')
# plt.xlabel('Word Count')
# plt.ylabel('Frequency')
# plt.show()

# sentences length plot distribution
df['sentencesLength'] = df['sentences'].apply(len)

sns.histplot(df['sentencesLength'], kde=True, color='pink', bins=30, ax=axes[2])
# plt.title('Sentences Length Distribution')
# plt.xlabel('Sentence Count')
# plt.ylabel('Frequency')
# plt.show()

axes[0].set_title('Review Length Distribution')
axes[1].set_title('Word Count Distribution')
axes[2].set_title('Sentences Length Distribution')

axes[0].set_xlabel('Word Count')
axes[0].set_ylabel('Frequency')
axes[1].set_xlabel('Word Count')
axes[1].set_ylabel('Frequency')
axes[2].set_xlabel('Sentence Count')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# top 10 most frequently occuring words
wordFrequency= df['stemmedWords'].explode().value_counts().head(10)
wordFrequencyDf = pd.DataFrame({'word': wordFrequency.index, 'frequency': wordFrequency.values})

plt.figure(figsize=(12, 6))
sns.barplot(x='word', y='frequency', data=wordFrequencyDf)
plt.title('Top 10 Most Frequent Words')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# top 10 most frequently occuring bi-grams and tri-grams
# df['biGrams'] = df['Review'].apply(lambda x: ' '.join(x.split()))
# df['triGrams'] = df['Review'].apply(lambda x: [' '.join(nltk.ngrams(word_tokenize(x), n)) for n in [2, 3]])

df['biGrams'] = df['filteredWords'].apply(lambda x: [' '.join(gram) for gram in ngrams(x, 2)])
df['triGrams'] = df['filteredWords'].apply(lambda x: [' '.join(gram) for gram in ngrams(x, 3)])

# Create bi-grams DataFrame
biGramsFrequency = df['biGrams'].explode().value_counts().head(10)
biGramsDf = pd.DataFrame({'biGram': biGramsFrequency.index, 'frequency': biGramsFrequency.values})

# Create tri-grams DataFrame
triGramsFrequecy = df['triGrams'].explode().value_counts().head(10)
triGramsDf = pd.DataFrame({'triGram': triGramsFrequecy.index, 'frequency': triGramsFrequecy.values})

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

sns.barplot(x='biGram', y='frequency', data=biGramsDf,  ax=axes[0])
plt.xticks(rotation=90)

sns.barplot(x='triGram', y='frequency', data=triGramsDf,  ax=axes[1])
plt.xticks(rotation=90)

axes[0].set_title('Top 10 Most Frequent BiGrams')
axes[1].set_title('Top 10 Most Frequent TriGrams')
plt.tight_layout()
plt.show()