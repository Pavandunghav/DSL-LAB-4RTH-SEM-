# this is the practical 1 , done in a python

def linear(hashtable,hashkey,n):
    
    i=1
    while(hashtable[hashkey!=0]):
        
        hashkey=(hashkey+i)%n
        
        i=i+1
    return hashkey 



def linearcount(hashtable,hashkey,n):
    
    i=1
    while(hashtable[hashkey!=0]):
        
        hashkey=(hashkey+i)%n
        
        i=i+1
    return i



def quadratic(hashtable,hashkey,n):
    
    i=1
    
    while(hashtable[hashkey!=0]):
        
        hashkey=(hashkey+i**2)%n
        
        i=i+1
        
    return hashkey 


def quadraticcount(hashtable,hashkey,n):
    
    i=1
    
    while(hashtable[hashkey!=0]):
        
        hashkey=(hashkey+i**2)%n
        
        i=i+1
        
    return i

def display(hashtable,n):
    
    
    for i in range(n):
        print(f"THE KEY  {hashtable[i]} is present at {i}")
        
        
def search(hashtable,n):
    
    value=int(input("ENTER THE VALUE \n"))
    
    k=1
    
    for i in range (n):
      
      if(value==hashtable[i]):
          print(f"{value} is present at {i}  \n ")
          print(f"THE COMPARISONS ARE {k}")
          break;
      
          
      else:
          
          
          if(i==n-1):
          
           print(f"{value} is not found")
         
      k=k+1 
      
      
        
def comparisons(hashtable,hashkey,n):
    
    
    
    
    print(quadraticcount(hashtable,hashkey,n));
    print( linearcount(hashtable,hashkey,n));
    


    




def main():
    n = int(input("ENTER  THE NO. OF DATA :"))

    keys = [0]*n

    for i in range(n):

        keys[i] = int(input("ENTER YOUR KEY:"))
    
    
    print("1] LINEAR PROBING  2] QUADRATIC PROBING    3]COMPARISON  \n ")
    ch=int(input("ENTER YOUR CHOICE (1/2)"))
    
    hashtable=[0]*n
    
    
    
    for i in range(n):
        
        key=keys[i]
        
        
        
        for i in range(n):
            hashkey=(key+1)%n
            
            
            if(hashtable[hashkey]==0):
                hashtable[hashkey]=key
                
            else:
                if(ch==1):
                    hashkey=linear(hashtable,hashkey,n)
                    hashtable[hashkey]=key
                   
    
                    
                
                elif(ch==2):
                    quadratic(hashtable,hashkey,n)
                    hashtable[hashkey]=key
                    
    
                elif(ch==3):
                    hashkey=linear(hashtable,hashkey,n)
                    hashtable[hashkey]=key
                    quadratic(hashtable,hashkey,n)
                    hashtable[hashkey]=key
                    
                    
                    
                    
                    comparisons(hashtable,hashkey,n)
                    
                else:
                    print("ENTER THE VALID CHOICE ")
                  
    
    #display(hashtable,n)
    #search(hashtable,n)
    
    
    
    comparisons(hashtable,hashkey,n)
    
    
    
            
                

main()
