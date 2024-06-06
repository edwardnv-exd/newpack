class Hello (object):
    def __init__ (self, name):
        self.name = name
    def say_hello (self):
        print ("Hello " + str (self.name))