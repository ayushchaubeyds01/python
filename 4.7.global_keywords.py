def sum(a,b):
    print("hello")
    global z # global keyword modifies the global variable value replaceed by local variable
    z=0
    return a+b
z=3   # replaced by local variable
print(sum(3,6))
print(z)
