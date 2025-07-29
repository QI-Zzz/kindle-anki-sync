import requests
import os


def note_exists(word):

    payload = {
        'action': 'findNotes',
        'version': 6,
        "params": {
            "query": f'front:"{word}" deck:"Kindle Vocabulary"'
        }
    }

    r = requests.post("http://localhost:8765", json=payload)
    return r.json()["result"] != []

def download_audio(audio_url):
    if not audio_url:
        return None

    filename = audio_url.split("/")[-1]
    anki_media_path = os.path.expanduser("~/Library/Application Support/Anki2/Zhizhi/collection.media")
    save_path = os.path.join(anki_media_path, filename)
    
    folder = "anki_media"
    os.makedirs(folder, exist_ok=True)

    try:
        response = requests.get(audio_url)
        with open(save_path, "wb") as f:
            f.write(response.content)
        return filename  
    except Exception as e:
        return None
    
def add_card(word, ipa, definition_list, translation, audio_url):
    back = f"{ipa}<br>{translation}<br>"

    for i, d in enumerate(definition_list):
        back += f"<br>{i+1}: {d['definition']}"
        if d['example']:
            back += f"<br><i>→ {d['example']}</i>"

    audio_filename = download_audio(audio_url)
    if audio_filename:
        back += f"<br><br>[sound:{audio_filename}]"

    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Kindle Vocabulary",
                "modelName": "Basic",
                "fields": {
                    "Front": word,
                    "Back": back
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": ["kindle"],
                # "audio": [
                #     { "path": os.path.abspath(os.path.join("anki_media", audio_filename)),
                #     "filename": audio_filename,
                #     "fields": ["Back"]}
                # ] if audio_filename else []
            }
        }
    }

    response = requests.post("http://localhost:8765", json=payload)
    return response.json()


if __name__ == "__main__":
    word = "serendipity"
    ipa = "ˌsɛrənˈdɪpɪti"
    definitions = [
        {"definition": "The occurrence of events by chance in a happy way.", "example": "Meeting her was pure serendipity."}
    ]
    translation = "机缘巧合"
    audio_url = "https://api.dictionaryapi.dev/media/pronunciations/en/serendipity-us.mp3"

    result = add_card(word, ipa, definitions, translation, audio_url)
    print(result)