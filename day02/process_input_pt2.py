import sys
from advancedKeyPad import advancedKeyPad

keys = advancedKeyPad()

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    text = f.readlines()

for line in text:
    for direction in line:
        keys.move(direction)
    keys.press_button()

print keys.buttonsPressed
