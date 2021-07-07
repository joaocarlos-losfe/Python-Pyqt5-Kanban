from Screens.start_screen import StartScreen

if __name__ == "__main__":
    try:
        arq = open("config.dat", "r")
        theme = arq.readline()
    except:
        theme = "Light Theme"

    start = StartScreen(theme)
    start.show()