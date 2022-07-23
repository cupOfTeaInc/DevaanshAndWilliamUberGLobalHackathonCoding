# HomeAI
## Setting up Home Assistant
Home Assistant was set up in the Core configuration for Linux [instructions here](https://www.home-assistant.io/installation/linux#install-home-assistant-core).

Next, a [Daikin AC was integrated](https://www.home-assistant.io/integrations/daikin/#climate). This allows us to control the AC from Home Assistant with commands such as off, heat, cool, etc.

Then, automations were set up. This allowed us to trigger webhooks to switch change the mode of the AC. A POST request can be sent to the webhook's URL to achieve this. Our Python script for the webisite makes use of these to control the AC with buttons, and the AI, of course, uses these to execute the commands it needs to execute. 
