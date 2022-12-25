import random

def get_response(message):

    if message.lower() == "hello":
        return "SHUT UP."

    if message.lower() == "!help":
        return "`This is a help message.`"
        
    return "I don't understand."
