from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi(swagger_client.ApiClient(configuration))
body = swagger_client.Post() # Post | Post object that needs to be added to the blog

try:
    # Add a new post to the blog
    api_instance.create_post(body)
except ApiException as e:
    print("Exception when calling PostApi->create_post: %s\n" % e)