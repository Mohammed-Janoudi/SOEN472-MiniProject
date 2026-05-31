# Support assistant for COMP 472 mini project 1

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
SENTIMENT_MODEL_NAME = "sentiment-analysis"
ESCALATION_THRESHOLD = 0.9


class SupportAssistant:
    def __init__(self, knowledge_base_path):
        self.knowledge_base_path = knowledge_base_path
        self.questions = []
        self.answers = []
        self.embedding_model = None
        self.question_embeddings = None
        self.sentiment_pipeline = None
        # TODO: load_knowledge_base(), load_models(), generate_embeddings()

    def load_knowledge_base(self):
        df = pd.read_csv(self.knowledge_base_path)
        self.questions = df["question"].tolist()
        self.answers = df["answer"].tolist()

    def load_models(self):
        self.embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        self.sentiment_pipeline = pipeline(SENTIMENT_MODEL_NAME)

    def generate_embeddings(self):
        self.question_embeddings = self.embedding_model.encode(self.questions)

    def semantic_search(self, query):
        query_embedding = self.embedding_model.encode(query)
        similarities = cosine_similarity([query_embedding], self.question_embeddings)[0]
        best_match = similarities.argmax()
        return self.answers[best_match]

    def analyze_sentiment(self, text):
        # run the pipeline and return the label + score
        raise NotImplementedError

    def should_escalate(self, label, score):
        # negative sentiment with confidence over the threshold
        raise NotImplementedError
