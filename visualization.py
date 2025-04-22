import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_sentiment_trends(input_file, output_path):
    """Plot sentiment distribution and save the figure."""
    df = pd.read_csv(input_file)
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Distribution')
    plt.savefig(f'{output_path}/sentiment_trends.png')
    plt.close()

def generate_wordcloud(input_file, output_path):
    """Generate a word cloud of tweets."""
    df = pd.read_csv(input_file)
    text = ' '.join(df['processed_tweet'])
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(f'{output_path}/feedback_wordcloud.png')
    plt.close()

if __name__ == "__main__":
    plot_sentiment_trends('data/processed_tweets.csv', 'visuals')
    generate_wordcloud('data/processed_tweets.csv', 'visuals')
