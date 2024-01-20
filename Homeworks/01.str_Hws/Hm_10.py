# barname ie benvisid str daryafti ba shart inke ta 4char aval agar 2 harf bozorg bood baghie ro
# ham upper kone


def upper_case(str1):
   numUpper = 0
   for letter in str1[0:4]:
       if letter.upper() == letter:
           numUpper +=1
           
   if numUpper >= 2:
        return str1.upper()
   return str1
        
               
   
        
    
print(upper_case('Salam ali'))    