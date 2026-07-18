import random
print("----------- Welcome to mad lib generator-----------")
print("Create your own mad lib stories by blind answers")
print("---------------------------------------------------")

strs=["Today I went to the {place} and saw a {adjective} {animal} eating my {food}",
    
    "At the {place}, a {adjective} {animal} started {verb} with my {food} for {number} minutes",
    
    "My {adjective} {animal} escaped from the {place} carrying {number} {food}s!",
    
    "Once upon a time, a {animal} was {verb} near the {place} looking for {food}",
    
    "Breaking News: A {adjective} {animal} was spotted {verb} at the local {place} with {number} pieces of {food}!",
    
    "I can't believe my {animal} started {verb} right in the middle of the {place} while holding {food}",
    
    "Yesterday, {number} {adjective} animals invaded the {place} and stole all the {food}",
    
    "The {place} was full of {adjective} people {verb} and eating {food} all day long",
    
    "My teacher said a {adjective} {animal} was {verb} in the {place} instead of eating {food}",
    
    "Scientists discovered a {adjective} {animal} at the {place} that only eats {food} while {verb}"]

print()
place=input("Enter a Place: ")
adjective=input("Enter a Adjective: ")
animal=input("Enter a Animal: ")
food=input("Enter a Food: ")
verb=input("Enter a verb (ending with -ing): ")
number=input("Enter a Number: ")

choose=random.choice(strs)
finalstory=choose.format(
    place=place,
    adjective=adjective,
    animal=animal,
    food=food,
    verb=verb,
    number=number
    )
print()
print(".....Your Mad lib story has been created Successfully.....")
print()
print(finalstory)
