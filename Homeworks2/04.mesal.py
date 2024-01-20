#az client adadi ro daryaft kon , agar string vared kard error bede:

while True:
    
    try:
    
        num = int(input('adad ra vared kon :'))
        break
        
    except ValueError:
        print('\n adad vared nakarde ied , dobare talash konid ...')
        print()
