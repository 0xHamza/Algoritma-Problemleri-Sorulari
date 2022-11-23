def ArrayChallenge(strArr):

  result = "not possible"
  word = strArr[0]
  lst = list(strArr[1].split(","))
  
  l1 = list()

  for e in lst:
    temp=True
    for i in range(len(e)):
      if(e[i] != word[i]):
        temp=False
        break
    if(temp):
      l1.append(e)


  for e in l1:
    last = word[len(e):]
    if last in lst:
      result = e+","+last
      

  return result

# keep this function call here 
print(ArrayChallenge(["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]))

"""
input: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]
output: hello,cat

input: ["hellodog", "apple,bat,cat,goodbye,hello,yellow,why"]
output: not possible



QUESTION:
    For example: strArr can be: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]. 
    Your goal is to determine if the first element in the input can be split into two words, 
    where both words exist in the dictionary that is provided in the second input. In this example, 
    the first element can be split into two words: hello and cat because both of those words are in the dictionary.
"""