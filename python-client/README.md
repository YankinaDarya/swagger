# swagger-client
Posts blog

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
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

```

## Documentation for API Endpoints

All URIs are relative to *https://127.0.0.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PostApi* | [**create_post**](docs/PostApi.md#create_post) | **POST** /create | Add a new post to the blog
*PostApi* | [**delete_post**](docs/PostApi.md#delete_post) | **POST** /myPosts/{postId}/delete | Delete post
*PostApi* | [**edit_post**](docs/PostApi.md#edit_post) | **POST** /myPosts/{postId}/edit | Edit post
*PostApi* | [**get_post_by_id**](docs/PostApi.md#get_post_by_id) | **GET** /myPosts/{postId} | Get post by ID
*PostApi* | [**get_posts**](docs/PostApi.md#get_posts) | **GET** /myPosts | Get all posts


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [FullPost](docs/FullPost.md)
 - [Post](docs/Post.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



