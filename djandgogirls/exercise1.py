print ('Hello World')

if 3 > 2:
    print('it works')

name = 'Abdul'

if name == 'Ola':
    print ('Hey Ola')
elif name == 'Sonja':
    print ('Hey Sonja')
else:
    print ('Hey Sonja')

volume = -1220

if volume < 20:
    print("It's kinda quiet")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties!")
elif 80 <= volume < 100:
    print("It's a bit loud")
else:
    print("I'm deaf")

#change the volume if it's too loud

if volume < 20 or volume > 80:
    volume = 50
    print("That's better")


def hi(name):
    print('Hi ' + name + '!')

girls = ['A','B','C','D','E']
for name in girls:
    hi(name)
    print('Next girl')

for i in range (1,6):
    print(i)
