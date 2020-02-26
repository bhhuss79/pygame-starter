import time

def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
print("Hello oliver, you are about to wake up to start your journey")
print("The sound of your alarm startles you, you wake up drenched in sweat.")
time. sleep(7.)
print("You get dressed for work and head to your car.")
time.sleep(5.)
clear()
print("  ______ \n /|_||_\`.__\n(   _    _ _\ \n=`-(_)--(_)-' )") # this is a car
time.sleep(3.)
print("Your car is not working, you try one more time...")
time.sleep(3.)
clear()
print("   (`  ).                   _  \n   (     ).              .:(`  )`.  \n  _(       '`.          :(   .    ) \n  .=(`(      .   )     .--  `.  (    ) ) \n  ((    (..__.:'-'   .+(   )   ` _`  ) ) \n      `(       ) )       (   .  )     (   )  ._    \n )      ` __.:'   )     (   (   ))     `-'.-(`  ) \n )  )  ( )       --'       `- __.'         :(      )) \n .-'  (_.'          .')                    `(    )  )) \n (_  )                     ` __.:' \n    --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--. \n ")
time.sleep(3.)
print("Your car doesn't start! The only way to go to work is to walk you can't be late to work")
choice = input("You keep walking and remember there is a shortcut in the forest. Do you A) go in the forest because its faster or B) go the normal way because its safer but longer?")
if choice == "A" :
     print("As you are walking trough the forest, you notice that the grass is very tall, no one has been here for a while... ")
     print("As you are walking, you hear a stick click behind you as if someone stepped on it. Your mind thinks: RUN! So you run as fast as you can never looking back.")
     time.sleep(15.)#wait for 15 seconds so you can read the text above 
     clear()
     print (" _O/ \n  \ \n  /\_ \n \  ` \n  ` \n  ")  #this is a person running 
     time.sleep(1.) # wait for 300 milliseconds
     clear()
     print ("   , \n  / \n `\_\ \n  \ \n /O\ \n  ")
     time.sleep(1.)  #wait for 300 milliseconds 
     print ("You get out of the forest. You feel so blessed that whatever that was didn't catch you, you are now on the road and you keep walking, terified")

          
else: 
       print("You keep walking on the road, and notice that no one is on the road, its just you, where is everybody...")
      
time.sleep(5.)


clear()
choice2 = input("You keep walking, and find out that people have been here recently, there are wet stains neaer the gas station, do you A) ingnore it or B) try to get some more clues...?")
if choice2 == "A" :
  print("You ignore it and keep walking.")
  print("As you keep walking you keep hearing these strange sounds, from all these")
  print
    