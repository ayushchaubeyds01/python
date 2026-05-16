for u in range(1,11):
    print(u)
    if u==5:
        break  #exit the loop completely
for v in range(1,11):
    print(v)
    if v==5:
        continue  #skip the current iteration and continue with the next
    
    
    for w in range(1,11):
        if w%2==0:
            pass  #syntax placeholder, does nothing
        print(w)