"""
CP1404/CP5632 Practical

"""

CODE_TO_NAME = {
    "#0048ba": "Absolute Zero",
    "#b0bf1a": "Acid Green",
    "#f0f8ff": "AliceBlue",
    "#e32636": "Alizarin crimson",
    "#e52b50": "Amaranth",
    "#ffbf00": "Amber",
    "#9966cc": "Amethyst"
}

print(CODE_TO_NAME)

color_code = input("Enter color code: ")
while color_code != "":
    if color_code in CODE_TO_NAME:
        print(color_code, "is", CODE_TO_NAME[color_code])
    else:
        print("Invalid color code")
    color_code = input("Enter color code: ")

