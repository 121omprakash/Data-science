name = 'Om Prakash'
lname = 'Kumar'
print("1.use of len() inbuilt method of print: ")
print("-----------------------------")
print("Length of name: ",len(name))
print("2.use of replace method: ")
s = name.replace('Om','Kumar')
print(name,"->",s)
print("-----------------------------")
print("3.string concatenation : ")
print("Full name: ",name+lname)
print("-----------------------------")
print("4.string replication: ",name*3)
print("-----------------------------")
print("5. Slicing: ")
print(name[0],name[-1],name[::-1],sep="\n")
print("-----------------------------")
a = "               Om Prakash                            "
print("6. Stripping: ",a.strip())
print("7. left stripping: ",a.lstrip())
print("8. right stripping",a.rstrip())
print("-----------------------------")
print("9. Indexing: ",name.index('Om'))
name = "Om om Prakash Om"
print("10. Sub string count: ",name.count('Om'))
print("11. finding substring: ",name.find('Om'))
print("-----------------------------")
print("Case conversion: ")
print("Upper: ",name.upper())
print("Lower: ",name.lower())
print("Title: ",name.title())
print("Capatalize: ",name.capitalize())
name = 'om'
courese = 'BCA'
enrol = 131
print("-----------------------------")
print("string formatting: ")
print("Default formatting: ","{} {} {}".format(name,courese,enrol))
print("Positional formatting: ","{2} {0} {1}".format(name,courese,enrol))
print("Keyword Formating: ")
print("{n} {e} {c} ".format(n=name,e=enrol,c=courese))
print("-----------------------------")
print("String Check: ")
print("Check for a digit: ",name.isdigit())
print("Check for alphabet: ",name.isalpha())
print("Check for lower case",name.lower())
print("Check for Upper case: ",name.isupper())
print("Adjusting the character: ")
print("Centre: ",name.center(20,'-'))
print("Left Adjust: ",name.ljust(20,'#'))
print("Right Adjust: ",name.rjust(20,'$'))
