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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

## CODE START ##
print("You wake up one beautiful morning, the usual warm light of the shining sun gently pushing you down into your bedroll and the soft dew giving you a refreshing first breath.")
print("You look around you and notice something; You can't seem to remember which direction you were going on the adjoining road. As you pack your things up, you're left with one unfortunate choice:")
firstchoice = input("Should you go left, or right?\n").lower()

if firstchoice == "left":
  print("You steady on down the path with things looking unfamiliar, you regail in your choice to go this way")
  secondchoice = input("After a few hours, you end up at a little ferry crossing. With no one in sight, and the opposite shore within reasonable distance, you ask yourself, should you swim or wait?\n").lower()
  if secondchoice == "wait":
    print("You sit patiently on the stool close to the pier, waiting for the ferry to return")
    print("About an hour later, the ferryman finally crossed back to pick you up. Although slightly aggravated, he quickly explains how he needed to go into town to fetch medicine for his daughter. He thanks you for your patience and offers you free passage")
    print("In your kind heart, you offer the kind man the usual tariff after crossing, thank him and wish him and his family well.")
    print("after resuming your journey, you fall upon an old destitute garrisson. Deciding to inspect it further, you end up in a small room with 3 different door, a red one, a blue one and a yellow one")
    thirdchoice = input("red, yellow or blue?\n").lower()
    if thirdchoice == "yellow":
      print("You open the yellow door to find a treasure chest filled with riches! A mule conveniently appears next to it and you're able to pack it all and bring it home. How fucking convenient?")
      print("You won the game!")
    elif thirdchoice == "red":
      print("You pull the handle of the door and are promptly met with a hail of arrows from all sides; Your red blood sprays yet another layer on the door.")
      print("GAME OVER")
    else:
      print("As you start to open the blue door, a troll awaiting on the other side runs you through and crushes your head under his mighty stomp.")
      print("GAME OVER")
  else:
    print("As you begin to make your way into the river, you notice the current to be slightly stronger than expected. Commiting to your decision, you press on only to be overwhelmed at the middle of the river. You're swept away and drown.")
    print("GAME OVER")
else:
  print("After hours of trekking, you end up back home. GAME OVER")