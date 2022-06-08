#%%

from behave import *
from common.common_module import *
import pandas as pd

#%%
df = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account", database_type='denodo')


#%%
db_connection(database_type = 'denodo')
