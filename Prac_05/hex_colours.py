

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                  "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                  "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                  "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0",
                  "AntiqueWhite4": "#8b8378", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
print(f"What colour do you want? \n{', '.join(list(COLOUR_TO_CODE.keys()))}")
colour = input("Colour name: ")
while colour != "":
    if colour in COLOUR_TO_CODE:
        print(COLOUR_TO_CODE[colour])
    else:
        print("Try again")
    print(f"What colour do you want? \n{', '.join(list(COLOUR_TO_CODE.keys()))}")
    colour = input("Colour name: ")
