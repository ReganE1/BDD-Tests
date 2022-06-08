import os
import json
import time
from factory.base_logging import BaseLogging as Log
from factory.running_exception import RunningException as Rexc
from factory.assertion import Assertion as Assert
from factory.strings_util import StringUtil


UTF8_UPPER = "UTF-8"
UTF8 = "utf-8"

class BaseSQL(Log):
    @staticmethod
    def assert_that(comparative_value=""):
        return Assert(comparative_value)

    def new_db_connection(json_db_config):
        if json_db_config is not None:
            return json.load(json_db_config)


    @staticmethod
    def select_cursor(conn, any_sql, validate_content):
        cursor_ = conn.cursor(buffered=True)
        time.sleep(0.5)
        try:
            if str(any_sql) is not None:
                Log.info(f"Executing statement:\n {any_sql}")
                any_sql = StringUtil.remove_multispaces(str(any_sql).replace("\n", "").strip())
                cursor_.execute(any_sql)
                time.sleep(1)
                BaseSQL.check_results(cursor_, validate_content)
        except Exception as e:
            Log.error(e)
            raise e
        finally:
            cursor_.close()

    @staticmethod
    def check_results(validate_content):
        Log.info("\n------------- The query has been executed ------------")
        try:
            if validate_content is not None:
                print(validate_content)
                assert len(validate_content) > 0
                # records = cursor_.fetchone()
                # if str(validate_content).isdigit():
                #     Log.info(f"Total rows: {len(records)}")
                #     BaseSQL.assert_that(records[0]).is_equals_to(
                #         int(validate_content), "Total rows found"
                #     )
                # else:
                #     for row in records:
                #         BaseSQL.assert_that(row).contains_the(
                #             validate_content, "Results fetched (Array_size)"
                #         )
        except Exception as error:
            Rexc.raise_assertion_error("Failed to read data from table", error)