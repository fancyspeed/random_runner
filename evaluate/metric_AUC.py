# -*- coding: utf-8 -*-
"""
Evaluation metric for the KDD Cup 2014 
AUC

@author: Michael Liu 
Created: Thu May 14 2014
"""

import os
import csv
import math


def create_solution_dictionary(solution):
    """ Read solution file, return a dictionary with key EventId and value (label, weight).
    Solution file headers: EventId, Label, Weight """
    
    solnDict = {}
    with open(solution, 'rb') as f:
        soln = csv.reader(f)
        #soln.next() # header
        for row in soln:
            if row[0] not in solnDict:
                if float(row[1]) > 0.5:
                    solnDict[row[0]] = 1
                else:
                    solnDict[row[0]] = 0 
    return solnDict

        
def check_submission(submission, solutionDict):
    """ Check that submission column is correct:
        1. All numbers are unique 
        2. All numbers are in solutionDict 
    """
    submissionDict = {} 
    with open(submission, 'rb') as f:
        sub = csv.reader(f)
        #sub.next() # header
        for row in sub:
            if row[0] in submissionDict:
                print 'duplicate id in submission'
                return False
            if row[0] not in solutionDict:
                print 'submission id must in solution' 
                return False
            submissionDict[row[0]] = float(row[1])
            
    if len(submissionDict) != len(solutionDict):
        print 'size of submission and solution must be the same'
        return False
    return submissionDict 

    
def AMS(s, b, br=10.0):
    """ Approximate Median Significance defined as:
        AMS = sqrt(
                2 { (s + b + b_r) log[1 + (s/(b+b_r))] - s}
              )        
    where b_r = 10, b = background, s = signal, log is natural logarithm """
    
    radicand = 2 * ( (s+b+br) * math.log (1.0 + s / (b+br)) - s )
    if radicand < 0:
        print 'radicand is negative. Exiting'
        return 0
    else:
        return math.sqrt(radicand)


def AUC_metric(solution, submission):
    """  Prints the AUC metric value to screen.
    Solution File header: EventId, Label
    Submission File header: EventId, Probability 
    """
    
    
    # solutionDict: key=eventId, value=label
    solutionDict = create_solution_dictionary(solution)

    submissionDict = check_submission(submission, solutionDict)
    if submissionDict:
        tot_true = len([v for k, v in solutionDict.items() if v > 0.5]) 
        tot_false = len(solutionDict) - tot_true
        if tot_false == 0:
            print 'no false instance...'
            return 1

        sort_list = sorted(submissionDict.items(), key=lambda d:d[1], reverse=True)

        remain_false = tot_false
        score = 0.
        for k, v in sort_list:
            if solutionDict[k] > 0.5:
                score += remain_false
            else:
                remain_false -= 1.
        auc = score / (tot_true * tot_false)
        print 'AUC= ', auc 
        return auc 
    return 0


if __name__ == "__main__":
    solutionFile = ""
    submissionFile = ""

    import sys
    if len(sys.argv) < 3:
        print '<usage> solution submission'
        exit(-1)
    solutionFile = sys.argv[1]
    submissionFile = sys.argv[2]
    
    AUC_metric(solutionFile, submissionFile)
    
    
