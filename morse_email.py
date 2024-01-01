#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SANJANA IAHVATHI
#
# Created:     27-05-2022
# Copyright:   (c) SANJANA IAHVATHI 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
import smtplib


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

# Function to decrypt the string
# from morse to english


def decrypt(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]

				citext = ''

	return decipher

# Hard-coded driver function to run the program

def main():
    while True :
        query = input('''DO YOU WANT TO SEND AN EMAIL OR DECODE AN EMAIL?
        IF YOU WANT TO SEND AN EMAIL,PLEASE ENTER SEND
        IF YOU WANT TO DECODE AN EMAIL,PLEASE ENTER DECODE : ''')



        if (query=="send"):
                message=input("PLEASE ENTER YOUR MESSAGE : ")
                text=encrypt(message.upper())
                receivers = input("PLEASE PROVIDE EMAIL ID TO WHOM YOU WANT TO SEND A MESSAGE : ")
                smtp = smtplib.SMTP('smtp.gmail.com', 587)
                smtp.starttls()
                smtp.login("ambicaiahvathi@gmail.com","ambu31@2003")
                smtp.sendmail("ambicaiahvathi@gmail.com", receivers,text)
                smtp.quit()
                print ("Email sent successfully!")


        elif (query=="decode"):
            morse_code=input("WHAT DO YOU WANT TO DECODE?")
            output=decrypt(morse_code)
            print('''YOUR MESSAGE IS : ''' ,output)
        else:
            break
        confirmation_text = input('''IS THERE ANYTHING WE CAN HELP YOU?
                                  YES/NO :
                                    ''')
        if (confirmation_text=="yes"):
            continue
        elif(confirmation_text=="no"):
            break

# Executes the main function
if __name__ == '__main__':
	main()


