# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle, shelve

def pickle_scores(player_name, score):
    try: 
        s = open("pickle_scores.dat", "rb+")
        score_list = pickle.load(s) 
    except:
        score_list = dict()
        print('Except works!')
    f = open("pickle_scores.dat", "wb+")
    #if name not in score_list:     
    print(f"\n  Your score ({score}) added! Have fun {player_name}!")
    score_list[player_name] = score


    print("\n", player_name, "has been added.")

    pickle.dump(score_list, f)
    f.close() 

def show_records():
    try:
        f = open("pickle_scores.dat", "rb+")
        a = pickle.load(f)
        print('\nHigh scores\n')
        print('NAME\tSCORE')
        
        sorted_score_list = dict()

        sorted_values = sorted(a.values(), reverse=True) # Sort the values
        for i in sorted_values:
            for k in a.keys():
                if a[k] == i:
                    sorted_score_list[k] = a[k]
                    break 
        for name in sorted_score_list:
            print(f'{name}\t{a[name]}')
        f.close()
        print('---------')
    except:
        print('Score list is empety!')
        
    
  


def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    #create cost of question.
    try:
        cost = next_line(the_file)
    #fix invalid literal for int() with base 10: ''
    except ValueError:
        cost = 0

    explanation = next_line(the_file)

    

    return category, question, answers, correct, explanation, cost

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

#def records():
#    text_file = open("read_it.txt", "r")
#    text_file = open('records.txt', 'w+', encoding='utf-8')

 
def main():
    player_name = input('Enter your name: ')
    trivia_file = open_file('bookMaterial/chapter07/trivia.txt', "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    

    # get first block
    category, question, answers, correct, explanation, cost = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(cost)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        score = int(score)
        # get next block
        category, question, answers, correct, explanation, cost = next_block(trivia_file)
        
     
    trivia_file.close()
    
    print("That was the last question!")
    print(f"Your ({player_name}) final score is {score}")
    pickle_scores(player_name, score)
    
show_records()
main() 
show_records()
input("\n\nPress the enter key to exit.")