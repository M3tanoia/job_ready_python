#Create a function that takes as input a variable number of keyword arguments using the following pattern:

word_1=value, word_2=value,…,word_n = value
#The function should return the word with the highest corresponding value, with the word and value in a tuple. Using the example data included in the following code, the result would be word_3 6.

def compute_max_value(**kwargs):
    #remove pass and place your code here
    pass
 
(word,freq) = compute_max_value(word_1 = 1,word_2 = 3,word_3 = 6,word_4 = 5)
print(word,freq) # should return word_3 6