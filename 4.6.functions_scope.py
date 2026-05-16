def sum(a,b): #here a and b are local variable 
    c=a+b
    z=8       #here z is a local  variable
    return c   #local variables are destroyed and can't be accesed after the function returns its value 

z=0 #here z is a global variable because it lies  outside of the loop and can be used anywhere
print(sum(4,6))