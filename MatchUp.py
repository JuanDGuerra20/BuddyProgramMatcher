"""
This file takes the info from the BuddyCreator file and will match leaders and buddies according to their responses to
the form that was sent out
Created by Juan David Guerra, McGill University
"""
import numpy as np

import BuddyCreator as bc


def findLeader():
    """
    This function will find the appropriate leader for the buddy and will create a txt file
    :return:
    """

    people = bc.getAnswersFromFile("INPUT THE FILENAME")

    fobj = open("Matched_Buddies_To_Leaders.txt", 'w', encoding='utf-8')
    buddyToLeader = {}
    for buddy in people[0]:
        cosMin = 10
        for leader in people[1]:
            cosSim = np.dot(buddy.vector, leader.vector)
            cosSim = cosSim/(np.linalg.norm(buddy.vector)*np.linalg.norm(leader.vector))
            cosSim = cosSim*(0.95**leader.numBuddies)
            if cosMin > cosSim:
                cosMin = cosSim
                bestLeader = leader

        bestLeader.numBuddies += 1
        buddyToLeader[buddy] = bestLeader
        fobj.write("Buddy: " + buddy.name + "\t email: " + buddy.email + '\t pronouns: ' + buddy.pronouns + '\t concerns: ' + buddy.concerns + '\n')
        fobj.write("Leader: " + bestLeader.name + "\t email: " + bestLeader.email + '\t pronouns: ' + bestLeader.pronouns + '\t concerns: ' + bestLeader.concerns + '\n')
        fobj.write("==================================================================================================")