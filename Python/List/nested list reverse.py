'''
Author: 0xHamza
Subject: IRREGULAR LIST TO FLATTEN LIST
Description: 'Patika.dev python projesi odevi cozumu.'
Date: 23.11.2022
Source:
	-https://app.patika.dev/courses/python-temel/proje
    -https://stackabuse.com/python-how-to-flatten-list-of-lists/
'''

#Example 1:
res = []
def flatten(l):
    for e in l:
        if( type(e) == list):
            flatten(e)
        else:
            res.append(e)


#Example 2 Recursion:
def flattenRec(l):                                  #Recursrive olacak fonksiyon olusturuldu
    if len(l) == 0:                                 #gelen 'l' eger bir boyuta sahip degilse non iterable demektir oyleyse: 
        return l                                    #flatten liste eklenecek tekil deger olarak direk alinir.
                                                    #gelen 'l' boyutu 0 dan buyukse iterable ise:
    if isinstance(l[0], list):                      #'l' nin 0. indeksi bir listse ise :
        return flattenRec(l[0]) + flattenRec(l[1:]) #onunda icine girerek ardisillarini eklemek lazim
                                                    #'l' nin 0. indeksi bir list degise :
    return l[:1] + flattenRec(l[1:])                # retrun l(0) + l( 1: ...)) digerleri eklenir
    
    
    
l = [[1,'a',['cat'],2,[[3]]],'dog',4,5]

flatten(l)
print(res)          #result: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]

f = flattenRec(l)
print(f)            #result: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]