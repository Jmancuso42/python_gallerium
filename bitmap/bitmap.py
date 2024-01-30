import os
import sys
import time
import json
import logging



def world_bitmap():
    bitmap = '''
    ....................................................................
       **************   *  *** **  *      ******************************
      ********************* ** ** *  * ****************************** *
     **      *****************       ******************************
              *************          **  * **** ** ************** *
               *********            *******   **************** * *
                ********           ***************************  *
       *        * **** ***         *************** ******  ** *
                   ****  *         ***************   *** ***  *
                     ******         *************    **   **  *
                     ********        *************    *  ** ***
                       ********         ********          * *** ****
                       *********         ******  *        **** ** * **
                       *********         ****** * *           *** *   *
                         ******          ***** **             *****   *
                         *****            **** *            ********
                        *****             ****              *********
                        ****              **                 *******   *
                        ***                                       *    *
                        **     *                    *
    ....................................................................
    '''
    return bitmap


def main()
    message = input('Enter text > ')
    if message is None or '': sys.exit()
    #NOTE using a multiline string for the bitmap makes it easier to edit
    for line in world_bitmap().splitlines(): #NOTE this loops over each character in the bit map
        for i, bit in enumerate(line): # #NOTE enumerate returns the index and the value of each character
            if bit == ' ' : #print a space if nothing in order to create the negative space of the bitmap 
                print(' ', end='') #end's the blank space and the line with whitespace
            else:
                #NOTE this will loop around the len of the message and print it, then circle back around to the beginning of the message and print it again
                #print char from the mnessage
                print (message[i % len(message)], end='') #this works by using the modulus operator to get the remainder of the index divided by the length of the message
        print() #NOTE this prints a new line after each line of the bitmap is printed
        
        
        '''What happens if the player enters a blank string for the message?
Does it matter what the nonspace characters are in the bitmap variable’s string?
What does the i variable created on line 45 represent?
What bug happens if you delete or comment out print() on line 52?'''