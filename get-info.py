# import pandas as pd
import mysql.connector as sql
import pandas as pd
import numpy as np
import user


def getBalance(account, month):

    if (account >= 700 and account < 800):
        db_query = 'select gl_acct_num, gl_acct_name, year(max(trans_date)) as myear, month(max(trans_date)) as mmonth, day(max(trans_date)) as mday, end_bal from sfcu.GL_700s_assets WHERE MONTH(TRANS_DATE) = ' + str(month) + ' AND GL_ACCT_NUM = ' + str(account) + ' group by gl_acct_num, year(trans_date), month(trans_date) order by gl_acct_num, myear, mmonth, mday' 
    elif (account >= 800 and account < 900):
        db_query = 'select gl_acct_num, gl_acct_name, year(max(trans_date)) as myear, month(max(trans_date)) as mmonth, day(max(trans_date)) as mday, end_bal from sfcu.GL_800s_liabilities WHERE MONTH(TRANS_DATE) = ' + str(month) + ' AND GL_ACCT_NUM = ' + str(account) + ' group by gl_acct_num, year(trans_date), month(trans_date) order by gl_acct_num, myear, mmonth, mday' 
    elif (account >= 900):        
        db_query = 'select gl_acct_num, gl_acct_name, year(max(trans_date)) as myear, month(max(trans_date)) as mmonth, day(max(trans_date)) as mday, end_bal from sfcu.GL_900s_equities WHERE MONTH(TRANS_DATE) = ' + str(month) + ' AND GL_ACCT_NUM = ' + str(account) + ' group by gl_acct_num, year(trans_date), month(trans_date) order by gl_acct_num, myear, mmonth, mday' 
    else:
        print("Not 700-999 account")
 
    'select gl_acct_num, gl_acct_name, year(max(trans_date)) as myear, month(max(trans_date)) as mmonth, day(max(trans_date)) as mday, end_bal from sfcu.GL_700s_assets WHERE MONTH(TRANS_DATE) = ' + str(month) + ' AND GL_ACCT_NUM = ' + str(account) + ' group by gl_acct_num, year(trans_date), month(trans_date) order by gl_acct_num, myear, mmonth, mday' 
    
    db_connection = sql.connect(host=user.db_host, database=user.db_database, user=user.db_username, password=user.db_password, ssl_ca= 'rds-combined-ca-bundle.pem')
    db_cursor = db_connection.cursor()
    db_cursor.execute(db_query)
    table_rows = db_cursor.fetchall()
    account_df = pd.DataFrame(table_rows, columns=db_cursor.column_names)
    return account_df

df = getBalance(701.03, 10)