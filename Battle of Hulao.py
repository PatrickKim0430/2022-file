
# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/5 
# Game name: Text based game / Battle of Hulao 
# Solution: Using python(visual studio) and codehs to create text based game



# Battle of Hulao
place = random.randint(11,19)
# objects 
#Bedroom --> Bed,  closet, clock, pillow, dresser
#Kitchen --> oven, table, chair, frying pan, knife  
#Treasure room --> Chest, armor, saddle, sword, shield, and lamp

# variables

 elif room_command == "enter treasure room":   
        y = 3
        print("Woah. It's a treasure room, there are chest, armor, saddle, sheild, lamp, and sword")
        print()

lif room_command == "look in bed":
        if y == 1:
            print("We can't look inside the bed.")
        else:
            print("I think there is no bed in this room")
    elif room_command == "look on bed":
        if y == 1:
            print("There are sheets and a pillow.")
        else:
            print("There is no bed in this room.")
    elif room_command == "look behind bed":
        if y == 1:
            if place == 11:
                print("A KEY! Maybe there's a chest somewhere we can open it with!")
                print("🔑")
                k = 1
            else:
                print("Nothing here!")
        else:
            print("There is no bed in this room.")
    elif room_command == "look under bed":
        if y == 1:
            print("AHHHHH! A DEAD BODY!!!!")
        else:
            print("There is no bed in this room.")
    elif room_command == "inspect bed":
        if y == 1:
            print("Okay let's try to find key in this bed.. Use other prepositions to find it")
elif room_command == "look on sofa":
        if y == 1:
            print("A cat is sitting on the sofa. How cute!")
        else:
            print("There is no sofa in this room")
    elif room_command == "look under sofa":
        if y == 1:  
            if place == 12:
                print("A KEY! Maybe there's a chest somewhere we can open it with!")
                print("🔑")
                k = 1
            else:
                print("SOMETHING is crawling under sofa.. Probably best to leave that alone... ")
        else:
            print("There is no sofa in this room.")
          
    elif room_command == "look in sofa":
        if y == 1:
            print("Some old coins are stuck in between the sofa. Take them?")
            print("         _.-'~~`~~'-._ ")
            print("      .'`  B   E   R  `'. ")
            print("    / I                 T \ ")
            print("   / `       .-'~'-.      `\ ")
            print("  / L      / `-    \      Y \\")
            print(" |        />  `.  -.|        |")
            print(" |       /_     '-.__)       | ")
            print(" |        |-  _.' \ |        | ")
            print(" |        `~~;     \\\       |")
            print("  |        /      \\)       |")
            print("   \       '.___.-'`       /     ")
            print("    \                     / ")
            print("     '._    1 9 9 7    _.' ")
            print("       `'-..,,,,,,,,..-'` ")
            take = input().lower()
            if take == "yes":
                print("Coins acquired! Maybe they will come in useful later?")
            else:
                print("My mother did always tell me to leave anything that is not mine alone. ")
        else: 
            print("There is no sofa in this room.")
            
    elif room_command == "inspect sofa":
        if y == 1: 
            print("Whoa.. there are lots of furs which are stick in the chair..")
            print("Maybe there is an animal on the sofa")
            print("MEOW!")
        else: 
            print("NO sofa in this room")
    elif room_command == "look behind sofa":
        if y == 1:
            print("There is something very warm.. Ah! it's an animal's poop")
        else: 
            print("No sofa in this room")
 elif room_command == "look on dresser":
        if y == 1:
            print("AH.. I can't reach the top of the dresser.. ")
        else:
            print("There is no dresser in this room.")
            
    elif room_command == "look behind dresser": 
        if y == 1:
            print("SPIDER webs are behind the dresser.. so sticky!")
        else:
            print("There isn't a dresser in this room.")
elif room_command == "inspect dresser":
        if y == 1:
            print("The dresser seems very classy.. If I find the pandora's box and escape this place, I want to buy a similar dresser")
        else: 
            print("Unfortunately, there isn't a table in this room")
elif room_command == "inspect table":
        if y == 2: 
            print("WOW. This table is made of gold.. It's so shiny!")
        else: 
            print("There isn't a table in this room...")
elif room_command == "look in table":
        if y == 2:
            print("Ah.. It's impossible to look in the table. Try looking near here.")
        else:
            print("There is no table in this room.")
    elif room_command == "look behind table":
        if y == 2:
            print("A wooden chair is behind the table. It seems old.")
        else:
           print("There is no table in this room.")
    elif room_command == "look on table":
        if y == 2:
            if place == 17:
                print("A KEY! Maybe there's a chest that could be opened with it?")
            else:
                print("Rotten food on the table! Gross!")
 elif room_command == "look behind chair":
        if y == 2:
            print("There are some rotten fruits behind the chair..")
        else:
            print("There is no chair in this room.")
    elif room_command == "look on chair":
        if y == 2:
            if place == 18:
                print("A KEY! Maybe there's a chest that could be opened with it?")
                print("")
                k = 1
            else:
                print("Uhhhh. Just a dead body sitting on the chair.")
        else:
           print("There is no chair in this room.")
    elif room_command == "look under chair":
        if y == 2:
            print("some broken dishes are under the chair.. I can't touch it")
        else:
            print("There is no chair in this room.")
    elif room_command == "inspect chair":
        if y == 2: 
            print("This chair is made of metal.. it looks like a special chair!")
        else: 
            print("No chair in this room")
elif room_command == "look in knife":
        if y == 2: 
            print("It's impossible to look in a knife.. use 'inspect' instead of look + preposition words ")
        else: 
            print("No knife in this room")
    elif room_command == "look on knife":
        if y == 2: 
            print("There is nothing on the knife!")
        else: 
            print("There is no knife in this room")
    elif room_command == "look behind knife": 
        if y == 2: 
            print("There is a frying pan behind the knife. Maybe we should check that out too.")
        else: 
            print("It seems there is no knife in this room")
    elif room_command == "look behind knife": 
        if y == 2: 
            print("There is nothing behind the knife.. let's try another command.")
        else: 
            print("No knife in this room")
    elif room_command == "inspect knife":
        if y == 2:
            print("The knife has spots of blood! Oh wait, it's tomato sauce...")
            print("     .---. ")
            print("     |---| ")
            print("     |---| ")
            print(".    |---| ")
            print(" .---^ - ^---. ")
            print(" :___________: ")
            print(".   |  |//| ")
            print("    |  |//| ")
            print("    |  |//| ")
            print("    |  |//| ")
            print("    |  |.-| ")
            print("    |.-'**| ")
            print("     \***/ ")
            print("      \*/ ")
            print("       V ")
            print("       ^' ")
            print("      (_) ")
        else:
            print("There is no knife in this room")
elif room_command == "look in frying pan":
        if y == 2: 
            print("There are spider webs on top of the frying pan.. gross")
        else: 
            print("It seems like there isn't a frying pan in this room")
lif room_command == "inspect frying pan":
        if y == 2:
            print("It's a golden frying pan! I've never seen such material before!")
elif room_command == "inspect chest":
        if y== 3: 
            print("Wait.. this chest seems special")
        else: 
            print("NO chest in this room")
elif room_command == "look in armor":
        if y == 3:
            print("Yikes!! It's empty and there are some bugs in there.")
            print(" \_/-.--.--.--.--.--. ")
            print(" (00)__)__)__)__)__)__) ")
            print("    ******************* ")
        else:
            print("There is no armor in this room ")
    elif room_command == "look behind armor":
        if y == 3:
            print("Lots of weapons such as spear, arrows, lances are behind the armor.. but they are not secret weapon!")
            print()
            print(".-'` |___________________________//////")
            print(" `'-.|                           \\\\\\")
            print("")
        else:
            print("There is no armor in this room.")
    elif room_command == "look on armor":
        if y == 3:
            print("It seems different with our nation's armor.. it looks more ancient.")
        else:
            print("There is no armor in this room.")
    elif room_command == "look under armor":
        if y == 3:
            print("Key is not under the armor.. we should find another way")
        else:
            print("There is no armor in this room.")
 elif room_command == "look on sword": 
        if y == 3: 
            print("There is nothing on sword.. it's impossible to hide key at the sword")
            print("let's try 'inspect' word to find a key ")
        else: 
            print("There is no sword in this room.")
    elif room_command == "look in sword": 
        if y == 3: 
            print("we can't inspect inside the sword...")
            print("let's try 'inspect' word to find a key ")
        else: 
            print("There is no sword in this room.")
    elif room_command == "look behind sword": 
        if y == 3: 
            print("There is a shield behind the sword.. Let's look at it later")
        else: 
            print("There is no sword in this room.")
    elif room_command == "look under sword": 
        if y == 3: 
            print("There is nothing under the sword.. ")
        else: 
elif room_command == "inspect shield":
        if y == 3:
            print("Would you like to take the shield?")
            shield = input().lower()
            if shield == "yes":
                print("YOU GOT AN ARMOR")
            else: 
                print("No.. let's try next time")
        else:
            print("There is no shield in this room.")
    elif room_command == "look on shield":
        if y ==3: 
            print("The key is not on the shield")
        else: 
            print("It seems like there isn't a shield in this room")
    elif room_command == "look behind shield":
        if y == 3:
            print("The armor is behind the shield.. let's look at it later")
        else: 
            print("THere is no shield in this room.")
    elif room_command == "look in shield":
        if y == 3: 
            print("It's impossible to look in the sheild")
        else: 
            print("No shield in this room")
    elif room_command == "look under shield":
        if y == 3:
            print("Nothing but dust...")
        else: 
            print("It seems like there isn't a shield in this room")
elif room_command == "look on saddle": 
        if y == 3:     
            print("Nothing Here! Let's use other prepositions")
        else: 
            print("There isn't a saddle in this room")
    elif room_command == "look in saddle":
        if y == 3:
            print("Grammarly incorrect")
        else: 
            print("There isn't a saddle in this room")
    elif room_command == "look behind saddle":
        if y == 3:
            print("There is gold behind the saddle!! BUT we need to find the pandora's box :/")
        else: 
            print("There isn't a saddle in this room") 
    elif room_command == "look under saddle":
        if y == 3:
            print("Lots of sands are under saddle.. ")
        else: 
            print("There isn't a saddle in this room") 
    
 elif room_command == "look behind lamp":
        if y == 3:
            print("There is nothing behind of the lamp... only dust")
        else:
            print("Uh-oh! Looks like there isn't a lamp in this room!")
    elif room_command == "look on lamp":
        if y == 3:
            print("Obviously, there is nothing ON the lamp.. We should use other preposition")
        else:
            print("There is no lamp in this room")
    elif room_command == "look under lamp":
        if y == 3:
            print("Some ashes and dusts are under the lamp.. smells are bad")
        else:
            print("There is NO lamp in this room.")
elif room_command == "look in clock":
        if y == 1:
            print("I'm not a mechanic so I don't know how to dismantle it..")
        else:
            print("No key in here.")
elif room_command == "look behind clock":
        if y == 1: 
           print("EMPTY.. There is nothing behind the clock")
        else: 
            print("No clock in this room!")
   
lif room_command == "look in closet":
        if y == 1:
            print("Only a bunch of bones stacked up inside the closet.")
            print(" .-.               .-.     .-.               .-.")
            print("(   `-._________.-'   )   (   `-._________.-'   )")
            print(" >=     _______     =<     >=     _______     =< ")
            print("(   ,-'`       `'-,   )   (   ,-'`       `'-,   ) ")
            print(" `-'               `-'     `-'               `-' ")
        else:
            print("Let's find something else, there isn't a closet in this room")
    elif room_command == "look on closet":
        if y == 1:
            print("It would be too obvious if the key was on top the closet.")
        else:
            print("No closet in this room!")
    elif room_command == "look under closet":
        if y == 1:
            print("All we can see is bloodstain.")
            print("_     _                 _  ")
            print("| |   | |               | | ")
            print("| |__ | | ___   ___   __| |")
            print("| '_ \| |/ _ \ / _ \ / _` |")
            print("| |_) | | (_) | (_) | (_| |")
            print("|_.__/|_|\___/ \___/ \__,_|")
        else:
            print("Looks like there isn't a closet in this room!")
    
elif room_command == "look under oven":
        if y == 2:
            print("Oops. You just made eye contact with the spider.")
            print("          (  ")
            print("           ) ")
            print("          (    ")
            print("    /\  .-'''-.  //\ ")
            print("  // \\/  ,,,  \///\\ ")
            print("  | /\| ,;;;;;, |/\|  ")
            print("   //\\\;-;;;-;///\\ ")
            print("  //  \/   .   \/  \\ ")
            print("( | ,-_| \ | / |_-, |) ")
            print("   //`__\.-.-./__`\\ ")
            print("  // /.-(() ())-.\ \\ ")
            print(" (\ |)   '---'   (| /) ")
            print("    (|           |)")
            print("    \)           (/")
            
        else:
            print("Looks like there isn't a oven in this room!")
