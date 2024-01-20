

class Dates:
    
    @staticmethod
    def toDashDate(date):
        return date.replace('/','-')
    
    
newDate = '2023 / 19 / 2'    

removedDash = Dates.toDashDate(newDate)

print(removedDash)


