my_list =[( x , y , z ) for x in range ( 1 , 30 ) for y in range ( x , 30 ) for z in
range ( y , 30 ) if x ** 2 + y ** 2 == z ** 2]
print my_list


words = [' one ', ' one ', ' two ', ' three ', ' three ', ' two ']
print list(set(words))

with open ( "d:\day5\exe30.py" , "r" ) as f1:
    print len ( f1.readline().rstrip())
	
func ([ 1 , 2 , 3 ]) # explicitly passing in a list
func () # using a default empty list
def func ( n = []):
   print next  
   return 

