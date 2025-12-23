import streamlit as st
import requests

api_key = "nMzCxbRsib62PsUAXurccwEVS823cjXTAst3zG2e"
url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")

response = requests.get(url)
content = response.json()

title = content["title"]
st.title(f"{title}")

image_url = content["hdurl"]
response2 = requests.get(image_url)
st.image(response2.content)

explanation = content["explanation"]
st.write(explanation)