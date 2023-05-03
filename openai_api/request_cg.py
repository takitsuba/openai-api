import os
import sys
import openai


if __name__ == "__main__":
    message = sys.argv[1]

    openai.api_key = os.environ.get("API_KEY")

    completion = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo", 
        model="gpt-4",
        messages=[{"role": "user", "content": message}]
    )

    print(completion)
