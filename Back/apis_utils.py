import openai
import requests

class OpenAI:

    image_urls = []
    MIN_HEIGHT = 600
    MIN_WIDTH = 800
    API_KEY = ""
    GOOGLE_API_KEY = ""
    CX = ""

    def __init__(self):
        openai.api_key = self.API_KEY

    def chatgpt_text(self, question):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional chef."},
                {"role": "user", "content": question}
            ]
        )
        return completion.choices[0].message['content']

    def search_image(self, query):
        url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={self.GOOGLE_API_KEY}&cx={self.CX}&searchType=image'
        response = requests.get(url)
        result = response.json()
        return result
