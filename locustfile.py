import time
from locust import HttpUser, task, between
import random 
import json


# class for load handling
class AppUser(HttpUser):

    wait_time = between(1, 5)

    #for index page
    @task
    def index_page(self):
        self.client.get("/")
        
    #for classification page
    @task
    def classification_page(self):
        texts = "My name is Priyanka"
        myheaders = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.client.post("/output", data= json.dumps(texts), headers=myheaders)

        

    