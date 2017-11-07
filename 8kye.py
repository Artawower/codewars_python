def disemvowel(string):
    list=['a','e','u','i','o']
    string2 = ''
    for i in string:
       if i.lower() not in list:
           string2 += i
    return string2



if __name__ == "__main__":
	print(disemvowel('sakdjkdaskdpakoOSYJDOKDo'))

