import pyautogui
from time import sleep
from random import randint

x = 50   #how many messages or comments you want to send
y = 0
finish = True

def name():
    """generates random names"""

    nameList = ["Baby", "Shona", "Honey", "Jaan", "Wifey"]   #list of names (change according to your requirement)
    rand_name = nameList[randint(0, len(nameList) - 1)]      #traverse names randomly for n, from 0 to (n-1)

    return rand_name    #return the random name it just generated 
 


while finish:      #forever loop
   # pyautogui.typewrite(f"I love you {name()}")  
    pyautogui.typewrite(f"I love you {name()}")
    sleep(.600)                        #A bit delay of 600 ms
    pyautogui.typewrite("\n")          #New line, here 'Enter' to send text
    sleep(0.600)                         #delay of 2 seconds
    y = y + 1
    x = x - 1         #decrement x value by 1I love you
    if y==10:
        finish == False

    if x == 0:       
        break         #get out of the loop and finishI love you {name()}
    