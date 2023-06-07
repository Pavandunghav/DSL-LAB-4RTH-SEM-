
// practical 1
/*
Consider telephone book database of N clients. Make use of a hash table implementation
to quickly look up client‘s telephone number. Make use of two collision handling
techniques and compare them using number of comparisons required to find a set of
telephone numbers



*/



#include<iostream>

using namespace std;

int main(){

int n;


cout<<"ENTER THE NO. OF CLIENTS:";
cin>>n;

// creation of the hash table 


int hashtable[100];


for(int i=0; i<=n;i++){

      hashtable[i]=-1;
}




// inserting the keys in the hashtable
int key;

for(int i=0;i<n;i++){
   
   cout<<"ENTER THE KEYS :";
   cin>>key;
   


  int hashkey=(key%n);
if (hashtable[hashkey]== -1){


  hashtable[hashkey]=key;
  
}

else{
    hashtable[hashkey+1]=key;
}


}


for(int i=0;i<=n;i++){
 
 cout<<hashtable[i]<<endl;

}
 
return 0;
}