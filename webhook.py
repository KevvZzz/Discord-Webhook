print("""
                                                                                                 
                              _ _ _     _   _____         _                
                             | | | |___| |_|  |  |___ ___| |_ 
                             | | | | -_| . |     | . | . | '_|
                             |_____|___|___|__|__|___|___|_,_|
               
                                       Made by Kev
                                     Github: keptz
""")

#imports
from dhooks import Webhook
import time
import os

#prompts
message = input("What do you want to send?: ")
webhookurl = Webhook(input("Enter webhook: "))

webhookurl.send(message)
print("------------------------------------------------")
time.sleep(2)
os.system('call start.bat')
