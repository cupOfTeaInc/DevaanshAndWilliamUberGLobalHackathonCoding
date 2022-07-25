# HomeAI
## Intro
Hello Judges, this is our submission for the coding category. You will not be able to run it as you require a specific AC(the only compatible device to hand). Thank you for taking the time to read our submission. The majority of commits are done by willeader; this does not represent the contributions because we used the VScode liveshare extension hosted on WILLEADER's device - who was the only one that pushed during the sessions to avoid problems.

## Collaboration
Some tolls we used to work together remotel were: 
- Github was very useful for version control and we could easily share code using git push and git pull.
- The LiveShare extension on VS Code was really helpful as we could work on code together. We used this quite a lot, so that only one person needs to push to the GitHub repo to update everything.
- Discord was used for video calling

## Setting up Home Assistant
Home Assistant was set up in the Core configuration for Linux [instructions here](https://www.home-assistant.io/installation/linux#install-home-assistant-core).

Next, a [Daikin AC was integrated](https://www.home-assistant.io/integrations/daikin/#climate). This allows us to control the AC from Home Assistant with commands such as off, heat, cool, etc.

Then, automations were set up. This allowed us to trigger webhooks to change the mode of the AC. A POST request can be sent to the webhook's URL to achieve this. Our Python script for the website makes use of these to control the AC with buttons, and the AI, of course, uses these to execute the commands it needs to execute. 

## Setting up the website
We set up a simple website using Flask to control the AC.

It has a home page where devices are listed. These can be clicked on to redirect you to their respective device pages. These pages have buttons to control the device. The device pages are dynamically generated so that if a new device is added, a new webpage is created with the respective control buttons.

On the testing branch, we have added a button to begin the controller.py program to start HomeAI. However, this has not been fully tested. 

## Data into the algorithm
For this hackathon, we have created a sample data generation script that creates one week's worth of sample data. This data is how we expect to format data coming from the user in the future. The sample data is fed into the algorithm to make the schedule. In the future, this will be done automatically. I.e. data will be collected as time passes. We have however, just for demonstration, taken the first steps into data collection from Home Assistant. The data_collection.py script queries the needed data from the sqlite database Home Assistant created. However, it currently has limited funcitonality and collects data from one device only.

This data has information about devices, what action was performed (e.g. on/off), and the timestamp for when this happened.

## The algorithm
The algorithm uses a moving average to calculate what action should be performed every 5 minutes daily, based on a week's worth of historical data. It is a simple yet effective algorithm, and due to time constraints we could not make a full ML model. 

In the video, when talking about the line, we are talking about the line that can be seen on a graph, with the x-axis as the time elapsed, and the y-axis as the state of the device (between 0 and 1). First, the data that comes from the database is translated to numerical data. the timestamp is already converted into 5 minute increments, but the 'On' and 'Off' values are translated to 1's and 0's respectively. After averaging, we get many intermediary values which are not suitable for use, so we round them to the nearest whole number. This then gives us the schedule.

## Data out (controlling the devices)
The devices are controlled using a python script that is continuously running. It checks the time to see if any device states need to be changed right now based on the schedule given out by the algorithm. E.g. if the time right now is 5 minutes after the last update, it triggers the webhook to perform the next action. However, you may notice in the timelapse in the video that the loogbook is updating around every 2-3 minutes. This is because async.sleep() is passed 2.5 minutes as the refresh rate, so it repeats the action.

## Controller
The controller.py can easily execute 1 function to create the schedule based on input data, start the website, and execute the schedule. Home Assistant currently is set up manually, but it is possible to dynamically generate scripts to feed into it for devices. We can also set it up automatically. In the future, we also plan to integrate an easy to use UI into our website for adding devices and configuring settings.
