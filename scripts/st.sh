#!/bin/bash
cat < /dev/stdin
echo "{'param1':'$1', 'param2':'$2'}"
echo "{'stdin works!':'ok'}"
