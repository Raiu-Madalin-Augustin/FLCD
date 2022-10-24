# HashTable data structure 
Properties: table (array) and size (int).

#### init(self, size):
__Description:__ The constructor for the SymbolTable takes as an input parameter an integer: "size", which represents the size of the symbol table.  
The table is initialized the given size with empty lists for each "position", ranging from 0 to size.  
__Input:__ int, the size of the table  
__Output:__ none

#### __hash(self, key):
__Description:__ The private hashing function takes a keyword and computed the hashing value as the sum of the ascii code of the lowercase letters found in the given keyword modulo the size of the table.  
__Input:__ string, the keyword  
__Output:__ int, the position where the keyword will be stored in the hashing table  

#### add(self, key):
__Description:__ The add function takes a keyword, computes its hashing value and if it is not already in the table, it adds it on the position given by the hashing value.  
__Input:__ string, the keyword we want to add  
__Output:__ none  

#### contains(self, key):
__Description:__ The contains function checks if a given keyword exists in the table.  
__Input:__ string, the keyword we search for  
__Output:__ boolean, true in case the keyword does exist in the table, and false otherwise.  
__Complexity:__ O(m+n), considering that the complexity of computing the hashing value is O(m), where m is the maximum possible length of a keyword,
and the complexity of finding the keyword in the table is O(n), where n is the number of keywords that have the same hashing value.

### getIndex(self,value):
__Description:__ The getIndex function return the tuple for the position of the value.

__Input:__ the value

__Output:__ index of the value on the has position
#### remove(self, key):
__Description:__ The remove function computes the hashing value, checks if the keyword does indeed exist in the table, and if it does, it removes it.  
__Input:__ string, the keyword we search for  
__Output:__ none