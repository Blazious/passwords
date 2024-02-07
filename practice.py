#1

list_1= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_2= ["0","1","2","3","4","5","6","7","8","9","@","#","$","%","&","^","*"]
thislist = list_1 + list_2

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 4
#2 This has been built on the previous code , the first code could only generate one password 
  import random
list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "@", "#", "$", "%", "&", "^", "*"]
thislist = list_1 + list_2
random.shuffle(thislist)
i = 0

while i < len(thislist):
    print(thislist[i], end="")
    i = i + 4  

#you can run this multiple times to generate multiple passwords at random






