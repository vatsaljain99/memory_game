import csv

#Scans input CSV file and checks for current balance rows. Loads all current balances and account numbers into dict
#that is returned
def create_current_balance_dict(filename):
    account_number_and_balance_dict = {}
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            account_number = float(row[0])
            # print (account_number)
            if (row[6] == "Current Balance"):
                # print(row[0], row[6], "\n Value: ", row[7], row[8], row[9])
                current_balance_float = float(row[9])
                print(account_number, current_balance_float)
                account_number_and_balance_dict[account_number] = current_balance_float

    return account_number_and_balance_dict


create_current_balance_dict("updated_test_EOM.csv")

