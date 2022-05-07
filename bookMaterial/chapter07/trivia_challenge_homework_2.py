# Trivia Challenge
# Trivia game that reads a plain text file
import sys, pickle, shelve
from traceback import print_tb

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
        f.close()
    except:
        print('Score list is empety!')
    else:
        print('\nHigh scores\n')
        print('NAME\tSCORE')
        '''
        list_out=[]
        list_in=[]
        for r in a:
            list_in=[a[r], r]
            list_out.append(list_in)
        list_out.sort(reverse=True)
        for i in list_out:
            print(f'{i[1]}\t{i[0]}')
        '''
        to_print = '' #создали пустую строку
        names = list(a.keys()) #создали список ключей словаря
        vals = list(a.values()) #создали список значений словаря
        vals.sort(reverse=True) #отсортировали список значений от большего к меньшему
        for val in vals: #для всех val(значений) в списке значений словаря
            for i in range(len(names)): #для всех i(значений) в промежутке до длины списка(количества переменных в нем)
                if a[names[i]] == val: #если в словаре "а", по ключу из списка "names" значение равер val
                    to_print += f'{names.pop(i)}:\t {val}\n' #тогда в строку "to_print" дабавить строку, где из i извлечено(удалено) из списка "names" и значение "val"
                    break #прервать цикл
        print(to_print)
        print('---------')
        
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

def next_line_score(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("\n", "")
    return line

def next_block_score(the_file):
    name = next_line(the_file)
    score = next_line(the_file)
    return name, score

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

def show_txt_records():
    score_file = open_file('trivia_score.txt', 'r')
    name, score = next_block_score(score_file)
    print('NAME\tSCORE')
    #костыль, найти другой метод
    '''
    first = f'{name}\t{score}'
    first = first.replace("\n", "")
    print(f'{first}')
    while name:
        name = next_line_score(score_file)
        score = next_line_score(score_file)
        print(f'{name}\t{score}')
    '''
    to_print = '' #создали пустую строку
    names, vals = next_block_score(score_file)
    while names:
        names = list(next_line_score(score_file)) 
        vals = list(next_line_score(score_file)) 
        vals.sort(reverse=True) 
        for val in vals: 
            for i in range(len(names)):
                if names[i] == val: 
                    to_print += f'{names.pop(i)}:\t {val}\n' 
                    
       
        print(to_print)
        print('---------')
        break



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
      
show_txt_records()
#main() 


input("\n\nPress the enter key to exit.")