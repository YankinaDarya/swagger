# swagger_client.PostApi

All URIs are relative to *https://127.0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post**](PostApi.md#create_post) | **POST** /create | Add a new post to the blog
[**delete_post**](PostApi.md#delete_post) | **POST** /myPosts/{postId}/delete | Delete post
[**edit_post**](PostApi.md#edit_post) | **POST** /myPosts/{postId}/edit | Edit post
[**get_post_by_id**](PostApi.md#get_post_by_id) | **GET** /myPosts/{postId} | Get post by ID
[**get_posts**](PostApi.md#get_posts) | **GET** /myPosts | Get all posts


# **create_post**
> create_post(body)

Add a new post to the blog



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()
body = swagger_client.Post() # Post | Post object that needs to be added to the blog

try:
    # Add a new post to the blog
    api_instance.create_post(body)
except ApiException as e:
    print("Exception when calling PostApi->create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Post**](Post.md)| Post object that needs to be added to the blog | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_post**
> Post delete_post(post_id)

Delete post

Delete post

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()
post_id = 789 # int | ID of post to delete

try:
    # Delete post
    api_response = api_instance.delete_post(post_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**| ID of post to delete | 

### Return type

[**Post**](Post.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_post**
> Post edit_post(post_id, body)

Edit post

Edit post

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()
post_id = 789 # int | ID of post to edit
body = swagger_client.Post() # Post | Post object that needs to be added to the blog

try:
    # Edit post
    api_response = api_instance.edit_post(post_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->edit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**| ID of post to edit | 
 **body** | [**Post**](Post.md)| Post object that needs to be added to the blog | 

### Return type

[**Post**](Post.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_by_id**
> Post get_post_by_id(post_id)

Get post by ID

Returns a single post

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()
post_id = 789 # int | ID of post to return

try:
    # Get post by ID
    api_response = api_instance.get_post_by_id(post_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->get_post_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_id** | **int**| ID of post to return | 

### Return type

[**Post**](Post.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posts**
> FullPost get_posts()

Get all posts

Returns all posts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()

try:
    # Get all posts
    api_response = api_instance.get_posts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->get_posts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FullPost**](FullPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

