import json
import requests
from credentials import *

class rest_api:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)
    
    """Login and Session to the vManage """
    def login(self, vmanage_ip, username, password):
        #Basic Auth User/Pass to the vmanage#
        login_basic_auth = f'https://{vmanage_ip}:8443/j_security_check'
        #Token included in the header since 19.2#
        url_token = f'https://{vmanage_ip}:8443/dataservice/client/token'
        
        #Format data for vManage Login
        login_data = {'j_username' : username, 'j_password' : password}
        
        #Creating a session object to the vManage#
        s = requests.session()
        
        #With the Session Object created (s), Posting user/pass and getting Token#
        login_response = s.post(url=login_basic_auth, data=login_data, verify=False)
        login_token = s.get(url=url_token, verify=False)
            
        #Adding content from 'login_token' into the header as 'X-XSRF-TOKEN'
        s.headers['X-XSRF-TOKEN'] = login_token.content
        self.session[vmanage_ip] = s
              
    def get_request(self, mount_point):
        """GET request"""
        url = f"https://{self.vmanage_ip}:8443/dataservice/{mount_point}"
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = response.content
        return data
        
    def post_request(self, mount_point, payload, headers={'Content-Type': 'application/json'}):
        """POST Request
            Payload is the name of the payload file in the same directory
        """
        
        url = f"https://{self.vmanage_ip}:8443/dataservice/{mount_point}"
        payload = open(payload)
        payload = json.loads(payload.read())
        payload = json.dumps(payload)

        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        data = response.json()
        return data

sdwan = rest_api(cvmanage_ip, cusername, cpassword) 
    
