# func ie tarif konid ke 2vomin adad kochik list ra namayesh dahad:

def kochike(numbers):
    if (len(numbers) < 2):
        return 'minimum input must be 2 items'
    if (len(numbers)==2) and (numbers[0] == numbers[1]):
        return 'same number . u cant repeat just a number'
    
    dupItems = set()
    uniqItems = []
    
    for x in numbers:
        if x not in dupItems:
            uniqItems.append(x)
            dupItems.add(x)
            
    uniqItems.sort()
    return uniqItems[1]


print(kochike([4,5,6,3,1,5,7]))