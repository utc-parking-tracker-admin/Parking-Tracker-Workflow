# Parking-Tracker-Workflow
The code that runs on the Parking Tracker Raspberry Pi.

Create a service file:
sudo nano /etc/systemd/system/parking_tracker_workflow.service

```
[Unit]
Description=Parking Tracker Script
After=network.target

[Service]
ExecStart=/home/utcparking/python_projects/parkingtracker/env/bin/python /home/utcparking/python_projects/parkingtracker/parking_tracker_workflow.py
WorkingDirectory=/home/utcparking/python_projects/parkingtracker
Restart=always
User=utcparking

[Install]
WantedBy=multi-user.target

```

Then run:
* sudo systemctl daemon-reexec
* sudo systemctl daemon-reload
* sudo systemctl enable parking_tracker_workflow.service
* sudo systemctl start parking_tracker_workflow.service
* sudo systemctl status parking_tracker_workflow.service

To stop the service:
sudo systemctl stop parking_tracker_workflow.service

Note: include any environment variables in [Service] section.
