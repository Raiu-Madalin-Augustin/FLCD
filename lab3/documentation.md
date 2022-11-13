# Scanner Integration

Integrated in the same directory the:
- Scanner
- HashTable
- token.in
- p1, p1err, p2, p3
- PIF.out, ST.out
- main

#PIF class
###Insert(token,position):
__inserts the given token and its position in the Symbol table in the PIF list of pairs__
# Scanner Implementation
The scanner separates each token from every line then checks character by character what type the token can be and adds it to his corresponding list of tokens
after registering all tokens the will be added to the symbol table and Pif with their positions, operators and reserved words have (-1,-1)
constants and identifiers will be saved with the name "constant" and  "identifier" along with their position
###get_reserved_words(): 
__returns a list of reserved words__
    
###get_operators_words(): 
__returns a list of operators__
    
###get_separators_words(): 
__returns a list of separators__
    
###read_tokens(): 
__reads the tokens that will be used from token.in__

###is_operator(elem):
__checks if the element is an operator__

###is_constant(elem):
__checks if the element is a constant__

###is_identifier(elem):
__checks if the element is an identifier__

###get_line_tokens(line):
__returns the list of tokens found on the given line__


![](D:\Year_3_sem_1_Projects\FLCD\FLCD\lab3\1.png)
