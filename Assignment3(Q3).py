ls = eval(input('Enter a list : '))            #Query List
s = eval(input('Enter the Query String : '))   #Query String
lst = []                  #List to store the strings  
for i in ls:
    if i.startswith(s)==True: #Checking if each string begins with the same substring
        lst.append(i)     #Adding them to a new list
print(lst)                #Printing the newly formed list
