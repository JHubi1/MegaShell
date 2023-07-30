from termcolor import colored

class console:
    def __init__(self, error_color:str="red", success_color:str="green", warning_color:str="yellow", info_color:str="blue", text_color:str="cyan"):
        self.__error_color = error_color
        self.__success_color = success_color
        self.__warning_color = warning_color
        self.__info_color = info_color
        self.__text_color = text_color
    def error(self, text: str):
        text = text.replace("\n", colored("\n > "))
        print(colored("Error: ", self.__error_color) + colored(text, self.__text_color))
