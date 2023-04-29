import os
import openai
import argparse

def main(input_text):
    openai.organization = os.environ['OPENAI_API_ORG']
    openai.api_key = os.environ['OPENAI_API_KEY']
    message = {"role": "user", "content": f"Reply very briefly in not more than 2 sentences. {input_text}"}
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[message])
    print('*' * 20)
    print(f"User: {input_text}")
    print(f"GPT: {completion.choices[0].message.content.strip()}")
    print('*' * 20)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='API calls to Google Cloud Natural Language API')
    parser.add_argument('arg1', type=str, help='input text')
    args = parser.parse_args()
    input_text = args.arg1
    main(input_text)