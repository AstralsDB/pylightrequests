# pylightrequests
A super-fast HTTP Client made in Python, using sockets


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

Lightt = HTTP()

data = Lightt.get_req("example.com", "/vuln.html")
print(data.decode('utf-8'))

data = Lightt.post_req("example.com", "/vuln.html", 'action=check&username=admin')
print(data.decode('utf-8'))

data = Lightt.request("get", "example.com", "/vuln.html")
print(data.decode('utf-8'))

data = Lightt.request("post", "example.com", "/vuln.html", 'action=check&username=admin')
print(data.decode('utf-8'))

data = Lightt.request_multiprocess("put", "example.com", "/vuln.html", "action=check&username=admin", process_count=1000)
for resp in data:
    print(resp.get().decode('utf-8'))
```



## Author
<a name="author"></a>

* **Pneb** - *Initial work* - [pneb](https://github.com/pneb)


## License
<a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
```
