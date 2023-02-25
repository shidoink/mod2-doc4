class stringGetter():
    def __init__(self, string=''):
        self.string= string

    def get_String(self):
        self.string= input("Give us a string pretty please")

    def print_String(self):
        print(self.string.upper())

my_string= stringGetter()

my_string.get_String()
my_string.print_String()
        