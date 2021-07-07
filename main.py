from Screens.start_screen import StartScreen

from istyles import Istyles
from Screens.styles import *

if __name__ == "__main__":
    try:
        arq = open("config.dat", "r")
        theme = arq.readline()
    except:
        theme = "Light Theme"

    Istyles.register(LightTheme)
    Istyles.register(DarkTheme)

    start = StartScreen(theme)
    start.show()