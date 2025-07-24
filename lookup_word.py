# English definition
# Chinese translation
# Pronunciation

import requests 
import spacy



def lookup(word):

    nlp = spacy.load("en_core_web_sm")

    def lemmatize_word(raw_word):
        doc = nlp(raw_word.lower())
        if not doc:
            return raw_word.lower()  # fallback in case it's empty
        return doc[0].lemma_
    
    word = lemmatize_word(word)
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]
    definitions = []

    for meaning in data.get('meanings', []):

        for d in meaning.get('definitions', []):

            definition_text = d.get("definition", "").strip()
            example_text = d.get("example", "").strip()
            if definition_text:  
                definitions.append({
                    "definition": definition_text,
                    "example": example_text
                })

            if len(definitions) >= 3:
                break

        if len(definitions) >= 3:
            break


    audio = ""
    for phon in data.get('phonetics', []):
        if phon.get("audio"):
            audio = phon["audio"]
            break
    
        
    ipa = data.get("phonetic", "")
    if not ipa:
        for phon in data.get("phonetics", []):
            if phon.get("text"):
                ipa = phon["text"]
                break
    return {
        "word": word,
        "definitions": definitions,
        "ipa": ipa,
        "audio": audio
    } 

    

if __name__ == "__main__":
    result = lookup("LightED")
    print(result["definitions"])
    print(result["word"])