""" 
Add a shebang line to define where the interpreter is located. In this case, the shebang line would be /usr/bin/env python3.

Se copió correctamente
Import the request module into the file using the import statements.

import requests
Se copió correctamente
To check whether the local host is correctly configured, we use the socket module.

Now, import the socket module.

import socket
Se copió correctamente
Next, write a function check_localhost, which checks whether the local host is correctly configured. We do this by calling the gethostbyname within the function.

localhost = socket.gethostbyname('localhost')
Se copió correctamente
The above function translates a host name to IPv4 address format. Pass the parameter localhost to the function gethostbyname. The result for this function should be 127.0.0.1.

Edit the function check_localhost so that it returns true if the function returns 127.0.0.1.

Now, we will write another function called check_connectivity. This checks whether the computer can make successful calls to the internet.

A request is when you ping a website for information. The Requests library is designed for this task. You will use the request module for this, and call the GET method by passing http://www.google.com as the parameter.

request = requests.get("http://www.google.com")
Se copió correctamente
This returns the website's status code. This status code is an integer value. Now, assign the result to a response variable and check the status_code attribute of that variable. It should return 200.

Edit the function check_connectivity so that it returns true if the function returns 200 status_code.

"""

#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    local_host = socket.gethostbyname('localhost')
    if local_host == "127.0.0.1":
        return True
    
def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request.status_code
    if response == 200:
        return True

if __name__ == "__main__":
    print(check_localhost())
    print(check_connectivity())
    

    




