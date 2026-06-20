# class Vaults:
#     def __init__(self,galleons=0 ,sickles=0 ,knuts=0):
#         self.galleons=galleons
#         self.sickles=sickles
#         self.knuts=knuts
        
#     def __str__(self):
#         return f"{self.galleons} galleons , {self.sickles} sickles ,{self.knuts} knuts"
# potter=Vaults(100,45,23)
# print(potter)
# weasly=Vaults(1000,457,23)
# print(weasly)

# now we can combine these vaults
# galleons=potter.galleons+weasly.galleons
# sickles=potter.sickles+weasly.sickles
# knuts=potter.knuts+weasly.knuts
# total=(galleons+sickles+knuts)
# print(total)


# this method is a manual method we can do this  in pythonic way using oprator overloading 

# class Vaults:
#     def __init__(self,galleons=0 ,sickles=0 ,knuts=0):
#         self.galleons=galleons
#         self.sickles=sickles
#         self.knuts=knuts
        
#     def __str__(self):
#         return f"{self.galleons} galleons , {self.sickles} sickles ,{self.knuts} knuts"
#     def __add__(self, other):
#         galleons=self.galleons + other.galleons
#         sickles=self.sickles + other.sickles
#         knuts=self.knuts + other.knuts
#         return Vaults(galleons,sickles,knuts)
# potter=Vaults(100,45,23)
# print(potter)
# weasly=Vaults(1000,457,23)
# print(weasly)
# total=potter+weasly
# print(total)




