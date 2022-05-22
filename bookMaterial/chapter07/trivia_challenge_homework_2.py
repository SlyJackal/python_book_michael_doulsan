# Trivia Challenge
# Trivia game that reads a plain text file
import sys, pickle, shelve

def show_records():
    global score_dict 
    score_dict = dict()
    try: 
        with open("trivia_score.txt") as file:
            while key := file.readline().strip():
                score_dict[key] = int(file.readline().strip())
    except:
        print('Score list is empety!')
    else:
        to_print = ''
        names = list(score_dict.keys())
        vals = list(score_dict.values())
        vals.sort(reverse=True)
        for val in vals:
            for i in range(len(names)): 
                if score_dict[names[i]] == val: 
                    to_print += f'{names.pop(i)}\t {val}\n' 
                    break #прервать цикл
        #print('\nHigh scores\n')
        #print(f'NAMES\tSCORES')
        #print(to_print)
        #print('---------')
    file.close
    return score_dict

def save_records_txt():
    
    with open("write_score.txt", 'w') as file:
        write_score_txt_keys = list(score_dict.keys())
        write_score_txt_values = str(list(score_dict.values()))
        print(write_score_txt_keys)
        print(write_score_txt_values)
        range_list = list()
        for i in range(len(write_score_txt_keys)):
            range_list += write_score_txt_keys[i]
            range_list += write_score_txt_values[i]
            #file.writelines(write_score_txt_keys[i])
            #file.writelines(write_score_txt_values[i])
        print(range_list)
        #while file.writelines:= 
        #file.writelines(["cat\n", "dog\n"])
        
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
print('----------------')
save_records_txt()
print('----------------')
#main() 

input("\n\nPress the enter key to exit.")