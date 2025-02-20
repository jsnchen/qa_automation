import requests

def send_api_request(method, url, headers=None, payload=None, auth=None, allow_redirects=True):
    """
    Sends an API request and returns the response.
    
    :param method: HTTP method (GET, POST, etc.)
    :param url: API endpoint
    :param headers: Request headers (default: None)
    :param payload: Request payload (default: None)
    :param auth: Optional authentication tuple (username, password)
    :return: Response object
    """
    print(f"method={method}, allow_redirects={allow_redirects}")

    method = method.upper()
    if method == "GET":
        response = requests.get(url, headers=headers, auth=auth, allow_redirects=allow_redirects)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=payload, auth=auth, allow_redirects=allow_redirects)
    elif method == "PUT":
        response = requests.put(url, headers=headers, json=payload, auth=auth, allow_redirects=allow_redirects)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers, auth=auth, allow_redirects=allow_redirects)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    
    return response
