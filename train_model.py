import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle
import os

# Dataset path
DATA_PATH = "data/train.csv"
MODEL_PATH = "models/faq_model.pkl"

# 1. Load dataset
df = pd.read_csv(DATA_PATH)
questions = df["Question"].astype(str).tolist()
answers = df["Answer"].astype(str).tolist()

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Encode questions
embeddings = model.encode(questions, convert_to_tensor=False)

# 4. Save as dictionary
model_data = {
    "vectorizer": model,
    "embeddings": embeddings,
    "questions": questions,
    "answers": answers
}

os.makedirs("models", exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model_data, f)

print(f"✅ Model trained and saved at {MODEL_PATH}")
