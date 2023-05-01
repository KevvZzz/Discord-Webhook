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

#prompts
message = input("What do you want to send?: ")
webhookurl = Webhook(input("Enter webhook: "))

#send message
webhookurl.send(message)
print(f"sent: {message}")