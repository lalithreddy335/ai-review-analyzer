import pandas as pd
from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Load dataset
df = pd.read_csv('Reviews.csv')
df = df.head(50)
print(f"Loaded {len(df)} reviews")

def analyze_review(review_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"""Analyze this product review and return JSON only:
{{
  "sentiment": "positive/negative/neutral",
  "score": 1-10,
  "theme": "main topic in 2-3 words",
  "summary": "one sentence summary"
}}

Review: {review_text[:500]}"""
        }],
        max_tokens=150
    )
    return response.choices[0].message.content

results = []
for i, row in df.iterrows():
    try:
        result = analyze_review(str(row['Text']))
        data = json.loads(result)
        data['review_id'] = i
        data['original_score'] = row['Score']