# tabeyi tarif konid ke ba daryaft jomle kalamt tekrari ra beshmorad


def wordCount(str):
    
    counts = dict()
    words = str.split(' ')
    
    for word in words :
        if word in counts:
            counts[word] +=1
        else :
            counts[word] =1
                

    
    
    
    return counts


print(wordCount('ali ali ali'))

