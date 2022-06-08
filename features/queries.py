from common.common_module import *
from factory.database_wrapper import BaseSQL as Db

class ScriptDenodoSchema(Db):
    @staticmethod
    def query_count_numerical_id_e_account(db_connection, expected=None):
        run_sql(servername= '', database='mondrian', command="select count(1) from mondrian_pr223.e_account WHERE internal_account_id REGEXP_LIKE '^[1-9]\d*(\.\d+)?$' order by internal_account_id asc limit 1", database_type='denodo')

    @staticmethod
    def query_e_account():
        run_sql(servername= '', database='mondrian', command="select * from mondrian_pr223.e_account", database_type='denodo')