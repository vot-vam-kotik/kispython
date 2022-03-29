import traceback

logs_file = open("logs.txt", 'w')
logs_file.write("-" * 30 + '\n')
logs_file.close()

def log(method):
    def wrapper(*args, **kwargs):

            try:
                a = method(*args, **kwargs)
                return a

            except Exception as e:
                logs_file = open("logs.txt", 'a')

                tr = traceback.format_exc(limit=1, chain=False)
                c = args[0].__class__.__name__

                logs_file.write(f"CLASS:    \t{c}\n\n")
                logs_file.write(f"TRACEBACK:\t{tr}\n")
                logs_file.write(f"ERROR:    \t{e}\n")
                logs_file.write("-" * 30 + '\n')
                logs_file.close()

                return tr

    return wrapper


class Calculator:

    @log
    def __init__(self):
        pass

    @log
    def divide(self, a, b):
        return a / b

class Joiner:

    @log
    def __init__(self):
        pass

    @log
    def join(self, a, b):
        return a + b