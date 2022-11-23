'''
Author: 0xHamza
Subject: Nested List Reverse
Description: 'İç içe olan listeye içlerindeki elemanlarıyla berabver terse çevirme.'
Date: 23.11.2022
Source:
	-https://app.patika.dev/courses/python-temel/proje
'''


def deep_reverse(mylist):                  
    res = []                                #Tersledigimiz listeleri tutacagimiz degisken
    for e in mylist:                        #Ic ice listelerin icine girilir
        if isinstance(e, list):             #Eger elemean bir list ise, nested list yapisi isE:
            res.append(deep_reverse(e))     #Recursive bir yapi ile o listenin icindeki elemanlari da sonuc degiskenine al
        else:                               #Nested list yapisi yoksa yani ic ice bir liste degilse:
            res.append(e)                   #Elemani sonuc degiskenine al
    res.reverse()                           #Alinan elemanları tersle
    return res                              


input = [[1, 2], [3, 4, [11,12]], [5, 6, 7]]
input_reversed = deep_reverse(input);

print("Original: ",input)
print("Reversed: ",input_reversed)
