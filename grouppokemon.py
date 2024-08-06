# Joseph Gerard
# This program creates classes for Pokemon moves. It then generates 5 random moves from a list of 9 moves, and displays the information, as well as a random attack value for given move. 

#importing the random library for use in calcuating damage numbers
import random

#defining the move class, uses name, type, low damage, and high damage parameters
class Move():
    def __init__(self,moveName,elementalType,lowDamage,highDamage): 
        self.move_name = moveName
        self.elemental_type = elementalType
        # the inputs for low and high damage, converts values to integers for use in functions
        self.low_damage = int(lowDamage)
        self.high_damage = int(highDamage)

        #the function for getting info on a pokemon
    def get_info(self):
        #concatenated string that gives all the information about a specific pokemon move
        information = (f"{self.move_name} (Type: {self.elemental_type}): {self.low_damage}-{self.high_damage}")
        return information
    
    #the function to generate attack values
    def generate_attack_value(self):
        #uses the random library to select any number in the range of the low damage to the high damage
        damage = random.randint(self.low_damage,self.high_damage)
        return damage

#the pokemon class 
class Pokemon():
    #takes name, type and hit points as parameters
    def __init__(self, name, elementalType, hitPoints):
        self.name = name
        self.elemental_type = elementalType
        self.hit_points = hitPoints
        self.list_of_moves = []

    #function for getting info on a pokemon.
    def get_info(self):
        #concatenated string displaying all of the information about given pokemon
        information = (f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}")
        return information
    
    #function for healing a pokemon
    def heal(self):
        #takes the pokemon's hit points and adds 15, then updates the number
        self.hit_points = self.hit_points + 15
        #message displaying the pokemon's name and their new hit points. 
        healMessage = (f"{self.name} has been healed to {self.hit_points} hit points.")
        return healMessage
    
    def display_choices(self):
        print("Your options:")
        for count, move in enumerate(self.list_of_moves):
            print(f"{count + 1}: {move.get_info()} ")
        healMessage = "H: Heal 15 hit points"
        return healMessage

    def attack(self,move_Index:int,opposingPokemon): 
        move_Index = int(move_Index)
        moveMessage = (f"{self.name} used {self.list_of_moves[move_Index - 1].move_name}!")
        damage = self.list_of_moves[move_Index - 1].generate_attack_value()
        #type advantage logic
        if str(self.list_of_moves[move_Index - 1].elemental_type) == "Grass":
            if opposingPokemon.elemental_type == "Fire":
                multiplier = 0.5
                damageMessage = "It's not very effective..."
            elif opposingPokemon.elemental_type == "Water":
                multiplier = 2.0
                damageMessage = "It's super effective!"
            else:
                pass
        elif str(self.list_of_moves[move_Index - 1].elemental_type) == "Fire":
            if opposingPokemon.elemental_type == "Water":
                multiplier = 0.5
                damageMessage = "It's not very effective..."
            elif opposingPokemon.elemental_type == "Grass":
                multiplier = 2.0
                damageMessage = "It's super effective!"
            else:
                pass
        elif str(self.list_of_moves[move_Index - 1].elemental_type) == "Water":
            if opposingPokemon.elemental_type == "Grass":
                multiplier = 0.5
                damageMessage = "It's not very effective..."
            elif opposingPokemon.elemental_type == "Fire":
                multiplier = 2.0
                damageMessage = "It's super effective!"
            else:
                pass
        else: 
            multiplier = 1
            damageMessage = ""
        
        #critical hit logic
        critical_hit=random.random ()<.06
        if critical_hit is True :
            critMult = 1.5
            criticalMessage = "Critical hit!"
        else:
            critMult = 1
            criticalMessage = ""
        
        adjustedDamage = damage * critMult * multiplier
        
        finalDamage = round(adjustedDamage)

        opposingPokemon.hit_points = opposingPokemon.hit_points - finalDamage
        
        return (f"{moveMessage}\n{damageMessage} {criticalMessage}\n{opposingPokemon.name} took {finalDamage} points of damage!")
        
                
#new pokemon battle function
def pokemon_battle(yourPokemon,opposingPokemon) :
    print("Battle Start!")
    print(f"{opposingPokemon.name} wants to fight!")
    print(f"Go! {yourPokemon.name}\n")

    while yourPokemon.hit_points > 0 and opposingPokemon.hit_points > 0 :
        print("Opponent:", opposingPokemon.get_info())
        print("You:", yourPokemon.get_info(), "\n")
        print(yourPokemon.display_choices())
        
        yourChoice = input("Choose an option: ")
        if yourChoice == "H" :
            print(Pokemon.heal(yourPokemon))
        else:
            print(yourPokemon.attack(yourChoice, opposingPokemon)) # if this isn't working, just hardcode list of moves at the 0

        if opposingPokemon.hit_points <= 0:
            input("\nPress enter to proceed...")
            print(f"{opposingPokemon.name} was defeated!")
            print(f"{yourPokemon.name} won the battle!")
            break
        
        input("\nPress enter to proceed...")

        opponent_action = random.choice(['attack', 'attack', 'heal'])
        if opponent_action == 'heal':
            print(opposingPokemon.heal())
        else:
            move_index = random.randint(1, len(opposingPokemon.list_of_moves))
            print(opposingPokemon.attack(move_index, yourPokemon))

        if yourPokemon.hit_points <= 0:
            input("\nPress enter to proceed...")
            print(f"{yourPokemon.name} was defeated!")
            print(f"{opposingPokemon.name} won the battle!")
            break

        input("\nPress enter to proceed...")


tackle = Move("Tackle", "Normal", 5, 20)
quickattack = Move("Quick Attack", "Normal", 6, 25)
slash = Move("Slash", "Normal", 10, 30)
flamethrower = Move("Flamethrower","Fire",5,30)
ember = Move("Ember","Fire", 10, 20)
watergun = Move("Water Gun", "Water", 5, 15)
hydropump = Move("Hydro Pump","Water", 20, 25)
vinewhip = Move("Vine Whip", "Grass", 10, 25)
solarbeam = Move("Solar Beam","Grass", 18, 27)

#turning the moves into a list for ease of use
listOfMoves = [tackle,quickattack,slash,flamethrower,ember,watergun,hydropump,vinewhip,solarbeam]

print("These are the moves the Pokemon will randomly select from:")
for move in listOfMoves :
    print(f"{Move.get_info(move)} Attack Points")

bulbasaur = Pokemon("Bulbasaur", "Grass", 60)
charmander = Pokemon("Charmander", "Fire", 55)
squirtle = Pokemon("Squirtle", "Water", 65)

#a list of the 3 pokemon found above, to be used in a loop later
pokemonList = [bulbasaur, charmander, squirtle]

available_moves = listOfMoves.copy()  # Keep track of moves that can still be assigned

for pokemon in pokemonList:
    valid_moves = [move for move in available_moves if move.elemental_type == pokemon.elemental_type or move.elemental_type == "Normal"]

    randomMove1 = random.choice(valid_moves)
    pokemon.list_of_moves.append(randomMove1)
    available_moves.remove(randomMove1)
    valid_moves.remove(randomMove1)

    randomMove2 = random.choice(valid_moves)
    pokemon.list_of_moves.append(randomMove2)
    available_moves.remove(randomMove2)

    print(f"{pokemon.name} was assigned:")
    for move in pokemon.list_of_moves:
        print(f"\t{move.move_name}")

print("Available Pokemon:")
availablePokemon = pokemonList.copy()
for count, pokemon in enumerate(pokemonList) :
    print(f"{count + 1}: {Pokemon.get_info(pokemon)}")

#from here on is step three, all of the above code should work perfectly, the code below is kinda messed up so feel free to change it however you like
#that being said, parts of it are probably good

decision1 = int(input("Choose the # of your Pokemon: "))
if decision1 == 1 :
    yourPokemon = availablePokemon[0]
elif decision1 == 2 :
    yourPokemon = availablePokemon[1]
else:
    yourPokemon = availablePokemon[2]
print(f"\nYou chose {yourPokemon.name} as your Pokemon.\n")
availablePokemon.remove(yourPokemon)


for count, pokemon in enumerate(availablePokemon) :
    print(f"{count + 1}: {Pokemon.get_info(pokemon)}")


opposingPokemon = int(input("Choose the # of the opposing Pokemon: "))
if opposingPokemon == 1:
    opposingPokemon = availablePokemon[0]
else :
    opposingPokemon = availablePokemon[1]
print(f"\nYou chose {opposingPokemon.name} as the opponent.")

pokemon_battle(yourPokemon, opposingPokemon)
