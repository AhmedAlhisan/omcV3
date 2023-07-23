from django.test import TestCase

# Create your tests here.
def test ():
    x = [ 1 ,2 , 3,4 , 5]
    for i in x:
        print(i)
        if i >= 5:
            print('***')
        else:
            print('yes')
        
    

print(test())    