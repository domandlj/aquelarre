# Testing the Lexer.
# Testing boolean functions.
test_set_scripts_succes = []
test_set_scripts_fail = []


def test_boolean(fun,succes_set, fail_set):
    succes_count = 0
    fail_count = 0
    for token in succes_set:
        if fun(token):
            succes_count += 1
    for token in fail_set:
        if not fun(token):
            fail_count += 1
    return (succes_count/len(succes_set), fail_count/len(fail_set))



