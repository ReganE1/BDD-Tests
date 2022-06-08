#%%
from behave import *
from common.common_module import run_sql, db_connection
import pandas as pd
import pyodbc
from features.queries import ScriptDenodoSchema
from factory.database_wrapper import BaseSQL as sql

# account

@given('denodo exists')
def step_query_denodo(context):
    conn = db_connection(db='mondrian',server='',database_type = 'denodo')
    assert type(conn) == pyodbc.Connection



@when('e_account can be queried')
def step_query_e_account(context):
    var = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account", database_type='denodo')
    assert len(var) >0
    #sql.check_results(validate_content = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account", database_type='denodo'))
    
@then('the account_id_billing should have non-null entries #Advantage')
def step_e_account_advantage(context):
    var = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account where account_id_billing is not null", database_type='denodo')
    assert len(var) >0

@then('the account_id_crm should should have non-null entries #Salesforce')
def step_e_account_salesforce(context):
    var = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account where account_id_crm is not null", database_type='denodo')
    assert len(var) >0

@then('the account_id_invest_accounting should should have non-null entries #Portia')
def step_e_account_portia(context):
    var = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account where account_id_invest_accounting is not null", database_type='denodo')
    assert len(var) >0

@then('the account_id_performance should have non-null entries #Sylvan')
def step_e_account_sylvan(context):
    var = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account where account_id_performance is not null", database_type='denodo')
    assert len(var) >0

@then('the account_id_oms should have non-null entries #Longview')
def step_e_account_longview(context):
    var = run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account where account_id_oms is not null", database_type='denodo')
    assert len(var) >0