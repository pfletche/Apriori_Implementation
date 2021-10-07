import pandas as pd
import csv
import pickle

# Change the data values to numeric encodings and output a transactions list
def changeToNumeric(data,outFile):

    numericTransactions = list()

    for i in range(len(data)):
        transaction = data.iloc[i,:]
        row = list()
        k = 0
        for item in transaction:
            if item == 1:
                row.append(k)
            k += 1

        print('Change to Numeric: Row number: ', i, 'processed')

        numericTransactions.append(row)

    with open(outFile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(numericTransactions)

    return numericTransactions

# Change the data values to binary (0,1)
def changeToBinary(data,trueVal,falseVal,outFile):

    items = data.columns.tolist()
    newData = pd.DataFrame(columns=items)

    for i in range(len(data)):
        row = data.iloc[i,:]
        newRow = list()

        for k in range(len(row)):
            value = row.iloc[k]
            if value == falseVal:
                rowVal = 0
            elif value == trueVal:
                rowVal = 1
            else:
                rowVal = 'nan'

            newRow.append(rowVal)

        df_length = len(newData)
        newData.loc[df_length] = newRow
        print('Change to Binary: Row number: ', i, 'processed')

    newData.to_csv('data/' + outFile)

    return newData

if __name__ == "__main__":

    # *******************
    # DATA PRE-PROCESSING
    # *******************

    # Choose the appropriate filename
    fileName = 'test' #supermarket

    # Load the data sheet (converted to .csv in Weka)
    data = pd.read_csv('data/' + fileName + '.csv')

    # Change values from (y,n) to (1,0)
    data = changeToBinary(data,'y','n','binary' + fileName + '.csv')

    # Create data sheet with only true transactions (coded with unique numeric values)
    transactions = changeToNumeric(data,'data/transactions' + fileName + '.csv')

    # Create a pkl file for quick access to transactions list
    file = open('data/transactions' + fileName + '.pkl', "wb")
    pickle.dump(transactions, file)
    file.close()