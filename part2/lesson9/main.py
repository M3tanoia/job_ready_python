#learning about tuples
# thisTuple = ("element1", "element2", "element3")

#creating a tuple example
age_range = (18,120)
#tuple containing only numbers
print(age_range)
print(type(age_range))
 
#tuple containing strings and numbers
info = ("Maria", "Smith", 31, "123 Main Street", "000-00-0000")
print(info)
print(type(info))

print("------------------------------------------------------------------------------------------------------")

#Python assigns an index value to each item in a tuple, 
# starting with the value 0 for the first item and continuing with sequential values for the remaining items.
#tuple[index_value]

info = ("Maria", "Smith", 31, "123 Main Street", "000-00-0000") 
print(info)
print(len(info))
print(info[0]) #retrieves the first item in the tuple
print(info[1])
print(info[2])
print(info[3])
print(info[4])

#index value −1 always references the last item in a list, regardless of how many items there are. 
info = ("Maria", "Smith", 31, "123 Main Street", 
  "000-00-0000", "Boston", "Software Developer")
print(info[-1]) #last item in the tuple
print(info[-2]) #second to last item in the tuple

print("------------------------------------------------------------------------------------------------------")

#slicing a tuple
info = ("Jonathan", "Vance", "679 Birchpond Street","Merrillville", "IN", "46410")
# we extract only the first two elements from the tuple and 
# store them in a new tuple
name = info[0:2]  
print("The name is:")
print(name)
 
# we extract only the last four elements from the tuple and 
# store them in a new tuple
address = info[2:6]
print("The address is:")
print(address)

print("------------------------------------------------------------------------------------------------------")

#concatenating tuples

name=("Layla","Bernstein",)
address=("123 Main Street, Leola, AR, 19987",)
contact=("474-887-9483","LBernstein@email.com",)
fullcontact = name + address + contact
print(fullcontact)

print("------------------------------------------------------------------------------------------------------")

#searching tuples
# create a tuple
tuple_of_names = ("Kate","Jennifer","Mike","Pete","Alex","Mike")
search_term = "Mike"
 
# check that the search term occurs at least once in the tuple
if search_term in tuple_of_names:
    print (search_term + " appears at least once in the tuple.")
 
# iterate through tuple to see if search term can be found
for name in tuple_of_names:
    if name == search_term:
        print("We found " + search_term)