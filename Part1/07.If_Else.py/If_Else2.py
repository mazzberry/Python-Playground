

kharid = float(input('mablagh ra vared konid : ')) 
#input voroodi ro str daryaft mikone va ma bayad tabdil be vahed hay adadi konim
#mesl float ya int



if kharid < 40000:
    takhfif_1 = kharid * 0.05
    
    print(f'takhfif {takhfif_1:.0f} T')  #{takhfif:.0f} baray inke ashar dide nashe

    
else: 
    kharid > 40000
    takhfif_2 = kharid * 0.15
    print(f'kharid ba {takhfif_2:.0f}T takhfif  anjam shod')