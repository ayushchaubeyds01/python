
for i in range (1,101):
    if i<=1:
        is_prime=False
    else:
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        else:
            print(i,"prime")