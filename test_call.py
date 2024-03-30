import google.generativeai as genai
import os

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')
#response = model.generate_content('Please summarise this document: ...')
response = model.generate_content('please compose a short and simple sentence in english containing the words "where", "sun", "church" and than translate it to russian')

print(response.text)
