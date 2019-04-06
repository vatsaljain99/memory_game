select gl_acct_num, gl_acct_name, year(max(trans_date)) as myear, month(max(trans_date)) as mmonth, day(max(trans_date)) as mday, end_bal
from sfcu.GL_700s_assets WHERE MONTH(TRANS_DATE) = 1
group by gl_acct_num, year(trans_date), month(trans_date)
order by gl_acct_num, myear, mmonth, mday 