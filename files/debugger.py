from termcolor import colored

class console:
    def __init__(self, error_color:str="red", success_color:str="green", warning_color:str="yellow", info_color:str="blue", text_color:str="cyan"):
        """Sets the colores for all errors.

        Args:
            error_color (str, optional): The color for errors. Defaults to "red".
            success_color (str, optional): The color for successes. Defaults to "green".
            warning_color (str, optional): The color for warnings. Defaults to "yellow".
            info_color (str, optional): The color for infos. Defaults to "blue".
            text_color (str, optional): The color for the general text color. Defaults to "cyan".
        """
        self.__error_color = error_color
        self.__success_color = success_color
        self.__warning_color = warning_color
        self.__info_color = info_color
        self.__text_color = text_color
    def error(self, text: str):
        """Prints an error message in a non MegaShell style.

        Args:
            text (str): The text to print.
        """
        text = text.replace("\n", colored("\n > "))
        print(colored("Error: ", self.__error_color) + colored(text, self.__text_color))
