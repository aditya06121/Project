w = int(input("Weight: "))
wt = input("(L)bs or (K)g: ")
if wt.upper() == 'L':
    wl = w * 0.45
    print(f'You are {wl} Kilos')
else:
    wk = w / 0.45
    print(f'You are {wk} Pounds')