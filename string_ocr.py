#Method 1:

def string_occuring(str1, str2):
    result = 0
    str2_len = len(str2) #measuring the length of str2
    for i in range(len(str1)):
        if str1[i:i+str2_len] == str2: #index slicing of string1 and matching with string 2
            result +=  1 #if these two matche then increasing the value of result
    return result

print(string_occuring('I love muri.ilovemuri,muriislife,without mur i am nothing,murei is valobasha','muri'))

#Method 2

def string_occuring2(str1,str2):
    return str1.count(str2)

print(string_occuring2('I love muri.ilovemuri,muriislife,without mur i am nothing,murei is valobasha','muri'))


