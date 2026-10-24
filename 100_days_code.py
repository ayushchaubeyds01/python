# # First character, last character, and length
# string=input("enter :")
# print(string[0])
# print(string[-1])
# print(len(string))




# Reverse a string
# s=input("enter :")
# print(s[::-1])





# # Check for a palindrome
# s=input("enter :").lower()
# if (s[::-1])==s:
#     print("it is palindrome")
# else:
#     print("not a palindrome")






# # Count the vowels in a string
# count=0
# s=input("enter :").lower()
# for i in s:
#     if i in "aeiou":
#         count+=1
# print(count)







# # Count words in a string
# count=0
# s=input("enter :").lower()
# b=s.split(" ")
# for word in b:
#     if word:
#         count+=1
# print(count)




# # Character frequency
# frq=0
# s=input("enter :").lower()
# word=input("enter char:").lower()
# for i in s:
#     if word==i:
#         frq+=1
# print(frq)



# # Remove spaces from a string
# s=input("enter :").lower()
# word=s.split()
# print("".join(word))




# # Toggle the case of each character
# s = input("Enter a string: ")
# table = str.maketrans(
#     "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
# print(s.translate(table))






# # Remove duplicate characters from a string while preserving their first-occurrence order.
# s=input("enter string:")
# e=""
# for ch in s :
#     if ch not in e :
#         e+=ch
# print(e)





# # Check whether two strings are anagrams.
# s=input("enter :").lower()
# s2=input("enter :").lower()
# if len(s)!=len(s2):
#     print("not anagram")
# else:
#     for u in s:
#         if s.count(u)!= s2.count(u):
#             print("not anagram")
#             break
#     else:
#       print("anagram")








# # First non-repeating character
# s=input("enter s:").lower()
# for ch in s:
#     if s.count(ch)==1:
#         print(ch)
#         break
#     else:
#         print("no repeating character")







# # Find the most frequent character
# s=input("enter s:")
# max_count=0
# frequent=""
# for i in s:
#     if s.count(i)>max_count:
#         max_count=s.count(i)
#         frequent=i
# if frequent:
#     print("most frequent=",i)
# else:
#     print("not frequent")




# Find the character with the second-highest frequency in a string.
