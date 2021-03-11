from typing import Any, List, Union
import re

""" 1. Abstract Syntax Tree Types."""
Method = str 
methods = ['get','post','put','delete', 'patch']
ScriptName = str 
URL = str 
Status = int 

def balanced(exp: str, left: str, right: str) -> bool:
    stack : List[str] = []
    for c in exp:
        if c == left:
            stack.append(left)
        if c == right:
            if stack == []:
                return False
            stack.pop()


    return stack == []

class ScriptDeclaration:
    def __init__(self, 
            script_name: ScriptName, 
            script: str):

        self.script_name = script_name
        self.script = script

class Cond:
    def __init__(self,
            neg: bool,
            if_script: ScriptName, 
            then_script: ScriptName, 
            status: Status):

        self.neg = neg
        self.if_script = if_script
        self.then_script = then_script
        self.status = status

class Fun:
    def __init__(self, 
            method : Method, 
            url: URL,
            body : List[Union[Cond]]):
        self.method = method
        self.url = url
        self.body = body

    def get_params(self) -> List[str]:
        result = []
        if '?' in self.url:
            params = self.url.split('?')
            params = params[1]
            result = params.split('&')

        return result

    def eval_params(self, args: List[str])-> URL:
        result = self.url
        if self.get_params() == [] or args == []:
            return self.url

        count = 0
        for param in self.get_params():
            result = result.replace(param,param + '=' + args[count])
            count += 1
        return result
            





Code = List[Union[ScriptDeclaration, Cond,Fun]]




""" 2. Tokenization"""
def is_scipt_declaration(line: str) -> bool:
    if len(line.split('=')) == 2 and '=>' not in line:
        return True
    else:
        return False

def is_comment(line: str) -> bool:
    if '#' in line:
        return True
    else:
        return False

def is_cond(line: str) -> bool:
    if ('=>' in line and ',' in line):
        return True
    else:
        return False

def is_fun(line: str) -> bool:
    tokens = line.split()
    if (len(tokens) >= 3 and 
            tokens[2] == ':'):
        if tokens[0] in methods:
            return True
        else:
            raise Exception('BadSyntax: ' + tokens[0] + ' not a valid HTTP method.')
    else:
        return False

def is_end(line: str) -> bool:
    return ('end' in line and len(line.split())==1)

def valid_token(line: str):
    return (line == '\n'
            or is_scipt_declaration(line)
            or is_comment(line)
            or is_fun(line)
            or is_cond(line)
            or is_end(line))
Token = str
FunToken = List[Union[str, List[Token]]]

def tokenize(lines:list) -> List[Union[Token, FunToken]]:
    tokens = []
    fun_tokens = []
    fun_body = []

    fun_open = False
    
    line_count = 0
    for line in lines:
        line_count += 1

        assert valid_token(line), 'BadSyntax: ' + 'line ' + str(line_count) +', ' + line
        if is_scipt_declaration(line):
            if fun_open:
                raise Exception('BadSyntax: script declaration inside HTTP method.')
            
            # print('script declaration => ' +line)
            tokens.append(line.replace('\n',''))

        if is_comment(line):
            # print("type: comment => " +line)
            pass

        if is_fun(line):
            if fun_open:
                raise Exception('BadSyntax: HTTP method inside HTTP mehtod.')

            fun_open = True
            # print('type: fun =>' + line)
            fun_tokens.append(line.replace('\n',''))

        if is_cond(line):
            # print('type: cond => ' + line)
            if fun_open:
                fun_body.append(line.replace('\n',''))
                        
        if is_end(line):
            fun_open = False
            fun_tokens.append(fun_body)
            tokens.append(fun_tokens)
            fun_tokens = []
            fun_body = []
    
    if fun_open:
        raise Exception('BadSyntax: HTTP method unclosed!')

    #print(str(tokens))
    return tokens

""" 3. Parsing"""
def parse_script_declaration(token: Token) -> ScriptDeclaration:
    tokens = token.split('=')
    return ScriptDeclaration(tokens[0], tokens[1])


def parse_cond(token: Token) -> Cond:
    token_clean = token.replace('\t','')
    neg_active = False

    if 'not' in token:
        neg_active = True
        token_clean = token_clean.replace('not','', 1)    
    
    tokens = re.split('=>|,',token_clean)

        
    return Cond(
            neg = neg_active ,
            if_script = tokens[0].replace(' ', ''), 
            then_script = tokens[1].replace(' ', ''),
            status = int(tokens[2]))



def parse_fun(token: FunToken) -> Fun:
    fun_declaration = token[0].split()
    method = fun_declaration[0]
    url = fun_declaration[1]

    fun_body = token[1]
    body = []

    for line in fun_body:
        if is_comment(line):
            pass 

        if is_cond(line):
            body.append(parse_cond(line))
    
    return Fun(method, url, body)

def parse(tokens) -> Code:
    code = []
    for token in tokens:
        if type(token) == Token:
            if is_scipt_declaration(token):
                code.append(parse_script_declaration(token))
            
            if is_cond(token):
                code.append(parse_cond(token))

        if type(token) == list:
            code.append(parse_fun(token))
    return code

def parse_script_from_io(name):
    file1 = open(name, 'r')
    lines = file1.readlines()
    tokens = tokenize(lines)
    return parse(tokens)
