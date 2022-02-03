# Iss game mein aap ek alien se fight karoge. Game mei alien
# ka stamina 10 se shuru hoga. Aapko uska stamina khatam karna 
# hai yaani ki 0 karna hai. Aisa karne ke liye aap alien ke against 
# in 4 options mei se koi option use kar sakte ho.

# 1
# Hit
# 2
# Attack
# 3
# Fight
# 4
# Run
# Hit aur attack karne se alien ka stamina 0-9 ke beech kisse random 
# number se kam hoga. Har bar stamina kam karne par report() se report 
# aayegi jo alien ke stamina ke hisab se uski condition bateygi.

 # allows you to generate a random number

# # variables for the alien
# alive = True
# stamina = 10
# main function - accepts your input for fight with the alien

from random import randint
alive=True
stamina=10
def report(stamina):
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:    
        print ("That's it! The alien is finished!")
report(int(input("enter any thing:")))
def fight(stamina): 
    while stamina > 0:
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run:")
        if "hit" in response or "attack" in response:
            less = randint(0, stamina)
            stamina-= less 
            report(stamina)
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
    return False        
alive = fight(stamina)
if alive == True:
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n")
    # print ("A threatening alien wants to fight you!\n")
