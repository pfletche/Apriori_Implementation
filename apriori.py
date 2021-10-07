import itertools

# Get the frequent one itemset
def getFrequentOneItemSet(data,minSup):

    items = list(data.columns)

    itemSupport = list()
    itemKey = list()
    itemset = list()

    key = 0
    for item in items:
        d = data[item]
        support = sum(d.values)

        if support >= minSup:
            itemSupport.append(([key],support))
            itemset.append(key)

        itemKey.append((key,item))

        key += 1

    return itemset, itemKey, itemSupport

# Generate the candidate item sets
def genCandItemSet(k,data):

    if k <= 2:
        itemset = list(itertools.combinations(data, k))
    else:
        result = list(set([x for l in data for x in l]))
        itemset = list(itertools.combinations(result, k))

    return itemset

# Prune the candidate itemsets based on support
def pruneCandidates(data,itemCandidates,minSup,supportCount):

    itemset = list()

    for itemCand in itemCandidates:
        itemCand = list(itemCand)
        sup = 0
        for i in range(len(data)):
            transaction = data[i]

            if all(item in transaction for item in itemCand):
                sup += 1

        if sup >= minSup:
            itemset.append(itemCand)
            supportCount.append((itemCand,sup))

    return itemset, supportCount

# Generate rules based on itemsets and support values
def generateRules(itemSet,supportCount,ruleList,minCon):

    for value in supportCount:
        if value[0] == list(itemSet):
            itemSup = value[1]

    for i in range(len(itemSet) - 1):

        iConsequents = list(itertools.combinations(itemSet, i + 1))

        for con in iConsequents:
            ant = list(itemSet)

            for k in range(len(con)):
                ant.remove(con[k])
            con = list(con)

            for value in supportCount:
                if value[0] == list(ant):
                    antSup = value[1]

                    ruleConf = itemSup / antSup

                    if ruleConf >= minCon:
                        ruleList.append((ant,con,ruleConf))

    return ruleList













