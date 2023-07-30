from .internal import commands

class __info:
    def listAll(self) -> list:
        """Returns a list of all commands.

        Returns:
            list: The list os all commands.
        """
        finishedText = []
        for command in commands.commands:
            finishedText.append(command)
        return finishedText
    def get(self, key: str) -> str | bool:
        """This function returns the help text for a command.

        Args:
            key (str): The key of the command.

        Returns:
            str | bool: The value or `False` if the command does not exist.
        """
        if key in commands.commands_meta:
            value = str(commands.commands_meta[key]["doc"][0])
            value = value.replace("v1", "").replace("v2", "").replace("disable", "").replace(",", "").strip()
            return value.strip()
        else:
            return False
info = __info()
