import pandas as pd
from openai import OpenAI
import json

client = OpenAI(api_key="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")

# Load dataset
df = pd.read_csv('Reviews.csv')
df = df.head(50)  # Only 50 reviews to save API costs
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
        results.append(data)
        print(f"✅ {i+1}/50 done — {data['sentiment']}")
    except Exception as e:
        print(f"❌ Error on {i}: {e}")

results_df = pd.DataFrame(results)
results_df.to_csv('analyzed_reviews.csv', index=False)
print("🎉 All done! Saved to analyzed_reviews.csv")