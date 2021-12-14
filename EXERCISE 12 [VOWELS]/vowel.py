vowels=['a','e','i','o','u','A','E','I','O','u']
string=input("enter the string:")
vow=[v for v in string if v in vowels]
print("vowels in",string,"are:",vow)
