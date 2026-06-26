# 🤖 AI Customer Review Analyzer

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-29B5E8)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B)

## 🚀 Live App
👉 [https://lalithreddy-review-analyzer.streamlit.app/](https://lalithreddy-review-analyzer.streamlit.app/)

## 📌 Project Overview
AI-powered customer review analyzer that uses OpenAI GPT-3.5 to extract sentiment, themes, and summaries from Amazon product reviews. Results are stored in Snowflake and visualized in an interactive Streamlit dashboard.

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Data processing & pipeline |
| OpenAI GPT-3.5 | Sentiment & theme extraction |
| Snowflake | Cloud storage for analyzed reviews |
| Streamlit | Interactive dashboard |
| Plotly | Data visualizations |
| Git/GitHub | Version control |

## 📊 What It Does
- Analyzes 50 Amazon reviews using GPT-3.5
- Extracts sentiment (positive/negative/neutral)
- Identifies key themes per review
- Generates one-line summaries
- Stores results in Snowflake
- Interactive Q&A — ask AI anything about the reviews

## 📈 Key Metrics
- 86% Positive sentiment
- 7.8/10 Average AI Score
- 50 reviews analyzed

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```