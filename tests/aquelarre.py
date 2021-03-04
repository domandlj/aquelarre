import sys

def get_parm(param_number):
    return sys.argv[param_number]

def get_json_payload():
    body = sys.stdin.read()
    body=body.replace('\n','')
    return body
