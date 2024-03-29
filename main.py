import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import plotly.express as px

#set_page_config(adalah sebuah metode yang digunakan untuk mengubah parameter dari page kita)
st.title("Youtube Comment Sentiment Analysis")
st.markdown('''Ini merupakan hasil analisa sentimen masyarakat terhadap pembangunan SPB Hidrogen di Indonesia.
            Data diambil dari komentar pada konten Youtube dengan keyword SPBU Hidrogen''')

#baca data
df = pd.read_csv("Dataset_youtube_comments.csv")
df.drop(['like_count', 'public'], axis=1, inplace=True)

if st.checkbox("Show Data"):
    st.write(df)

#menampilkan wordcloud    
data = pd.read_csv("data_analisis.csv")
data.drop(['comment_en'], axis=1, inplace=True)

comment_words = ' '
stopwords = set(STOPWORDS)

for val in data['clean_sw']:
       val = str(val)
       tokens = val.split()
       for i in range(len(tokens)):
              tokens[i] = tokens[i].lower()
       comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
                      background_color = 'white',
                      stopwords = stopwords,
                      min_font_size = 10).generate(comment_words)

image = wordcloud.to_file('wordcloud.gif')

if st.checkbox("Show Wordcloud"):
       st.image('wordcloud.gif')

## Visualisasi
select=st.selectbox('Visualisation Of Data',['Histogram','Pie Chart'],key=1)
sentiment=data['klasifikasi_bayes'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'comments':sentiment.values})
st.markdown("###  Sentiment count")
if select == "Histogram":
        fig = px.bar(sentiment, x='Sentiment', y='comments', color = 'comments', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(sentiment, values='comments', names='Sentiment')
        st.plotly_chart(fig)

st.caption('Copyright (c) Meidi Utami')