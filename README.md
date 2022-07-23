# HomeAI
## Setting up Home Assistant
Home Assistant was set up in the Core configuration for Linux [instructions here](https://www.home-assistant.io/installation/linux#install-home-assistant-core).

Next, a [Daikin AC was integrated](https://www.home-assistant.io/integrations/daikin/#climate). This allows us to control the AC from Home Assistant with commands such as off, heat, cool, etc.

Then, automations were set up. This allowed us to trigger webhooks to switch change the mode of the AC. A POST request can be sent to the webhook's URL to achieve this. Our Python script for the webisite makes use of these to control the AC with buttons, and the AI, of course, uses these to execute the commands it needs to execute. 

## Setting up the website
We set up a simple website using Flask to control the AC and to display the schedule.

It has a home page where devices are listed. These can be clicked on to redirect you to their respective device pages. These pages have buttons to control the device, and the current schedule for it.

## Data into the algorithm
For this hackathon, we have created a sample data file that is fed into the algorithm to make the schedule. In the future, this will be done automatically. I.e. data will be collected as time passes.

This data has information about devices, what action was performed (e.g. on/off), and the timestamp for when this happened.

## The algorithm
...

## Data out (controlling the devices)
The devices are controlled using a python script that is continuously running. It checks the time to see if any device states need to be changed right now based on the schedule given out by the algorithm.
