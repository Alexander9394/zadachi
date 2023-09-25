shotrange = float(input('Введите дальность выстрела - '))

if shotrange > 28 and shotrange < 30:    
    print ('ПОПАЛ')

elif shotrange >= 30:    
    print ('ПЕРЕЛЕТ')

elif shotrange > 0 and shotranget <= 28:    
    print ('НЕДОЛЕТ')

elif shotrange >= 0:    
    print ('НЕ БЕЙ ПО СВОИМ')