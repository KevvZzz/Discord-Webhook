print("""
                                                                                                 
                              _ _ _     _   _____         _                
                             | | | |___| |_|  |  |___ ___| |_ 
                             | | | | -_| . |     | . | . | '_|
                             |_____|___|___|__|__|___|___|_,_|
               
                                       Made by Kev
                                     Github: KevvZzz
""")

#imports
from dhooks import Webhook
import time
import os

#prompts
message = input("What do you want to send?: ")
webhookurl = Webhook(input("Enter webhook: "))

#send message
webhookurl.send(message)

#print
print("------------------------------------------------")

#delay for 2 seconds
time.sleep(2)

#call start.bat
os.system('call start.bat')
