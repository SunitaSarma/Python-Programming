# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:41:52 2024

@author: sarma
"""

import random
import string

def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage: generate a password of length 12
password = generate_password()
print("Generated password:", password)