### :heavy_check_mark: Solution
> [:point_right: 2-measure_runtime.py](2-measure_runtime.py)
> [:point_right: api/v1/app.py](api/v1/app.py), [:point_right: api/v1/views/index.py](api/v1/views/index.py)

## [3. Auth class](api/v1/auth)
### :page_with_curl: Task requirements.
Now you will create a class to manage the API authentication.

*    Create a folder api/v1/auth
*     Create an empty file api/v1/auth/__init__.py
*     Create the class Auth:
    *     in the file api/v1/auth/auth.py
    *     import request from flask
    *     class name Auth
    *     public method def require_auth(self, path: str, excluded_paths: List[str]) -> bool: that returns False - path and excluded_paths will be used later, now, you don’t need to take care of them
    *     public method def authorization_header(self, request=None) -> str: that returns None - request will be the Flask request object
    *     public method def current_user(self, request=None) -> TypeVar('User'): that returns None - request will be the Flask request object

This class is the template for all authentication system you will implement.
```
bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth
a = Auth()
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.authorization_header())
print(a.current_user())
bob@dylan:~$ 
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
bob@dylan:~$
```

### :wrench: Task setup.
```bash
# Directory and files setup.
mkdir -p api/v1/auth
touch api/v1/auth/__init__.py
touch api/v1/auth/auth.py

# Tests
touch main_0.py
chmod +x main_0.py

pycodestyle api/v1/auth/auth.py

# Start server.
API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/auth](api/v1/auth), [:point_right: api/v1/auth/__init__.py](api/v1/auth/__init__.py), [:point_right: api/v1/auth/auth.py](api/v1/auth/auth.py)
# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;
