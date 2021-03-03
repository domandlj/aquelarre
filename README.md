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

3. And that's it. You can now run your own aquelare .re scripts like
```
aquelarre script.re
```

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

