import time
import random
Place =['Halla2','Nady','Kabareh','gezerah','Point 90', 'Mall Of Egypt']
Sport =['Basket Ball','Football','Volley Ball','Dodge']
Country =['USA','Egypt','Morroco','Algeria','KSA','Jordon','Palastine']
Color =['Blue','Red','Black','Green','White','Yellow','Brown','Pink','Orange']
Transport =['Bus','Car','Van','Taxi','Plane','Train','Helicopter']
Animal =['Dog','Cat','Elephant','Rabbit','Lion','Horse','Cow','Monkey']

print("Welcome to Spy Game")
time.sleep(2)

print("Choose your category \n 1-Place \n 2-Sport \n 3-Country \n 4-Color \n 5-Transport \n 6-Animal")
time.sleep(2)
category = str(input())

print("Enter the number of players : ") 
numOfPlayers = int(input())

print("Enter the number of Spys : ") 
spys = int(input())

if category == "Place":
    TheChoice=random.choice(Place)
elif category == "Sport":
    TheChoice=random.choice(Sport)
elif category == "Country":
    TheChoice=random.choice(Country)
elif category == "Color":
    TheChoice=random.choice(Color)
elif category == "Transport":
    TheChoice=random.choice(Transport)
elif category == "Animal":
    TheChoice=random.choice(Animal)
    
isSpy = random.sample(list(range(numOfPlayers)),spys)
allPlayers = {}

for i in range(numOfPlayers):
    if i in isSpy:
        allPlayers[i] = 'spy'

    else:
        allPlayers[i] = "Player:", i+1

for i in range(numOfPlayers):
    if i in isSpy:
        print("Player:", i+1, ", You are the Spy.")
        time.sleep(1)
        if i != numOfPlayers-1 :
            print("Give the phone to the next player")
            time.sleep(2)
            
    else:
        print("Player:", i+1, ", The",category,"is", TheChoice)
        time.sleep(1)
        if i != numOfPlayers-1 :
            print("Give the phone to the next player")
            time.sleep(2)