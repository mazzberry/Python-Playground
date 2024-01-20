

name = "mohammad"

sv_name = "Myrath" 

message = "salam be discord Myrath khoshoomadi"
message_1 = f"salam {name} be discord {sv_name} khoshoomadi "

print (message)
print (message_1)

#__________________________

age = input("how old are u :")
name = input("what's ur name :")

lastName = input("and! last lastname??? : ")

message = (f" ur name is {name} and ur lastname is {lastName} and you're  {age} yearold") 

print(message.capitalize()) # (variable.capitalize()) harf aval ro bozorg mikone.

#__________________________
pi = 3.14159265

jomle_1 = f'adad pi barabar ba {pi}'
jomle_2 = f'adad pi barabar ba {pi:.2f}'

print(jomle_1)
print(jomle_2)

#__________________________

name = 'Amirhossein'
job = 'Developer'
age = 60

msg = (
    f'hi \t {name}'
    f"you're a \t {job}"
    f'and you \t are {age} year old'
)

print(msg.expandtabs(2))
