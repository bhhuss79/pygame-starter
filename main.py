import time
from playsound import playsound 
def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 


def wholegame1():
  print("Hello oliver, you are about to wake up to start your journey")#The code shows these texts 
  print("The sound of your alarm startles you, you wake up drenched in sweat.")
  time. sleep(7.)#wait for seven seconds 
  print("You get dressed for work and head to your car.")
  time.sleep(5.)#wait for 5 seconds 
  clear()#clear everything in the terminal
  print("  ______ \n /|_||_\`.__\n(   _    _ _\ \n=`-(_)--(_)-' )") # this is a car
  time.sleep(3.)
  print("Your car is not working, you try one more time...")
  time.sleep(3.)
  clear()
  print("   (`  ).                   _  \n   (     ).              .:(`  )`.  \n  _(       '`.          :(   .    ) \n  .=(`(      .   )     .--  `.  (    ) ) \n  ((    (..__.:'-'   .+(   )   ` _`  ) ) \n      `(       ) )       (   .  )     (   )  ._    \n )      ` __.:'   )     (   (   ))     `-'.-(`  ) \n )  )  ( )       --'       `- __.'         :(      )) \n .-'  (_.'          .')                    `(    )  )) \n (_  )                     ` __.:' \n    --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--. \n ") #this is smoke 
  time.sleep(3.)
  print("Your car doesn't start! The only way to go to work is to walk you can't be late to work")
  choice = input("You keep walking and remember there is a shortcut in the forest. Do you A) go in the forest because its faster or B) go the normal way because its safer but longer?")#asks a question so the user can type in an answer 
  if choice == "A" :
      print("As you are walking trough the forest, you notice that the grass is very tall, no one has been here for a while... ")
      print("As you are walking, you hear a stick click behind you as if someone stepped on it. Your mind thinks: RUN! So you run as fast as you can never looking back.")
      time.sleep(10.)#wait for 15 seconds so you can read the text above 
      clear()
      print (" _O/ \n  \ \n  /\_ \n \  ` \n  ` \n  ")  #this is a person running 
      time.sleep(2.) # wait for 300 milliseconds
      clear()
      print ("   , \n  / \n `\_\ \n  \ \n /O\ \n  ")#a person running
      time.sleep(2.)  #wait for 300 milliseconds 
      print ("You get out of the forest. You feel so blessed that whatever that was didn't catch you, you are now on the road and you keep walking, terified")

            
  else: 
        print("You keep walking on the road, and notice that no one is on the road, its just you, where is everybody...")
        
  time.sleep(5.)#wait for 5 seconds so the person can read the text 


  clear()#clear the terminal 
  choice2 = input("You keep walking, and find out that people have been here recently, there are wet stains neaer the gas station, do you A) ingnore it or B) try to get some more clues...?")#asking a question that the user types in a answer 
  if choice2 == "A" :
    print("You ignore it and keep walking.")
  else:
    print ("You go and try to find something at the gas station that would make sense")
    print ("You find a wierd chucky doll that has smells terrible")
    print("Ew what is that smell, you get the chills....")
    time.sleep(7.)#wait for seven  seconnds 
    clear()
    time.sleep(.300)
    print("""       ...----....
                          ..-:"''         ''"-..
                        .-'                      '-.
                      .'              .     .       '.
                    .'   .          .    .      .    .''.
                  .'  .    .       .   .   .     .   . ..:.
                .' .   . .  .       .   .   ..  .   . ....::.
              ..   .   .      .  .    .     .  ..  . ....:IA.
              .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
            .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
            '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
            .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
          .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
          ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
          .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
        .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
        :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
        ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
        ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
        :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
        '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
          :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
        .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
        ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
      : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
      :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
      'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
        "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
          :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
          :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
          :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
          :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
          :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
          ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
            V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
              'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
              I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
              .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
              :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
              :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
              ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
              ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
              :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
              ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
                "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
                ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
                  "::....::.:::..:..::IIIIIHHHHMMMHHMV"
                    "::.::.. .. .  ...:::IIHHMMMMHMV"
                      "V::... . .I::IHHMMV"'
                        '"VHVHHHAHHHHMMV:"'""")#this is a jumpscare
    playsound("assets/ghost.wav")#play the scary sound 
    print("Woah, you just had a major wierd flashback about that movie, you countinue walk")
  time.sleep(3.)
  clear()
  print("As you keep walking you keep hearing these strange sounds, from all directions, it sounds like a little girl. ")
  print("You think its just your mind messing with you because you watched a horro movie last night...")
  print ("You remember that you need to eat breakfast! Your starving and you find this grocery store and walk in... ")
  print ("No ones here, you decide to steal because you can't take it anymore.")
  print ("You go and try to get some lunchables, as your reaching for the lunchables in the creepy isle, you feela tap on the back and something saying: I've been looking for you..")
  print ("you turn around....")
  time.sleep(17.)
  clear()
  time.sleep(2.)
  print ("Nothing, thats confusing")
  print ("You turn back and grab the luncables.")
  time.sleep(3.)
  clear()
  print(""""███████████▓▓▓▓▓▓▓▓▒░░░░░▒▒░░░░░░░▓█████
  ██████████▓▓▓▓▓▓▓▓▒░░░░░▒▒▒░░░░░░░░▓████
  █████████▓▓▓▓▓▓▓▓▒░░░░░░▒▒▒░░░░░░░░░▓███
  ████████▓▓▓▓▓▓▓▓▒░░░░░░░▒▒▒░░░░░░░░░░███
  ███████▓▓▓▓▓▓▓▓▒░░▒▓░░░░░░░░░░░░░░░░░███
  ██████▓▓▓▓▓▓▓▓▒░▓████░░░░░▒▓░░░░░░░░░███
  █████▓▒▓▓▓▓▓▒░▒█████▓░░░░▓██▓░░░░░░░▒███
  ████▓▒▓▒▒▒░░▒███████░░░░▒████░░░░░░░░███
  ███▓▒▒▒░░▒▓████████▒░░░░▓████▒░░░░░░▒███
  ██▓▒▒░░▒██████████▓░░░░░▓█████░░░░░░░███
  ██▓▒░░███████████▓░░░░░░▒█████▓░░░░░░███
  ██▓▒░▒██████████▓▒▒▒░░░░░██████▒░░░░░▓██
  ██▓▒░░▒███████▓▒▒▒▒▒░░░░░▓██████▓░░░░▒██
  ███▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░███████▓░░░▓██
  ███▓░░░░░▒▒▒▓▓▒▒▒▒░░░░░░░░░██████▓░░░███
  ████▓▒▒▒▒▓▓▓▓▓▓▒▒▓██▒░░░░░░░▓███▓░░░░███
  ██████████▓▓▓▓▒▒█████▓░░░░░░░░░░░░░░████
  █████████▓▓▓▓▒▒░▓█▓▓██░░░░░░░░░░░░░█████
  ███████▓▓▓▓▓▒▒▒░░░░░░▒░░░░░░░░░░░░██████
  ██████▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▓████████
  ██████▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░▓██████████
  ██████▓▓▓▓▒▒██████▒░░░░░░░░░▓███████████
  ██████▓▓▓▒▒█████████▒░░░░░░▓████████████
  ██████▓▓▒▒███████████░░░░░▒█████████████
  ██████▓▓░████████████░░░░▒██████████████A
  ██████▓░░████████████░░░░███████████████
  ██████▓░▓███████████▒░░░████████████████
  ██████▓░███████████▓░░░█████████████████
  ██████▓░███████████░░░██████████████████
  ██████▓▒██████████░░░███████████████████
  ██████▒▒█████████▒░▓████████████████████
  ██████░▒████████▓░██████████████████████
  ██████░▓████████░███████████████████████
  ██████░████████░▒███████████████████████
  █████▓░███████▒░████████████████████████
  █████▒░███████░▓████████████████████████
  █████░▒██████░░█████████████████████████
  █████░▒█████▓░██████████████████████████
  █████░▓█████░▒██████████████████████████
  █████░▓████▒░███████████████████████████
  █████░▓███▓░▓███████████████████████████
  ██████░▓▓▒░▓████████████████████████████
  ███████▒░▒██████████████████████████████
  ████████████████████████████████████████
  ████████████████████████████████████████""")#this is a jumpscare 
  playsound("assets/Scream 4 (1).wav")#play the sound 
  print("Monster: I have caught, you! You cannot do anything to stop me now!")
  choice3 = input("You get caught, do you A) fight back or B) surrender?")
  if choice3 == "A" : #the if statement gives the user a question 
    print("You grab a can of beans and throw it at the monster. He gets knocked out. You run as quickly as you can out of the store")
    time.sleep(3.)
    clear()
  else: 
    print("As your apoligizing for whatever you did, you distract the monster by throwing something and pretending it wasnt you, you escape while he is figuring out what happened.")
    time.sleep(4.)
    clear()

  print("As your running your feet freeze to the ground, you can't move!")
  time.sleep(3.)#tells the code to wait for 3 seconds 
  clear()
  print("You try and try to move but you can't, you see a foggy figure come right at you...!")
  time.sleep(5.)
  clear()
  playsound("assets/Scream 3.wav")
  print("That noise scared you to death! But you can't see anything your so confused and terrified and just want to go to work!")
  time.sleep(5.)
  clear()
  print("""__________________________________________________
  __________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________________
  ______________¶¶¶¶_____________¶¶¶¶¶______________
  ___________¶¶¶_____________________¶¶¶¶___________
  ________¶¶¶¶__________________________¶¶¶_________
  _______¶¶_______________________________¶¶¶_______
  ______¶¶__________________________________¶¶______
  ____¶¶_____________________________________¶¶_____
  ____¶________________________________________¶____
  ___¶¶________________________________________¶¶___
  __¶¶_____________¶¶¶__________________________¶___
  ___¶___________¶¶_____________________________¶¶__
  ___¶___________¶________________¶¶¶___________¶¶__
  ___¶_____¶¶_¶¶_¶¶¶¶¶_¶____________¶¶¶__________¶__
  ___¶_________¶___¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶_________¶__
  ___¶¶______¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶_¶¶____¶¶¶_
  ___¶¶____¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶__¶¶__
  ___¶____¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶___
  __¶¶___¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶___
  ____¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶____
  ______¶¶¶¶¶¶¶___¶¶_____¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶____
  ______¶__¶¶¶____¶¶¶___________________¶¶¶¶¶¶¶_____
  _____¶¶________¶¶¶¶¶¶__¶________________¶¶¶_______
  _____¶¶______¶¶¶____¶¶¶¶______________¶¶¶¶________
  ______¶¶______¶_______¶¶_________¶¶¶¶¶¶¶¶¶________
  _______¶¶¶¶¶_______________¶_¶¶¶¶¶¶¶¶¶¶¶¶¶________
  ___________¶¶¶____¶¶¶¶_¶¶_¶¶¶___¶¶¶¶¶___¶¶________
  ____________¶¶¶¶¶_¶__¶¶_¶_¶_¶____¶¶_____¶_________
  _____________¶_____________¶¶_____¶_____¶_________
  ______________¶¶¶¶¶_¶¶¶¶¶¶________¶¶____¶_________
  ____________________¶¶¶¶¶¶_________¶____¶_________
  _____________________¶¶_¶¶_________¶¶___¶¶________
  ______________________¶¶¶¶¶_________¶____¶________
  _______________________¶¶¶¶¶_______¶¶____¶¶_______
  _______________________¶¶¶¶¶______¶_¶_____¶_______
  _______________________¶_¶¶¶_____¶__¶¶____¶_______
  _______________________¶¶¶¶¶____¶¶__¶¶___¶________
  _______________________¶¶¶¶¶__¶¶¶__¶¶___¶_________
  ________________________¶¶¶¶¶¶¶__¶¶¶___¶¶_________
  _________________________¶¶_____¶¶¶____¶__________
  ____________________________¶¶¶¶______¶___________
  ______________________________¶¶_____¶¶___________
  _______________________________¶¶¶¶¶¶¶____________
  __________________________________________________""")#this is a jumpscare
  playsound("assets/Scream 5.wav")#play the scary sound
  time.sleep(5.)
  print("You wake up, and are so happy that what you just experienced was a nightmare. ")
  print("You get up to work, and when you go to your car your car doesn't start.")
  print("You find the same doll in the passengers seat as the one in your dream")
  print("The end ")#tell the user that it was all a dream, but you see the same doll in real life.
  choice4 = input("Play again? [yes or no]")
  if choice4 == "yes" :
    print("Ok.")
    time.sleep(2.)
    wholegame1()
  else: 
    print("Thanks for playing!")

wholegame1()