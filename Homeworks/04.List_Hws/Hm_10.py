#tabeie benvisid ke bozorg tarin adad list ra neshan dahad

def maxNum(list):
    max = list[0]
    
    for a in list:
        if a > max:
            max = a
    
    return max


print(maxNum([2,5,4,6,8,4]))

        