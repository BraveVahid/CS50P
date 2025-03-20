from sys import argv, exit
from pyfiglet import figlet_format, Figlet

if len(argv) == 1:
    font = "standard"
elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
    font = argv[2]
    if font not in Figlet().getFonts():
        exit("Invalid font")
else:
    exit("Invalid usage")

text = input("Input: ").strip()
print(f"Output:\n{figlet_format(text, font=font)}")
