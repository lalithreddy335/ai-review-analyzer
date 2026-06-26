import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
import os

df = pd.read_csv('analyzed_reviews.csv')

st.set_page_config(page_title="AI Review Analyzer", page_icon="🤖", layout="wide")

st.title("🤖 AI Customer Review Analyzer")
st.subheader("Powered by OpenAI GPT-3.5 + Snowflake")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Reviews", len(df))
with col2:
    positive = len(df[df['sentiment'] == 'positive'])
    st.metric("Positive", f"{positive/len(df)*100:.0f}%")
with col3:
    negative = len(df[df['sentiment'] == 'negative'])
    st.metric("Negative", f"{negative/len(df)*100:.0f}%")
with col4:
    avg_score = df['score'].mean()
    st.metric("Avg AI Score", f"{avg_score:.1f}/10")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = df['sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']
    fig1 = px.pie(sentiment_counts, values='Count', names='Sentiment',
                  color_discrete_map={'positive': '#00cc44', 'negative': '#ff4444', 'neutral': '#ffaa00'})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🏷️ Top Themes")
    theme_counts = df['theme'].value_counts().head(10).reset_index()
    theme_counts.columns = ['Theme', 'Count']
    fig2 = px.bar(theme_counts, x='Count', y='Theme', orientation='h',
                  color='Count', color_continuous_scale='blues')
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("⭐ AI Score vs Original Rating")
fig3 = px.scatter(df, x='original_score', y='score',
                  color='sentiment',
                  color_discrete_map={'positive': '#00cc44', 'negative': '#ff4444', 'neutral': '#ffaa00'},
                  labels={'original_score': 'Original Star Rating', 'score': 'AI Sentiment Score'})
st.plotly_chart(fig3, use_container_width=True)

st.subheader("📝 Review Summaries")
st.dataframe(df[['sentiment', 'score', 'theme', 'summary']].head(20), use_container_width=True)

st.divider()
st.subheader("💬 Ask AI About Reviews")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

user_question = st.text_input("Ask a question about the reviews")
if user_question:
    summaries = df['summary'].tolist()[:20]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Based on these review summaries: {summaries}\n\nAnswer: {user_question}"
        }]
    )
    st.write(response.choices[0].message.content)