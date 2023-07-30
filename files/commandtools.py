from .internal import tools as t
from .internal import outputLibrary as ol
from .help import info as ol

class __commandtools:
    def parse(self, extra: dict, *args, codeOnWrongArguments="") -> tuple | str:
        argsDone = []
        extra = extra["extra"]
        try:
            for arg in args:
                if arg == "":
                    argsDone.append(extra[0])
                    extra.pop(0)
                else:
                    argsDone.append(arg)
        except IndexError:
            return False
        except:
            return False
        if len(argsDone) == 1:
            argsDone = str(argsDone[0])
        return argsDone
commandtools = __commandtools()
