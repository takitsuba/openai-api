import os
import openai

if __name__ == "__main__":
    openai.api_key = os.environ.get("API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="次の文章を簡潔にしてください。\n最近なんていうか最近英語の会話を話すのが苦手。",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    cleaned_text = response["choices"][0]["text"]

    print(cleaned_text)
