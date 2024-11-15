# Maria Rafaela Abrunhosa - 107658
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

# word tokenization > break-done sentences into words
df['words'] = df['Review'].apply(word_tokenize)
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
# review length plot distribution

reviewLen = df['Review'].apply(len)

plt.subplot(1, 3, 1)
sns.histplot(df['review_length'], kde=True, color='skyblue', bins=30)
plt.title('Review Length Distribution')