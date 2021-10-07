import pandas as pd
import apriori as ap
import pickle
import time

# *******************
# DATA PRE-PROCESSING
# *******************

# Get the binary data sheet
data = pd.read_csv('data/binarySupermarket.csv') # CHANGE THIS TO CHANGE DATA SET
data = data.drop(columns=['Unnamed: 0'])

# Open the numeric transactions list
T = open("data/transactionsSupermarket.pkl", "rb") # CHANGE THIS TO CHANGE DATA SET
transactions = pickle.load(T)
T.close()

# ************************
# CONDUCT APRIORI ANALYSIS
# ************************
startTime = time.time()

# Set the values for min support and confidence
minSupThreshold = 0.45
minSup = int(len(data) * minSupThreshold)
minCon = 0.3

print('Min Support Threshold: ', minSupThreshold,
      '\nMin Support: ', minSup,
      '\nMin Confidence: ', minCon)

# Get the frequent 1 itemset
itemSet, itemKey, itemSupport = ap.getFrequentOneItemSet(data, minSup)

print('\nItem Key Codes: ', itemKey)
print('\nFrequent (1) Itemsets: ', itemSet)

# Process k+1 itemsets until support is less than minSup for all sets
k = 2
ruleList = list() # Create an empty list to store the generated rules

while len(itemSet) > 0:

    # Get the candidate (k) itemsets
    itemSet = ap.genCandItemSet(k,itemSet)

    # Prune the candidate (k) itemsets based on minSup
    itemSet, itemSupport = ap.pruneCandidates(transactions,itemSet,minSup,itemSupport)

    for item in itemSet:
        ruleList = ap.generateRules(item, itemSupport, ruleList, minCon)

    print('Frequent (%d) Itemsets: ' % (k), itemSet)

    k += 1

# Print the generated rules
print('\n** Rules Generated **\n')
for rule in ruleList:
    print(rule[0], '=>', rule[1], 'Confidence: ', rule[2])

# Get the finishing time
finishTime = time.time() - startTime

# Output the runtime and number of rules to the record
runtimeRecord = pd.read_csv('data/runtimeRecordTest.csv', index_col=0)
newRecord = pd.DataFrame({'time': [finishTime],
                          'numRules':[len(ruleList)],
                          'minSup':[minSup],
                          'minSupThreshold': [minSupThreshold],
                          'minCon': [minCon]})
runtimeRecord = runtimeRecord.append(newRecord)
runtimeRecord.to_csv('data/runtimeRecordTest.csv')



