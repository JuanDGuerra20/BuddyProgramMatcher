"""
This file takes the info from the BuddyCreator file and will match leaders and buddies according to their responses to
the form that was sent o
Created by Juan David Guerra, McGill University
"""
import numpy as np

import BuddyCreator as bc


def findLeader():
    """
    This function will find the appropriate leader for the buddy and will create a txt file
    :return:
    """

    people = bc.getAnswersFromFile("SUS Buddy Program Sign-Up Form (Responses) - Form Responses 1.tsv")

    fobj = open("Matched_Buddies_To_Leaders.txt", 'w', encoding='utf-8')
    buddyToLeader = {}
    # looping through all the buddies and setting to find the proper leader
    for buddy in people[0]:
        cosHigh = -10
        # looping through the leaders to find the smallest cosine similarity meaning best match
        for leader in people[1]:
            cosSim = np.dot(buddy.vector, leader.vector)
            cosSim = cosSim/(np.linalg.norm(buddy.vector)*np.linalg.norm(leader.vector))
            cosSim = cosSim*(0.85**leader.numBuddies)
            print(leader.name + str(cosSim))
            print("===========================================================")
            if cosHigh < cosSim:
                cosHigh = cosSim
                bestLeader = leader
        print('///////////////////////////////////////////////////////////////////////////////////////')
        print('///////////////////////////////////////////////////////////////////////////////////////')

        bestLeader.numBuddies += 1
        buddyToLeader[buddy] = bestLeader
        fobj.write("Buddy: " + buddy.name + "\t email: " + buddy.email + '\t pronouns: ' + buddy.pronouns + '\n')
        fobj.write("Leader: " + bestLeader.name + "\t email: " + bestLeader.email + '\t pronouns: ' + bestLeader.pronouns + '\n')
        fobj.write("Cos Sim: " + str(cosHigh) + "\n")
        fobj.write("================================================================================================== \n")

    fobj.close()

findLeader()