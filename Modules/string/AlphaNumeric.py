def check_if_alpha_num(s):
    alpha=False
    dig=False
    for ch in s:
        if ch.isalpha() :
            alpha = True
        if ch.isdigit():
            dig = True
    if alpha and dig:
        print(f"{s} is Alpha Numeric")
    else: print(f"{s} Not an Alphanumeric")


s='abLion$124c'
check_if_alpha_num(s)