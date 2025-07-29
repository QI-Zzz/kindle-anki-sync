from parse_clippings import get_highlighted_words
from lookup_word import lookup
from translate_word import translate_to_chinese
from anki_add import add_card, note_exists

def process_words(file):

    raw_words = get_highlighted_words(file)


    for raw_word in raw_words:
        
        try: 
            if note_exists(raw_word):
                continue
            
            data = lookup(raw_word)
            if not data:
                continue

            translation = translate_to_chinese(raw_word)
            if not translation:
                continue

            add_card(
                word=raw_word,
                ipa=data['ipa'],
                definition_list=data['definitions'],
                translation=translation,
                audio_url=data["audio"]
            )
        except Exception as e:
            print(f"💥 Error processing '{raw_word}': {e}")

if __name__ == "__main__":
    process_words("My Clippings.txt")