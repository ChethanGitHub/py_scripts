def check_symetrical(s):
    piv = len(s) // 2
    first = s[:piv]
    second = s[piv:]
    if first == second: print(f"{s} Symetrical")
    else:  print('Non Symetrical')

def check_polyndrome(s):
    reverse_str = s[::-1]
    if s == reverse_str:
        print(f"{s} is polyndrome")
    else: print(f"{s} not polybdrome")

s = 'abaaba'
check_symetrical(s)
check_polyndrome(s)