# Random Password Generator
import random

lower = "abcdefghijklmnopqrstuvwXyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}();*-/_"

all = lower + upper + numbers + symbols

# update length value to reduce or increase password length 
length = 22
password = "".join(random.sample(all, length))

print(password)