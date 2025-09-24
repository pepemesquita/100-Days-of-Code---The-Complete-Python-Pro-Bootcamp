
print('''
*******************************************************************************

          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your missions is to find the treasure")
print("You' re at a cross road. Where do you want to go?")

response = input("Type 'left' or 'right': ")

if response == "Left" or response == "left":
    print("You've come to a lake. There an island in the middle of the lake")
    response = input("Type 'wait' to wait for a boat. Type 'swin' to swin across: ")

    if response == "Wait" or response == "wait":
        print("You found three doors ahead with different colours, which you choose?")
        response = input("Type 'red' to choose the Red Door, type 'yellow' to the Yellow Door or type 'blue' to choose the Blue Door: ")

        if response == "Yellow" or response == "yellow":
            print("Congrats, you won!")
        else:
            print("You died.")
    else:
        print("You died")
else:
    print("You died")