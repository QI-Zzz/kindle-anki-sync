from googletrans import Translator
import asyncio

translator = Translator()

async def translate_to_chinese(word):
    async with Translator() as translator:
        result = await translator.translate(word, src='en', dest='zh-cn')
        return result

if __name__ == "__main__":
    print(translate_to_chinese("light"))
    print(translate_to_chinese("serendipity"))
