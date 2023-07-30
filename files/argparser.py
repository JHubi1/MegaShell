class __argparser:
    def parse(self, args: list) -> tuple:
        """Parses a list of strings to a tuple.

        Args:
            args (list): A list of strings to parse.

        Returns:
            tuple: The parsed values.
        """
        finishedText = {}
        otherArguments = []
        args.append("")
        cache1 = ""
        cache2 = ""
        string = ""
        name = ""
        num = -1
        for arg in args:
            arg = str(arg)
            otherArguments.append(arg)
            if num == 2 and string == "":
                finishedText[name] = cache2
                name = ""
                num = -1
                otherArguments.remove(cache2)
            if (arg.startswith("'") or arg.startswith('"')) and string == "":
                if arg.startswith("'"): string = "'"
                else: string = '"'
            if string == "'" or string == '"':
                cache1 += arg
                if arg.endswith(string):
                    finishedText[name] = cache1.replace(string, "")
                    string = ""
                    name = ""
                    cache1 = ""
                    num = -1
            if arg.startswith("--") and string == "":
                if name != "":
                    finishedText[name] = True
                name = arg.replace("--", "")
                num = 0
                otherArguments.remove(arg)
            if num != -1:
                num += 1
                cache2 = arg
        try: otherArguments.remove("")
        except KeyError: pass
        try: finishedText.pop("")
        except KeyError: pass
        return finishedText, otherArguments
argparser = __argparser()
