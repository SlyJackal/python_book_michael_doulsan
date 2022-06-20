# Games
# Demonstrates module creation

class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n") or ("yes", "no"):
        print('Use only "y" or "yes", "n" or "no"!')
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
            if response < low:
                print(f'Are you stupid? We need {low} player minimum!')
                response = None
            elif response > high:
                print(f'Are you stupid? We need not more {high} players!')
                response = None
        except:
            print(f'You can use only numbers from {low} to {high}')
            response = None
    return response

  
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")


