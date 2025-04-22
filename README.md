# Social Media Sentiment Analysis

This project analyzes the sentiment of 10,000+ tweets using Natural Language Processing (NLP) techniques. It achieves an accuracy of 85% in classifying tweets as positive, negative, or neutral using NLTK and Scikit-learn. The insights are presented through visualizations, highlighting sentiment trends and customer feedback.

## Features
- **Data Preprocessing**: Cleans tweets by removing URLs, mentions, hashtags, and special characters, followed by tokenization and lemmatization.
- **Model Training**: Uses TF-IDF vectorization and Logistic Regression for sentiment classification.
- **Visualizations**: Generates sentiment distribution plots and word clouds to showcase trends.

## Directory Structure
- `data/`: Raw and processed datasets (not included in the repository).
- `notebooks/`: Jupyter Notebook with the full analysis workflow.
- `src/`: Python scripts for preprocessing, model training, and visualization.
- `visuals/`: Output visualizations (e.g., sentiment trends, word clouds).
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.
- `LICENSE`: MIT License.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/social-media-sentiment-analysis.git
Install dependencies:
bash

Copy
pip install -r requirements.txt
Download NLTK data:
python

Copy
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
Usage
Place your raw tweet dataset in data/raw_tweets.csv with columns tweet and sentiment.
Run the preprocessing script:
bash

Copy
python src/data_preprocessing.py
Train the model:
bash

Copy
python src/model_training.py
Generate visualizations:
bash

Copy
python src/visualization.py
Alternatively, explore the full workflow in notebooks/sentiment_analysis.ipynb.
Results
Accuracy: 85% on the test set.
Visualizations: Sentiment distribution and word clouds saved in visuals/.
License
This project is licensed under the MIT License
