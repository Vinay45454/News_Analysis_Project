## 2. Entity Extraction
import spacy
from typing import Dict, List

def extract_entities(text: str) -> Dict[str, List[str]]:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Extract entities classified as 'PERSON' or 'ORG'
    entities = {
        "PERSON": list(set(ent.text for ent in doc.ents if ent.label_ == "PERSON")),
        "ORG": list(set(ent.text for ent in doc.ents if ent.label_ == "ORG"))
    }

    return entities

if __name__ == "__main__":
    text = """
    Apple Inc. announced that Tim Cook will be the keynote speaker at the upcoming developer conference. 
    Meanwhile, Elon Musk from Tesla has expressed interest in collaborating with SpaceX for satellite projects.
    """
    entities = extract_entities(text)
    print("Extracted Entities:", entities)