#!/usr/bin/env python3
import aquelarre as aque

aque.response("{'param1': '"+ aque.get_param(1) + "' , 'param2': '" + aque.get_param(2)+ "'}" )
aque.response(str(aque.get_json_payload()))
