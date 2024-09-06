# I would like to say a few (adjective) words about the most important invention of the twentieth century.
# I am not referring to (an invention) or even the discovery of (a food).
# The most (adjective) invention, in my opinion, is the sneaker. If it were not for sneakers,
# our (part of body plural) would be dirty, cold, and (adjective).
# Sneakers keep me from skidding if the (plural noun) are slippery, and when I run,
# they keep me from stubbing my (plural noun).

#creating variables

strAdj1 = input("Enter an adjective: ")
strAdj2 = input("Enter an adjective: ")
strAdj3 = input("Enter an adjective: ")
strPnoun1 = input("Enter a plural noun: ")
strPnoun2 = input("Enter a plural noun: ")
strInv1 = input("Enter the name of an invention: ")
strFood = input("Enter a food: ")
strBodyPart = input("Enter a body part plural: ")

# recording input

print(strAdj1, strAdj2, strPnoun1, strPnoun2, strInv1, strFood, strBodyPart)

# give output

print(("I would like to say a few " + strAdj1 + " words about the most important invention of the twentieth century. \n"
"I am not referring to " + strInv1 + " or even the discovery of " + strFood + ". \n"
"The most " + strAdj2 + " invention, in my opinion, is the sneaker. If it were not for sneakers, \n"
"our " + strBodyPart + " would be dirty, cold, and " + strAdj3 + "."
"Sneakers keep me from skidding if the " + strPnoun1+ " are slippery, and when I run, \n"
"they keep me from stubbing my " + strPnoun2 +"."))


# different method

# assigning a variable to give output

#strStory = (("I would like to say a few " + strAdj1 + " words about the most important invention of the twentieth century. \n"
#"I am not referring to " + strInv1 + " or even the discovery of " + strFood + ". \n"
#"The most " + strAdj2 + " invention, in my opinion, is the sneaker. If it were not for sneakers, \n"
#"our " + strBodyPart + " would be dirty, cold, and " + strAdj3 + "."
#"Sneakers keep me from skidding if the " + strPnoun1+ " are slippery, and when I run, \n"
#"they keep me from stubbing my " + strPnoun2 +"."))

# printing the string variable

#print(strStory)
