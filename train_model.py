#!/usr/bin/env python

# Do *not* edit this script. Changes will be discarded so that we can process the models consistently.

# This file contains functions for training models for the 2022 Challenge. You can run it as follows:
#
#   python train_model.py data model
#
# where 'data' is a folder containing the Challenge data and 'model' is a folder for saving your model.

import sys
from helper_code import is_integer
from team_code import train_challenge_model

if __name__ == '__main__':
    # Parse the arguments.
    # if not (len(sys.argv) == 3 or len(sys.argv) == 4):
    #     raise Exception('Include the data and model folders as arguments, e.g., python train_model.py data model.')

    # Define the data and model foldes.
    data_folder = sys.argv[1]
    model_folder = sys.argv[2]

    # Change the level of verbosity; helpful for debugging.
    if len(sys.argv)==5 and is_integer(sys.argv[4]):
        print("ARGUMENTS ACCEPTED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        ep1 = int(sys.argv[3])
        ep2 = int(sys.argv[4])
    else:
        ep1 = 10
        ep2 = 20

    verbose = 0

    train_challenge_model(data_folder, model_folder, verbose, ep1, ep2) ### Teams: Implement this function!!!
