import os

class Comunicator:
    def __init__(self):
        self.outputMessage=' '
        self.comand=' '

    def write_command(self,comand):
        self.outputMessage += str(os.system(comand))


    def read(self):
        result=self.outputMessage
        self.outputMessage=''
        return result

comunicator=Comunicator()
comunicator.write_command('runas /user:test explorer.exe')
# comunicator.write_command('test')
print(comunicator.outputMessage)