# openai-api
## Initial setting
1. Create `.env` file

        cp .env.sample .env


2. Get your secret key from openai and add it to the `.env` file.

## How to clean text
    poetry run python openai_api/clean_text.py "最近なんていうか 最近英語の会話を話すのが苦手。"

### An example of the results
    英語会話が苦手だ。
