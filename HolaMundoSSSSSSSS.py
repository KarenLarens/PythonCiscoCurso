###Section 1 – The "Hello, World!" Program
###Page for conventional comits https://gist.github.com/parmentf/359667bf23e08a1bd8241fbf47ecdef0
print("Hello world, Im a new baby python")
###You can use empty pint function
print()
###Escape character \n
print("Im a big python -------\n ---------------- \n------------o~")
###Using multiple arguments
print("Im a big python -------\n " , "---------------- \n------------o~" , "\n :)")
###Using multiple arguments whitout spaces
print("My" , "Name" , "is","Karen","Jazmin")
###This example is from Keyword arguments
###In order to use it, it is necessary to know some rules:
#a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
#any keyword arguments have to be put after the last positional argument (this is very important)
print("My name is", "Karen", end=" *")
print("Jazmin Suarez")
#The print() function separates its outputted arguments with spaces. This behavior can be changed, too.
#The keyword argument that can do this is named sep (as in separator).
print("~O", "", "", "", "", sep="-")
#Both keyword arguments can be mixed in one invocation
print("My", "email", "is", sep=" ", end=":\n")
print("Karen", "Jazmin","2025", sep="_", end="@gmail.com")
