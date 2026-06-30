# Find the longest word in a sentence.
s=input("enter s:").strip()
words=(s.split())
max_word=(words[0])
for word in words :
  length=(len(word))
  if length>len(max_word):
    max_word=word
print(max_word)
print(len(max_word))