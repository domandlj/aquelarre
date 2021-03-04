#!/bin/bash


# We run aquelarre with the test script in the background for 10s.
timeout 10s aquelarre code.re & 

# Wait 2 secs for the sv to start...
sleep 2

# GET 
# Succes tests:
curl -X GET -H 'Content-Type: application/json' 'localhost:8080/'

# POST

# PATCH

# PUT
curl -X PUT -H "Content-Type: application/json" -d '{"name": "juan", "email": "juan@gmail.com"}' 'localhost:8080/postear?id=1&wallet=bity'

# DELETE
