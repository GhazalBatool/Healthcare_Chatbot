from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load saved model
with open("models/faq_model.pkl", "rb") as f:
    model_data = pickle.load(f)

vectorizer = model_data["vectorizer"]
embeddings = model_data["embeddings"]
questions = model_data["questions"]
answers = model_data["answers"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    user_vec = vectorizer.encode([user_input])
    sims = cosine_similarity(user_vec, embeddings)
    idx = sims.argmax()
    best_answer = answers[idx]
    return jsonify({"reply": best_answer})

if __name__ == "__main__":
    app.run(debug=True)
