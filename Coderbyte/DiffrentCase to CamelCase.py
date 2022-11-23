def DifferentCases(strParam):

  newStr = ''
  finalWord = []
    
  for char in strParam:
    if char.isalpha():
      newStr += char
    else:
      newStr += ' '
  
  for word in newStr.split():
    l = list(word)
    l[0] = l[0].upper()
    for i in range(1,len(l)):
      l[i] = l[i].lower()
    s="".join(l)
    finalWord.append(s)
  

  bas = list(finalWord[0])
  bas[0] = bas[0].lower()
  finalWord[0] = "".join(bas)

  return ''.join(finalWord)

# keep this function call here 
print(DifferentCases("BOB loves-coding,for*ever"))

"""
input: "BOB loves-coding,for*ever"
correct: "bobLovesCodingForEver"
"""