
from collections import namedtuple

animal = namedtuple( "animal" , "name age type" )

jimmy = animal(name = 'a1' , age = 9 , type = 'cat')


print(jimmy.name , jimmy.type)

# va hamintor qabeliat index az beyn narafte...

print(jimmy[0])