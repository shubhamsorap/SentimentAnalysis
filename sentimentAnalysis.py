#import docx2txt
#pip install textblob
import pandas as pd
import re
from textblob import TextBlob


def analyse(text):
    my_text = text
    my_text = my_text.replace("”", '"')
    my_text = my_text.replace("“", '"')

    dialogues = re.findall('"([^"]*)"', my_text)
    df = pd.DataFrame({'Dialogue': dialogues})
    df.head()

    df['Dialogue'] = df['Dialogue'].str.replace('\n', '')
    df['Dialogue'] = df['Dialogue'].str.replace("[^a-zA-Z]", " ")
    df['Dialogue'] = df['Dialogue'].str.lower()
    df.head()

    df['Subjectivity'] = df['Dialogue'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    df['Polarity'] = df['Dialogue'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df.head(10)

    df['Sentiment'] = df['Polarity'].apply(get_sentiment)
    df.head()
    return df['Sentiment'].value_counts().to_string()


def get_sentiment(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"
