#!/bin/python3

from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
import subprocess


def add_score(difficulty_number):

# copying  /training/devops/scores.txt to /tmp/oldscore.txt

    FILESCOREOLD = "/tmp/oldscore.txt"
    COMMAND = ""
    COMMAND +=  "cp " + SCORES_FILE_NAME + " " + FILESCOREOLD
    #print(COMMAND)
    subprocess.check_output(COMMAND, shell=True).rstrip()

    with open(SCORES_FILE_NAME,"r") as file:
        scorenow = int(file.read())
        print(f"your score now is" , int(scorenow))
        file.close()
        win_points = (difficulty_number * 3) + 5
        new_score = scorenow + win_points
        print(f"New Score is" , int(new_score))
        with open(SCORES_FILE_NAME,"w") as f:
         f.write(str(new_score))
         f.close()

def zero_score():
    with open(SCORES_FILE_NAME,"w") as f:
       f.write(str('0'))
       f.close()
         

if __name__ == '__main__':

    add_score()
