# pylightrequests
A super-fast HTTP Client made in Python, using sockets

## Note

- 14x faster than `requests`
- Easy to use (real)

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

http = HTTP('example.com')

# GET REQUEST


# with params
http.get_req('/', {'q': 'search'})

# without params
http.get_req('/')

# POST REQUEST

# with params
http.post_req('/', {'q': 'search'})

# without params
http.post_req('/')

# PUT REQUEST

# with params
http.put_req('/', {'q': 'search'})

# without params
http.put_req('/')

# REQUEST
http.request('GET', '/')
```



## Author
<a name="author"></a>

* **Pneb** - *Initial work* - [pneb](https://github.com/pneb)


## License
<a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
```
