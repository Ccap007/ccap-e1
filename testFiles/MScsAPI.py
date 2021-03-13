import requests
import json
import dotenv
from dotenv import load_dotenv
import os

# the variable for the url address of the created service
vision_service_address = "https://thispythonimageanalyzer.cognitiveservices.azure.com/vision/v3.1/"

# the address plus the function to be used, here its analyze 
address = vision_service_address + "analyze"

# the proscribed params of the api per the documentation https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-1-ga/operations/56f91f2e778daf14a499f21b
parameters = {"visualFeatures":"Description,Color", "language":"en"}

# set the image path and open then read the file
image_path = "./Users/Charles/Desktop/python folder/FancyRepo/ccapo-e1/testFiles/jeep.png"
image_data = open("jeep.png", "rb").read()

# uses dotenv pkg to get the DATABASE key pair value from .env
load_dotenv()
password = os.getenv("DATABASE")

# per the documentation, the required headers are being defined here, 
# using the subscription key variable from above
headers = {"Content-Type": "application/octet-stream", "Ocp-Apim-Subscription-Key": password}
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise for Status automatically raises exception to be handled as normal for any error
response.raise_for_status()
results = response.json()

# # loops thru the results descriptions' tags and prints them
# for item in results["description"]["tags"]:
#     print(item)

# all the results raw
print(json.dumps(results))

# print("requestId")
# print(results["requestId"])