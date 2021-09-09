'''
This file is made to create objects of type Buddy or leader based on the person's responses
Created by: Juan David Guerra, McGill University
'''
import numpy as np


class Buddy:

    def __init__(self, name, pronouns, email, vector, ):
        self.name = name
        self.pronouns = pronouns
        self.email = email
        self.vector = vector  # This will be the person's responses to all the questions


class Leader:

    def __init__(self, name, pronouns, email, vector):
        self.name = name
        self.pronouns = pronouns
        self.email = email
        self.vector = vector
        self.numBuddies = 0


def getAnswersFromFile(fileTSV):
    """
    This function gets the data from the spreadsheet tsv
    :param fileTSV: the filename
    :return: will return a 2D array where the first array contains an array of all the buddies and the second array
            is made up of the Leader objects
    """

    fobj = open(fileTSV, 'r', encoding='utf-8')

    buddies = []
    leaders = []

    for line in fobj:

        line = line.strip("\n")
        info = line.split('\t')

        if info[0] == "Timestamp":
            continue

        vector = np.zeros(13)
        for i in range(5, 17):
            if info[i] == 'Yes':
                vector[i - 5] = 1
        if info[1] == "Incoming Buddy":

            leaders.append(Leader(info[2], info[3], info[4], vector))
        else:
            buddies.append(Buddy(info[2], info[3], info[4], vector))

    return [buddies, leaders]
