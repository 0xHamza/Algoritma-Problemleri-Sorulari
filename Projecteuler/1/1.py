def Project_euler (number):
    _sum=0
    for i in range(number):
        if i %3==0 or i %5 ==0:
            _sum +=i
    return _sum
    
print(Project_euler(1000))
