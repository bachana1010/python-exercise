
import random

I="""
****************
*              *
*      *       *
*              *
****************
"""
II="""
****************
*  *           *
*              *
*         *    *
****************
"""

III="""
****************
*  *           *
*      *       *
*          *   *
****************
"""

IV="""
****************
*   *       *  *
*              *
*   *       *  *
****************
"""

V="""
****************
*   *       *  *
*       *      *
*   *       *  *
****************
"""
VI="""
****************
*   *       *  *
*   *       *  *
*   *       *  *
****************
"""

dices= [I,II,III,IV,V,VI]
welcome_text=""""
*****************************
*       welcome             *
*   this is a game named    *  
*       roll dice           *
******************************

"""

print(welcome_text)
while True:
    roll_again=input("play again?")

    if roll_again=="no":
        print("finish")
        break
    dice_index=random.randint(0,5)
    print(dices[dice_index])


