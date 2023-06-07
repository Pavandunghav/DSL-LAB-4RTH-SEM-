'''To create ADT that implement the &quot;set&quot; concept.
a. Add (new Element) -Place a value into the set , b. Remove (element) Remove the value
c. Contains (element) Return true if element is in collection, d. Size () Return number of
values in collection Iterator () Return an iterator used to loop over collection, e.
Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subset'''


def main():

   # se = sets()

    n = int(input("ENTER THE NO. OF ELEMENTS YOU WANT TO ADD"))

    s1 = set()

    for i in range(n):

       

        ele = int(input("enter the new element :"))

        s1.add(ele)
        
        

    print(s1)

    # removing the element from the set  by using the remove function 
    
   
        
    key=int(input("ENTER THE ELEMENT THAT YOU WANT TO REMOVE FROM THE SET :"))
    
    
    if key not in s1:
        print("tTHIS KEY DOESNT EXIST INT HE SET :")
        
    if key in  s1:
       s1.remove(key)
        
     
    print(s1)
    
    
   
   
   # finding the element 
   
    key2=int(input("ENTER THE ELEMENT THAT YOU WANT TO FINDs FROM THE SET :"))
    
    
    if key2 in s1:
        
        print("it exist ")
    if key2 not in s1:
        print("tTHIS KEY DOESNT EXIST IN  THE SET :")
        
    
    
    
    print("THE SIZE OF THE SET IS :",len(s1))
    print("BELOW IS FOR ANOTHER SET :")
    
    
    n2= int(input("ENTER THE NO. OF ELEMENTS YOU WANT TO ADD"))

    s2 = set()

    for i in range(n):

       

        ele2 = int(input("enter the new element :"))

        s2.add(ele2)
        
        

    print(s2)
    
    
    
    
    print("TAKING THE UNION FOR THE SETS :\n")
    
    
    
    print("THE UNION OF THE SETS IS :",s1 | s2)
   
    print("THE intersection OF THE SETS IS :",s1 & s2)
    
    
    
    print("THE SIZES OF THE SETS ARE :",len(s1), len(s2))
    
    
    
    print("THE DIFFERENCE BETWEEN THE TWO SETS IS :",s1-s2)
    
    
    
    
    print("IS THERE A SUBSETS OF EACH OTHER :\n ")
    
    
    
    print(s1.issubset(s2))
    
    
    
   
main()
