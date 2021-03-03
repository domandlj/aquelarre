cond1 = scripts/./cond1.sh
succes = scripts/./script.sh
home = scripts/./home.sh
st = scripts/./st.sh

get /?id&name :
    # succes.
        cond1 => succes, 201 
    # failure.
end

get / :
    # succes.
	cond1 => home, 200 
    # failure.
end

put /postear?id&wallet :
	cond1 => st, 200
end

