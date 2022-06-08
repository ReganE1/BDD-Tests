Feature: E_Account is fully functional and returns data
    In order for e_account to be used in interface views and downstream processes
    by any business user
    E_Account must return data and have connections from Salesforce, Advantage, Portia

    Scenario: Execute account entity 
        Given denodo exists
        when e_account can be queried
        Then the account_id_billing should have non-null entries #Advantage
        And the account_id_crm should should have non-null entries #Salesforce
        And the account_id_invest_accounting should have non-null entries #Portia
        And the account_id_performance should have non-null entries #Sylvan
        And the account_id_oms should have non-null entries #Longview