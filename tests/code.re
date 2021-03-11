#!/usr/local/bin/aquelarre

cond1 = scripts/cond1.sh
cond2 = scripts/cond2.sh
succes = scripts/script.sh
home = scripts/home.sh
st = scripts/st.py

get /?id&name :
    # succes.
        cond2 => succes, 201 
    # failure.
end

get / :
    # succes.
	not cond1 => home, 200 
    # failure.
end

put /postear?id&wallet :
	cond2 => st, 200
end

