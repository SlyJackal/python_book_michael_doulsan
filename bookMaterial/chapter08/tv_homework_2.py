class tv(object):
    a = None

    def __init__(self, volume = 7, chanel = 1):
        self.volume = volume
        self.chanel = chanel
    
    def volume_level(self, a):
        self.volume += a
        if self.volume < 0:
            self.volume = 0
        elif self.volume > 14:
            self.volume = 14
        if self.volume == 0:
            print('\n\nMute\n\n')
        else:
            print(f'\n\nSet volume: {self.volume}\n\n')

    def chanels_change(self, a):
        self.chanel += a
        if self.chanel > 100:
            self.chanel = a
        elif self.chanel < 1:
            self.chanel = 100
        print(f'\n\nSet channel: {self.chanel}\n\n')

    def channel_jump(self, a):
        if 1 < a < 100:
            self.chanel = a
            print(f'\n\nSet channel: {self.chanel}\n\n')
        else:
            print(f'\n\nOut of channels range. You still watching channel number - {self.chanel}!\n\n')

def main():
    tv_control = tv()
    print(f"\nI'm turn on!\nChannel - {tv_control.chanel}\nVolume set - {tv_control.volume}\n")
    choice = None 
    while choice != 'Off':
        choice = input('TV menu:\nN : next channel\nP : previous channel\n+ : turn up the volume\n- : turn down the volume\nM : mute\nNumber : chosse chanel (1 - 100)\nTurn off - Off\n\nYour choice:\t').lower()
        try:
            tv_control.channel_jump(int(choice))
        except:
            if choice == '+':
                tv_control.volume_level(1)
            elif choice == '-':
                tv_control.volume_level(-1)
            elif choice == 'm':
                tv_control.volume_level(-tv_control.volume)
            elif choice == 'n':
                tv_control.chanels_change(1)
            elif choice == 'p':
                tv_control.chanels_change(-1)
    else:
        print("\n\nGood bye! I'm off!\n\n")

main()