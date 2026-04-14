import time
import os
import subprocess
from datetime import datetime, timezone
from inference_sdk import InferenceHTTPClient, InferenceConfiguration
import firebase_admin
from firebase_admin import firestore

image = "/home/utcparking/python_projects/parkingtracker/image.jpg" # name of the image, including full path
config = InferenceConfiguration(confidence_threshold=0.5, iou_threshold=0.5) # configuration for the inference model (50% confidence and 50% overlap)
client = InferenceHTTPClient(api_url="http://localhost:9001", api_key=os.environ["API_KEY"]).configure(config) # computer vision inference server client 
if not firebase_admin._apps: # if the Firebase app has not been initialized yet
        firebase_admin.initialize_app() # initialize app with credentials
db = firestore.client() # database from which to pull parking data

while True: # Repeat forever

    now = datetime.now() # the time when the image is taken 
    hour = now.hour # the hour of the timestamp
    now_utc = datetime.now(timezone.utc) # the time in UTC for Firestore timestamp

    print(now.strftime("%Y-%m-%d_%H-%M-%S")) # print timestamp to the console

    if 7 <= hour < 19: # only run between 7am and 7pm
        try:
            subprocess.run(["rpicam-still", "-n", "-o", image]) # take picture and save to specified path
            results = client.infer(image, model_id="parking-tracker-training-data-2y5xf/2") # process the image with the computer vision model
            count = len(results["predictions"]) # count the cars in the image 
            data = {"time": now_utc, "occupied": count} # data to be sent to Firestore
            doc_ref = db.collection("Lot 12").document("Totals") # reference to the Firestore document where the data will be stored
            doc_ref.set(data) # send data to Firestore
            print("Success") # if everything is successful, print success to the console
        except Exception as e:
            print(f"Error: {e}") # if there is an error, print it to the console

    time.sleep(15) # wait for 15 seconds 
