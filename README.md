Cisco-SDWAN-Basic-Rest-connection

The Cisco SD-WAN Solution, is a WAN Arquitecture for the digital transformation, it provide an easy/cost effective way to deploy, monitor and troubleshoot your WAN and WAN Devices. The solution have different major components and features, and one of those is the ability to beign managed via APIs.


SDWAN Basic Rest Connections

The main pourpose of this basic repository is show you how you can create your own basic script to configure and maintain your network via APIs. Here you will find a basic python file where yu will be able to understand how to make calls to your vManage.
The scripts do not have any particular functionality, you are the one who have to provide any API URL or payload that you want to check. You can find all the API documentation at your vManage in the url: https://vmanage_ip/apidocs

This script was mainly built to provide a basic understanding on how it works and interact APIs.

Requirements

- Python3
- User with the right permission in the vManage to configure via APIs

Recomendations

- You can check a few API calls in Postman or any similar software. There is a Postman collection already pre-built at https://documenter.getpostman.com/view/3224967/SVmpXhXd?version=latest
- Always try to create a virtual enviroment for your Python tests.


Using the Script

Setup
   1. Clone the script into your computer
   
        a. git clone https://github.com/ai-devnet/Getting-started-with-Cisco-SD-WAN-REST-APIs.git
        
        b. Move to the folder created
        
   2. Create a Virtual Enviroment 
                                
          python3.8 -m venv venv
          source venv/bin/activate
          
   3. Install the requests module
   
          pip install requests
          
   4. Setup the correct for your own vManage enviroment credentials in the document "credentials.py"
    
   5. open your python console and import "rest_connection" as sdwan
    
Executing your own calls
  Now you can create your own API calls, let's try a few examples:
   
   Get Example:
    To query a list of your devices, the api is "/dataservice/device". The full url should be https://vmanage_ip:port/dataservice/device. Inside the URL dataservice is referencinf directly to APIs, so basically we can resume the call just with 'device'. In your Python console you can type:
    
    sdwan.sdwan.get_request('device') --> You will receive the info with all the devices and now you will be able to format it.
    
   
   Post Example:
   To POST some info into the vManage, we need to provide a payload (Data) to be send. You can have a .json file in your directory or just have the json payload in your enviroment as a variable.
   To query the audit logs the api is "/dataservice/auditlog". The full url should be https://vmanage_ip:port/dataservice/auditlog. nside the URL dataservice is referencinf directly to APIs, so basically we can resume the call just with 'auditlog'. One last step is required, payload, we can use this as an example
   
    {
    "query": {
    "condition": "AND",
    "rules": [
      {
        "value": [
          "1"
        ],
        "field": "entry_time",
        "type": "date",
        "operator": "last_n_hours"
      }
    ]
     },
    "size": 10
    }
    
   You can create a variable in your enviroment with that payload assigning it a variable, for example variable name "payload"
   In your Python console you can type:
    
    sdwan.sdwan.post_request('auditlog', payload) --> You will receive the info with all the last 10 audit logs in the last hour and now you will be able to format the info.

 
 
