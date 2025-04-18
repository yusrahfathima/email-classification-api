# models.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

def train_and_save_model():
    try:
        df = pd.read_csv("data/sample_data.csv")

        if 'email_body' not in df.columns or 'category' not in df.columns:
            raise ValueError("CSV must contain 'email_body' and 'category' columns.")

        X = df["email_body"]
        y = df["category"]

        model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB())
        ])

        model.fit(X, y)

        os.makedirs("saved_models", exist_ok=True)
        joblib.dump(model, "saved_models/classifier.pkl")

        print("✅ Model trained and saved successfully.")

    except Exception as e:
        print(f"❌ Error training model: {e}")

if __name__ == "__main__":
    train_and_save_model()
