# Support assistant for COMP 472 mini project 1

import pandas as pd
from sentence_transformers import SentenceTransformer
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
        # encode all the questions once and keep them around
        raise NotImplementedError

    def semantic_search(self, query):
        # embed the query, find the closest stored question, return its answer
        raise NotImplementedError

    def analyze_sentiment(self, text):
        # run the pipeline and return the label + score
        raise NotImplementedError

    def should_escalate(self, label, score):
        # negative sentiment with confidence over the threshold
        raise NotImplementedError
