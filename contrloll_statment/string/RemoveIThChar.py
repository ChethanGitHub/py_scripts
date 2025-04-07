def remove_char(s):
    new_str=''
    for c in s:
        if c not in 'HE':
            new_str += c
    print(new_str)

def better_function(s):
    r = "".join([c for c in s if c not in 'H'])
    print(r)

s = 'Hello World'
remove_char(s)
better_function(s)