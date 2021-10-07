CSCE 474/874 Data Mining
Assignment #2
Last Updated: 03/06/2021
Group Members: Paul Fletcher and Juan Francisco-Simon

This program implements the Apriori algorithm.

We include two preprocessed data sets for testing of the algorithm:

test.csv - a test file provided in the assignment
supermarket.csv - supermarket transaction data set from Weka

To test a data set, navigate to main.py.

    To run test.csv:
        -In line 11 of main.py, change the filename to 'data/binaryTest.csv'
        -In line 15 of main.py, change the filename to 'data/transactionsTest.pkl'

    To run supermarket.csv:
        -In line 11 of main.py, change the filename to 'data/binarySupermarket.csv'
        -In line 15 of main.py, change the filename to 'data/transactionsSupermarket.pkl'

To experiment with different confidence and support threshold values

    Confidence:
        -In line 25, change the support threshold
        -In line 27, change the minimum confidence

When you are ready to run the program:
    -Navigate to the directory in a terminal
    -Run 'python3 main.py'

Output
    -The program will output all of the Frequent k itemsets and generated rules
    -It will also output a key to determine which numbers correspond to items




