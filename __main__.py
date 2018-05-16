from controller import Controller

c = Controller()
text = ''
while(text != 'exit'):
    text = input('hey, command me boy\n')
    c.process_command(text)
