# Parking-Tracker-Workflow
The code that runs on the Parking Tracker Raspberry Pi.

**Pre-requisites:**
* Ensure proper set up of Roboflow inference server, Firestore database, and Streamlit web application
* parking_tracker_workflow.py should be stored within /home/utcparking/python_projects/parkingtracker/
* Ensure the service account key file from Firestore is located within /home/utcparking/python_projects/parkingtracker/
* Install requirements.txt:
```
cd /home/utcparking/python_projects/parkingtracker
source env/bin/activate
pip install -r requirements.txt
```

**Steps to run the workflow automatically:**
1. Create a service file:
```
sudo nano /etc/systemd/system/parking_tracker_workflow.service
```
2. Paste the following into the nano editor:
```
[Unit]
Description=Parking Tracker Script
After=network.target

[Service]
ExecStart=/home/utcparking/python_projects/parkingtracker/env/bin/python /home/utcparking/python_projects/parkingtracker/parking_tracker_workflow.py
WorkingDirectory=/home/utcparking/python_projects/parkingtracker
Restart=always
User=utcparking
Environment=API_KEY=[api_key_value]
Environment=GOOGLE_APPLICATION_CREDENTIALS=/home/utcparking/python_projects/parkingtracker/utc-parking-tracker-firebase-adminsdk-fbsvc-f20ff2b1aa.json

[Install]
WantedBy=multi-user.target

```
Note: `[api_key_value]` should be replaced by the API key from Roboflow.

3. Save (Ctrl+O) and exit (Ctrl + X)
4. Run the following commands:
```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable parking_tracker_workflow.service
sudo systemctl start parking_tracker_workflow.service
sudo systemctl status parking_tracker_workflow.service
```

**To stop the service:**

Run the following command:
```
sudo systemctl stop parking_tracker_workflow.service
```


