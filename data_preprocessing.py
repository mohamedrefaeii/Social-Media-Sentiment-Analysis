import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_tweet(tweet):
    """Clean a tweet by removing URLs, mentions, hashtags, and special characters."""
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)  # Remove URLs
    tweet = re.sub(r'@\w+|\#\w+', '', tweet)  # Remove mentions and hashtags
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Remove special characters
    return tweet.lower()

def preprocess_tweets(input_file, output_file):
    """Preprocess tweets and save to a new CSV."""
    df = pd.read_csv(input_file)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    df['cleaned_tweet'] = df['tweet'].apply(clean_tweet)
    df['tokens'] = df['cleaned_tweet'].apply(word_tokenize)
    df['tokens'] = df['tokens'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x if word not in stop_words])
    df['processed_tweet'] = df['tokens'].apply(lambda x: ' '.join(x))
    
    df.to_csv(output_file, index=False)
    return df

if __name__ == "__main__":
    preprocess_tweets('data/raw_tweets.csv', 'data/processed_tweets.csv')
