from aquelarre_syntax import *
import subprocess


def scripts_table(code: Code) -> dict:
    result:dict = {}
    
    for elem in code:
        if type(elem) == ScriptDeclaration:
            result[elem.script_name.replace(' ', '')] = elem.script.replace(' ', '')
    
    return result


def run_script(name:str,stdin=None) -> str:
    result = subprocess.check_output(name,input=stdin, shell = True)
    result = result.decode()
    result.replace('\n','')
    return str(result)


def run_cond(code: Code, cond: Cond, args: List[str],stdin=None) -> str:
    args_ = ' '.join(args)
    scripts_table_ = scripts_table(code)
    if_script = scripts_table_[cond.if_script] + ' ' + args_
    then_script = scripts_table_[cond.then_script] + ' ' + args_ 
    
    # print(run_script(if_script,stdin))
    
    if 'true' in run_script(if_script,stdin):
        return run_script(then_script,stdin)
    else:
        return 'false'

def get_params_or_args(path,option) -> List[str]:
    result = []
    mode = 0
    
    if option == 'params':
        mode = 0
    if option == 'args':
        mode = 1

    if '?' in path:
        params = path.split('?')
        params = params[1]
        params = params.split('&')
        for pair in params:
            result.append(pair.split('=')[mode])
    return result

def get_fun(method,url, code) -> Fun:
    args = get_params_or_args(url,'args')

    funs = list(filter(lambda elm:
        type(elm) == Fun, code))

    result = list(filter(lambda fun:
        fun.method == method and 
        fun.eval_params(args) == url, funs))

    if result == []:
        raise Exception('URL and method match not found!')
    return result[0]

