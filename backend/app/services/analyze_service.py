from transformers import pipeline

# Pipeline laden (vortrainiertes Modell für Textklassifikation)
classifier = pipeline("sentiment-analysis")

def analyze_text(text: str) -> list:
    """
    Analysiert Text und stuft jeden Satz als 'relevant', 'unsicher', etc. ein.
    Gibt Liste mit Labeln pro Satz zurück.
    """
    results = []
    for sentence in text.split("."):
        sentence = sentence.strip()
        if sentence:
            classification = classifier(sentence)[0]
            results.append({
                "text": sentence,
                "label": classification["label"],
                "score": round(classification["score"], 2)
            })
    return results