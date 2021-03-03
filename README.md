[![Generic badge](https://img.shields.io/badge/Progress-Early%20Development-Orange.svg)](https://shields.io/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-bash](https://img.shields.io/badge/Made%20with-Bash-1f425f.svg)](https://www.gnu.org/software/bash/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Aquelarre.

Aquelarre is a DSL for making minimalistic web apps. It's more minimalistic 
than similiar software beacuse:

* Only implements: GET, POST, PUT, PATCH and DELETE HTTP methods.
* Each request is proccesed by a custom script (of any language), it's 
parameters are passed as script parameters and it's body JSON payload as stdin.
* Responses are in JSON format only, must be the stdout of a script.

## Installing.
1. Clone the repo and go to it: 
```
git clone https://github.com/domandlj/aquelarre.git 
```
2. Run the installer (only works with MAC OS, Linux and Termux.).
```
chmod +x install.sh
sudo ./install.sh
``` 

3. And that's it, you can now run your own aquelare .re scripts like
```
aquelarre script.re
```
and you can now remove the github repositorie. 

4. You can run again the install script to remove Aquelarre. 

## Syntax example.
script.re
```ruby
exists_worker = ./is_is_worker.py
get_worker = ./get_worker.py
anything = ./anything.sh
not_exists_worker = ./not_exists_worker.py
fail = ./fail.py
create_worker = ./create_worker.py

get / : 
     anything => home, 200 
end

get /?id&name :
    # succes.
        exists_worker => get_worker, 201 
    # failure.
	not_exists_worker => fail, 400
end

post
	not_exists_worker => create_worker, 201
end
```
## License.
MIT license (© 2021 Juan Salvador Domandl).

