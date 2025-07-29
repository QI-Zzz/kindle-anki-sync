from googletrans import Translator

translator = Translator()

def translate_to_chinese(word):
    result = translator.translate(word, src='en', dest='zh-cn')
    return result.text

if __name__ == "__main__":
    print(translate_to_chinese("light"))
    print(translate_to_chinese("serendipity"))