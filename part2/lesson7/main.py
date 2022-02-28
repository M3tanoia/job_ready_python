#Create a list of names as long as user enters Y to continue and until 5 names are reached
names = []
uContinue = ""
count = 0
 
while count < 5 and uContinue != "N":
  name = input("What's your name? ")
  print("You entered: "+name)
  count += 1
  names.append(name)
  uContinue = input("Continue (Y or N) ")
 
print(names)

print("--------------------------------------------------")

#print numbers while i is less than 10
i = 0
while ((i < 10) == True):
    print(i)
    i = i + 1

print("-------------------------------------------------")

message = "Hello, World!"
 
print(message)
print(len(message))
 
# extract the substring from message starting from the first character (index 0) 
# through the character whose index value is 4. 
message_1 = message[0:5]
 
print("message_1 is " + message_1) 
 
# Extract the substring from message starting from the first character (index 0)
# through the character whose index value is 4. The lower bound is not specified,
# so Python uses 0. 
message_2 = message[:5]
 
print("message_2 is " + message_2)
 
# Extract the substring from message starting from the eighth character (index 7)
# through the character whose index value is 9 (one less than 10)..
message_3 = message[7:10]
 
print("message_3 is " + message_3)
 
# Extract the substring from message starting from the eighth character (index 7)
# through the last character. Index 14 is past the end of the string.
message_4 = message[7:14]
 
print("message_4 is " + message_4)
 
# Extract the substring from message starting from the eighth character (index 7)
# all the way to the last character, regardless of index value.
message_5 = message[7:]
 
print("message_5 is " + message_5)