def funky(a,b):

    if type(a) == str and type(b) == str:
        
        print (a + b)

    elif type(a) == int and type(b) == int:
        
        print (a + b)

    elif type(a) == float and type(b) == float:
        
        print (a + b)

    elif type(a) == list and type(b) == list:
        
        print (a + b) 

    else:
        
        print ("try again")

        
funky("uptown","funk")
funky(6,8)
funky(4.8, 3.3)
funky([34,45,56,67],[25,53,36,67])
funky("uptown", 8)
funky(4.9, 8)

a = {"artist": "mark ronson","song": "uptown funk"}

b = {"featuring":"bruno mars", "year": 2015}

a.update(b)

print (a)