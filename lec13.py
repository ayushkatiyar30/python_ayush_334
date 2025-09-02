# strings are immutable
a= "s ,,A Yush !Y!,,"
# b= (a.upper())
print(a.upper())    # doesn't changes the primary string,creates a new one
print(a.lower())
print(a.rstrip())
print(a.rstrip(","))   #removes only those who are at last or trailing one
print(a.rstrip("!"))   #doesn't removes from b/w    
print(a.replace("Y","y"))  #replaces all Y by y present in string
print(a.split(" "))     #converts string into list
print(a.capitalize())    #make the first character have upper case and the rest lower case
print(a.center(17))
print(len(a.center(17)))
print(len(a))
print(a.count(","))
print(a.endswith(",,,"))   #let us know ki koi string ends with that or not
print(a.endswith(",,"))     #startswith same with starting 
print(a.endswith("A",0,5))
print(a.find("A"))
print(a.index("A"))  #dono find aur index same kaam krte hai pr find na milne pr -1 aur index error deta hai
#a.isalnum() if whole string alpha,numeric(A,a-z,Z)(0-9)
#isalpha() only characters
# islower() all lower, isprintable() all printable false is \n used and all
#isspace() if their are white spaces
#istitle() each word of string is capitalised & isupper all upper
#swapcase() each case of string changes to the other case(upper to lower and vise versa)
#title() capitalises every word's first letter