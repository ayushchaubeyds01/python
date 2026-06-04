#random.choices
# from random import choice
# coin=choice(['head','tails'])
# print(coin)



# #random.randint(a,b)
# from random import randint
# number=randint(1,10)
# print(number)



# #random.shuffle(x)
# from random import shuffle
# cards=["jack","queen","kings"]
# shuffle(cards)
# for card in cards:
#     print(card)



# #statistics
# import statistics
# print(statistics.mean([100,95,245]))








#################### sys
# import sys
# # print("hello my name is",sys.argv[1])

# # if len(sys.argv)<2:
# #     print("too few arguements")
# # elif(len(sys.argv))>2:
# #     print("too many arguements")
# # else:
# #     print("my name is ",sys.argv[1])



# import random
# coin=random.choice(["heads","tails"])
# print((coin))


# from random import choice
# coin=choice(["heads","tails"])
# print(coin)



# from random import randint
# number=randint(1,10)
# print(number)


# from random import shuffle
# cards=(["king","queen","jack"])
# shuffle(cards)
# for card in cards:
#     print(card)


# import statistics
# print(statistics.mean([100,90]))


import sys
# print("my name is ",sys.argv[1])
# print("my name is ",sys.argv[0])
# if len(sys.argv)>2:
#     print("many arguements")
# elif(len(sys.argv)<2):
#     print("a few arguements")
# else:
#     print("my name is ",sys.srgv[1])


# try:
#     print("my name is",sys.argv[1])
# # except:
#     print("few arguements")




############sys.exit
# import sys
# if len(sys.argv)>2:
#     print("many arguements")
# elif(len(sys.argv)<2):
#     print("a few arguements")

# print("my name is ",sys.argv[1])    ## there will be an index error 


#then using sys.exit
# import sys
# if len(sys.argv)>2:
#     sys.exit("many arguements")
# elif(len(sys.argv)<2):
#     sys.exit("a few arguements")

# print("my name is ",sys.argv[1])


#now we can use it for multiple inputs not just a single string input 
# import sys 
# if len(sys.argv)<2:
#     sys.exit("too few arguements")
# for arg in sys.argv[1:]:    #it is a list slicing method to itrate over a list from settnig starting point and end point
#     print("my name is ",arg)


