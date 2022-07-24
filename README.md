# HomeAI
## Intro
Hello Judges, this is our submission for the coding category. You will not be able to run it as you require a specific AC(the only compatible device to hand). Thank you for taking the time to read our submission. The majority of commits are done by willeader, this does not represent to contributions because we used the VScode liveshare extension hosted on WILLEADER's device -who was the only one that pushed during the sessions to avoid problems.

## Setting up Home Assistant
Home Assistant was set up in the Core configuration for Linux [instructions here](https://www.home-assistant.io/installation/linux#install-home-assistant-core).

Next, a [Daikin AC was integrated](https://www.home-assistant.io/integrations/daikin/#climate). This allows us to control the AC from Home Assistant with commands such as off, heat, cool, etc.

Then, automations were set up. This allowed us to trigger webhooks to switch change the mode of the AC. A POST request can be sent to the webhook's URL to achieve this. Our Python script for the webisite makes use of these to control the AC with buttons, and the AI, of course, uses these to execute the commands it needs to execute. 

## Setting up the website
We set up a simple website using Flask to control the AC.

It has a home page where devices are listed. These can be clicked on to redirect you to their respective device pages. These pages have buttons to control the device.

## Data into the algorithm
For this hackathon, we have created a sample data generation script that creates one week's worth of sample data. This data is how we expect to format data coming from the user in the future. The sample data is fed into the algorithm to make the schedule. In the future, this will be done automatically. I.e. data will be collected as time passes. We have however, just for demonstration, have taken the first steps into data collection from Home Assistant. The data_collection.py script queries the needed data from the sqlite database Home Assistant created. However, it currently has limited funcitonality and collects data from one device only.

This data has information about devices, what action was performed (e.g. on/off), and the timestamp for when this happened.

## The algorithm
The algorithm uses a moving average to calculate what action should be performed every 5 minutes daily, based on a week's worth of historical data. It is a simple yet effective algorithm, and due to time constraints we could not make a full ML model. 

## Data out (controlling the devices)
The devices are controlled using a python script that is continuously running. It checks the time to see if any device states need to be changed right now based on the schedule given out by the algorithm.

## Controller
The controller.py can easily execute 1 function to create the schedule based on input data, start the website, and execute the schedule. Home Assistant currently is set up manually, but it is possible to dynamically generate scripts to feed into it. We can also set it up automatically. In the future, we also plan to integrate an easy to use UI into our website for adding devices and configuring settings.
