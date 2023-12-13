import os
import json
import time

nombre_archivo = os.path.join(os.path.dirname(__file__), 'config.json')

with open(nombre_archivo, 'r') as archivo_json:
    config = json.load(archivo_json)

# print(config)

class App:
    def __init__(self):
        self.printBanner()

        os.system("title Delete Temp and Trash archives")
        # time.sleep(1)
        os.system("rd %temp% /s /q")
        os.system("rd temp /s /q")
        os.system("ipconfig /flushdns")
        os.system("wuauclt /detectnow")
        os.system("wuauclt /updatenow")
        os.system("wuauclt /detectnow /updatenow")

        os.system("")

    def printBanner(self):
        print(
            """
██████╗  █████╗  ██████╗██╗ █████╗       █████╗ ██╗      ███████╗ █████╗ ███╗   █╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██║██╔══██╗     ██╔══██╗██║      ██╔════╝██╔══██╗████╗ ██║██╔═══  ██╔══██╗
██████╦╝███████║╚█████╗ ██║██║  ═╝█████╗██║  ╚═╝██║      █████╗  ███████║██╔██╗██║█████╗  ██████╔╝
██╔══██╗██╔══██║ ╚═══██╗██║██║  █╗╚════╝██║  ██╗██║      ██╔══╝  ██╔══██║██║╚████║██╔══╝  ██╔══██╗
██████╦╝██║  ██║██████╔╝██║╚█████╔╝      ╚█████╔╝███████╗███████╗██║  ██║██║ ╚███║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝ ╚════╝        ╚════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝

Github : https://github.com/MangyGuitar/Basic-cleaner

------------------------------------------------------------------------
"""
        )

if __name__ == "__main__":
    app = App()
