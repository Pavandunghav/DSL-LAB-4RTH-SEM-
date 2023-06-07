'''Consider telephone book database of N clients. Make use of a hash table implementation
to quickly look up client‘s telephone number. Make use of two collision handling
techniques and compare them using number of comparisons required to find a set of
telephone numbers
'''
def linear(key,hashtable,hashkey,n,i):
    
    
    #hashkey=(hashkey+i)%n
    
    while(hashtable[hashkey]!=0):
      
         hashkey=(hashkey+i)%n
         i=i+1
         
         
        
    
    return hashkey

    
    
        
    #print(hashtable)
    

def quadratic(key,hashtable,hashkey,n,i):
    
    
    
    #hashkey=(hashkey+i**2)%n
    
    while(hashtable[hashkey]!=0):
        
        
        hashkey=(hashkey+i**2)%n
    
        i=i+1
        
        
        
        
        
    return hashkey


def display(hashtable,n):
    
    for i in range(n):
         print(f"{hashtable[i]}  IS PRESENT AT :{i}")   

def  search(hashtable,n):
    value=int(input("ENTER THE KEY YOU WANT TO FIND :\n "))
    
    for i in range(n):
      
        if(value)==hashtable[i]:
        
            print(f"{value}  IS PRESENT AT :{i}")   
            
            
            break;
          
        else:
            
            
            continue;
        
        
        
    
            
            if(i==n-1):
             print("key is  not found \n")
            
            
            
def main():
    
    
    n=int(input("ENTER THE NO. OF PEOPLE:\n "))
    
    
    hashtable=[0]*n
    
    keys=[0]*n
    
    
    for i in range(n):
        
        keys[i]=int(input("ENTER THE PHONE NO.:"))
        
    
    
    print("1]LINEAR PROBING   \t    2]QUADRATIC PROBING \n")
    ch=int(input("ENTER YOUR CHOICE :"))
    
    
    
    
    
    for i in range(n):
        
        key=keys[i]
       
        
        hashkey=key%n
        
        
        
        if(hashtable[hashkey]==0):
            hashtable[hashkey]=key
            
        
        else:
            if(ch==1):
                
               hashkey= linear(key,hashtable,hashkey,n,0)
               hashtable[hashkey]=key
               
                
            elif(ch==2):
                
                hashkey=quadratic(key,hashtable,hashkey,n,0)
                hashtable[hashkey]=key
                
            else:
                
                print("ENTER PROPER CHOICE :")
    print(hashtable)
    display(hashtable,n)
    search(hashtable,n)




main()