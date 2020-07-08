import re

# Method 1: Using filter
def alphanum(str1):
    #filtering the string with alphanumeric characters
    alphanumeric_filter = filter(str.isalnum, str1)

    #joining all the characters using join methon
    alphanumeric_string = ''.join(alphanumeric_filter)

    return alphanumeric_string

print(alphanum('abidur.0177$^%$@gmail.com'))


#Method 2: Using Regex

def alphanum2(str2):

    result = re.sub(r'[\W]+', '', str2)
    return result

print(alphanum2('abidur.0177$^%$@gmail.com'))


#Method 3: Without Filtering

def alphanum3(str3):
    return ''.join(char for char in str3 if char.isalnum())

print(alphanum3('abcd 1234 !@#$ ABCD %^&* EFGH ijkl 5678 ()_+'))

