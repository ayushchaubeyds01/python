
#   print("it is palindrome")
# else:
#   print(" it is not a palindrome")





#count vowels
# s=input("enter string:")
# count=0
# for ch in s:
#   if ch in "aeiou":
#     count+=1
# print(count)


#count consonents
s=input("enter string:")
count=0
for ch in s:
  if ch not in "aeiou":
    count+=1
print(ch,count)