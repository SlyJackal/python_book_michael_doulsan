class TV():

    MAX_VOLUME = 14
    MAX_CHANNEL = 100
    MIN_CHANNEL = 1

    def __init__(self, volume = 7, chanel = 1):
        self.volume = volume
        self.chanel = chanel
        self.save_volume = 0
    
    def press_button(self, choice):
        choice = choice.lower()
        try:
            self.channel_jump(int(choice))
        except:
            if choice == '+':
                self.volume_level(1)
            elif choice == '-':
                self.volume_level(-1)
            elif choice == 'm':
                self.mute()
            elif choice == 'n':
                self.chanels_change(1)
            elif choice == 'p':
                self.chanels_change(-1)
    
    def volume_level(self, a):
        self.volume += a
        if self.volume < 0:
            self.volume = 0
        elif self.volume > self.MAX_VOLUME:
            self.volume = self.MAX_VOLUME
        print(f'\n\nSet volume: {self.volume}\n\n')      

    def mute(self):
        if self.volume != 0:
            self.save_volume = self.volume 
            self.volume = 0
            print('\n\nMute\n\n')
        else:
            self.volume = self.save_volume
            print(f'\n\nSet volume: {self.volume}\n\n')
        
    def chanels_change(self, a):
        self.chanel += a
        if self.chanel > self.MAX_CHANNEL:
            self.chanel = a
        elif self.chanel < self.MIN_CHANNEL:
            self.chanel = self.MAX_CHANNEL
        print(f'\n\nSet channel: {self.chanel}\n\n')

    def channel_jump(self, a):
        if self.MIN_CHANNEL < a < self.MAX_CHANNEL:
            self.chanel = a
            print(f'\n\nSet channel: {self.chanel}\n\n')
        else:
            print(f'\n\nOut of channels range. You still watching channel number - {self.chanel}!\n\n')

def main():
    tv_control = TV()
    print(f"\nI'm turn on!\nChannel - {tv_control.chanel}\nVolume set - {tv_control.volume}")
    choice = None 
    while choice != 'Off':
        print('''
TV menu:
N : next channel
P : previous channel
+ : turn up the volume
- : turn down the volume
M : mute
Number : chosse chanel (1 - 100)
Turn off - Off
''')
        choice = input('Your choice: ')
        tv_control.press_button(choice)
    else:
        print("\n\nGood bye! I'm off!\n\n")

main()