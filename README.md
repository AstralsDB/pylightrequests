# pylightrequests
A super-fast HTTP Client made in Python, using sockets

## Note

- 14x faster than `requests`
- Easy to use (real)
![](https://cdn.discordapp.com/attachments/1023585021606498358/1037267841839288351/Screenshot_20221102-1530492.png)

## Table of Contents
<a name="table-of-contents"></a>
* [Installation](#installation)
* [Example](#example)
* [Author](#author)
* [License](#license)

## Installation
<a name="installation"></a>

To install pylightrequests, simply use pip:

```
$ pip install git+https://github.com/pneb/pylightrequests
```
(you may need to run `pip` with root permission: `sudo pip install pylightrequests`)

Then import the package:
```python
from pylightrequests import *
```

## Example
<a name="example"></a>

```python
from pylightrequests import *

http = HTTP()

# Get request
print(http.get_req('google.com', '/'))


# Post request
print(http.post_req('google.com', '/', 'Hello World!'))


# Put request
print(http.put_req('google.com', '/', 'Hello World!'))


# Request (method is up to you)
print(http.request('get', 'google.com', '/'))


# Request (multiprocess)
print(http.request_multiprocess('get', 'google.com', '/'))

# Parse data
print(http.parse_data(http.request('get', 'google.com', '/')))

# Get response code
print(http.get_response_code())

# Get status
print(http.get_status())

# Get header
print(http.get_header())

# Get json
print(http.get_json())

# Get json data
print(http.get_json_data())

# Get data
print(http.get_data())
```



## Author
<a name="author"></a>

* **Pneb** - *Initial work* - [pneb](https://github.com/pneb)


## License
<a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
```
