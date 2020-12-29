# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_users_post**](DefaultApi.md#create_user_users_post) | **POST** /users/ | Create User
[**delete_user_users_user_id_delete**](DefaultApi.md#delete_user_users_user_id_delete) | **DELETE** /users/{user_id} | Delete User
[**read_user_users_user_id_get**](DefaultApi.md#read_user_users_user_id_get) | **GET** /users/{user_id} | Read User


# **create_user_users_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_user_users_post(user_input)

Create User

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.user_input import UserInput
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_input = UserInput(
        name="name_example",
        email="email_example",
    ) # UserInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.create_user_users_post(user_input)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_user_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_input** | [**UserInput**](UserInput.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_users_user_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_user_users_user_id_delete(user_id)

Delete User

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_id = "user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete User
        api_response = api_instance.delete_user_users_user_id_delete(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_user_users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_user_users_user_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type read_user_users_user_id_get(user_id)

Read User

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_id = "user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Read User
        api_response = api_instance.read_user_users_user_id_get(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->read_user_users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

