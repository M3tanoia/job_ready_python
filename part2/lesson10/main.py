#Lesson 10 Dictionaries

#Data structure types:
#Lists - ordered and mutable example: 1 = [1,2,"a"]
#Tuples - ordered and immutable. exmaple: t = (1,2,"a")
#Dictionary - unordered, mutable, indexed, and has keys:values. example: d = {"a":1, "b":2}
#Set - unordered collection of items. Every set element is unique and immutable. example: s = {1,2,3}

#dictionaries are a collection of items in key:value pairs (both must be defined) and keys must be unique 

#METHOD     DESCRIPTION
#keys()	    Returns a list containing the dictionary's keys
#items()	Returns a list containing a tuple for each key: value pair
#values()	Returns a list of all the values in the dictionary
#get()	    Returns the value of the specified key
#pop()	    Removes the element with the specified key
#update()	Updates the dictionary with the specified key: value pairs
#copy()	    Returns a copy of the dictionary
#clear()	Removes all the elements from the dictionary

#creating a dictionary
accounts_dict = dict()
accounts_dict['X10000'] = 'Anita'   #Assign key X10000 and value Anita
accounts_dict['X10002'] = 'Michael' #Assign key X10002 and value Michael
accounts_dict['X10003'] = 'Nia'     #Assign key X10003 and value Nia
print(accounts_dict)

print("-------------------------------------------------------------------------------------------------")

#one step dictionary
myFirstDict = {
  "brand": "Mercedes",
  "model": "GLE",
  "year": 2021
}
print(myFirstDict)

print("-------------------------------------------------------------------------------------------------")

#using a dictionary for abbreviations

states = {
 "AL":    "Alabama",
 "AK":    "Alaska",
 "AZ":    "Arizona",
 "AR":    "Arkansas",
 "CA":    "California",
 "CO":    "Colorado",
 "CT":    "Connecticut",
 "DE":    "Delaware",
 "FL":    "Florida",
 "GA":    "Georgia",
 "HI":    "Hawaii",
 "ID":    "Idaho",
 "IL":    "Illinois",
 "IN":    "Indiana",
 "IA":    "Iowa",
 "KS":    "Kansas",
 "KY":    "Kentucky",
 "LA":    "Louisiana",
 "ME":    "Maine",
 "MD":    "Maryland",
 "MA":    "Massachusetts",
 "MI":    "Michigan",
 "MN":    "Minnesota",
 "MS":    "Mississippi",
 "MO":    "Missouri",
 "MT":    "Montana",
 "NE":    "Nebraska",
 "NV":    "Nevada",
 "NH":    "New Hampshire",
 "NJ":    "New Jersey",
 "NM":    "New Mexico",
 "NY":    "New York",
 "NC":    "North Carolina",
 "ND":    "North Dakota",
 "OH":    "Ohio",
 "OK":    "Oklahoma",
 "OR":    "Oregon",
 "PA":    "Pennsylvania",
 "RI":    "Rhode Island",
 "SC":    "South Carolina",
 "SD":    "South Dakota",
 "TN":    "Tennessee",
 "TX":    "Texas",
 "UT":    "Utah",
 "VT":    "Vermont",
 "VA":    "Virginia",
 "WA":    "Washington",
 "WV":    "West Virginia",
 "WI":    "Wisconsin",
 "WY":    "Wyoming"
}
print(states)

print("-------------------------------------------------------------------------------------------------")

#working with dict items
#print total and average income for all years

yearly_revenue = {
    2017 : 100000,
    2018 : 120000,
    2019 : 125000, 
    2020 : 130000,
    2021 : 135000,
}

total_income = yearly_revenue[2017]+yearly_revenue[2018]+yearly_revenue[2019]+yearly_revenue[2020]+yearly_revenue[2021]
average_income = total_income/5

print(total_income)
print(average_income)

print("-------------------------------------------------------------------------------------------------")

#pull values from the dict using keys() method

students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10002'] = 'Nia'
students_dict['X10001'] = 'Anita'
 
for student_id in students_dict.keys():
    print(students_dict[student_id])

print("-------------------------------------------------------------------------------------------------")

#adding information into a dictionary

loans = dict()
ctr = 1
while ctr <= 5:
   loan_id = input("Please enter the loan ID for loan "+str(ctr)+": ")
   loan_amt = input("Please enter the loan amount for loan "+str(ctr)+": ")
   loans[loan_id]=loan_amt
   ctr+=1
 
for key,value in loans.items():
   print(key,": ", value)

print("-------------------------------------------------------------------------------------------------")

#display keys, values, and items from a dictionary

students_dict = dict()
students_dict['X10000'] = 'Michael'
students_dict['X10002'] = 'Nia'
students_dict['X10001'] = 'Anita'
 
print(students_dict.keys())
print(students_dict.values())
print(students_dict.items())

print("-------------------------------------------------------------------------------------------------")





