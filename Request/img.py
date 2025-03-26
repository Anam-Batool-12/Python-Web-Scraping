import requests
from PIL import Image
from io import BytesIO
image_url = "https://plus.unsplash.com/premium_photo-1664474619075-644dd191935f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = requests.get(image_url)

if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    img.save("img.jpg")
    print("Image saved successfully.")
else:
    print("Failed to retrieve image. Status code:", response.status_code)
