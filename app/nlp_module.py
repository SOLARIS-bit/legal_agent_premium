from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from .legal_texts import LEGAL_TEXTS

# Modèle public CamemBERT pour tests
MODEL_NAME = "camembert-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

nlp_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)

def detect_infractions(text, country="FR"):
    legal_context = LEGAL_TEXTS.get(country, "")
    text_to_analyze = legal_context + " " + text
    results = nlp_pipeline(text_to_analyze, truncation=True)
    return results

def classify_recours(text, country="FR"):
    legal_context = LEGAL_TEXTS.get(country, "")
    text_to_analyze = legal_context + " " + text
    results = nlp_pipeline(text_to_analyze, truncation=True)
    return max(results, key=lambda x: x['score'])['label']
