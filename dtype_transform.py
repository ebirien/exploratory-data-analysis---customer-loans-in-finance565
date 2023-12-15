import pandas as pd
# from datetime import datetime as dt

class DataTransform:
    '''
    This class contains the methods which are used to transform the datatypes of a dataset columns.

    Parameters:
    -----------
    data_frame: DataFrame
        A Pandas DataFrame for transformation

    Methods:
    --------
    to_object(column_list)
        Converts the datatype of the listed columns to 'object'
    
    to_float(column_list)
        Converts the datatype of the listed columns to 'float64'

    to_category(column_list)
        Converts the datatype of the listed columns to 'category'

    to_integer(column_list)
        Converts the datatype of the listed columns to 'Int64'

    to_datetime(column_list)
        Converts the datatype of the listed columns to 'datetime64'
    '''

    def __init__(self, data_frame) -> None:
        self.df = data_frame
        
    def to_object(self, column_list):
        '''This method converts the datatype of the listed columns to 'object'.
        
        Parameters:
        -----------
        column_list: list
            A list of DataFrame columns for dataype conversion
        
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        
        self.df[column_list] = self.df[column_list].astype(object)

        return self.df
    

    def to_float(self, column_list):
        '''This method converts the datatype of the listed columns to 'float64'.
        
        Parameters:
        -----------
        column_list: list
            A list of DataFrame columns for dataype conversion
        
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        
        self.df[column_list] = self.df[column_list].astype('float64')

        return self.df
    

    def to_category(self, column_list):
        '''This method converts the datatype of the listed columns to 'category'.
        
        Parameters:
        -----------
        column_list: list
            A list of DataFrame columns for dataype conversion
        
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        
        self.df[column_list] = self.df[column_list].astype('category')

        return self.df
    
    
    def to_integer(self, column_list):
        '''This method converts the datatype of the listed columns to 'Int64'.
        
        Parameters:
        -----------
        column_list: list
            A list of DataFrame columns for dataype conversion
        
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        
        self.df[column_list] = self.df[column_list].astype('Int64')

        return self.df
    

    def to_datetime(self, column_list):
        '''This method converts the datatype of the listed columns to 'datetime64'.
        
        Parameters:
        -----------
        column_list: list
            A list of DataFrame columns for dataype conversion
        
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        
        for feature in column_list:
            self.df[feature] =  pd.to_datetime(self.df[feature], format='%b-%Y')

        return self.df



if __name__ == "__main__":

    df = pd.read_csv('loan_payments.csv')

    to_object_columns = ['id', 'member_id', 'policy_code']
    to_float_columns = ['loan_amount'] 
    to_category_columns = ['term', 'grade', 'sub_grade', 'employment_length', 'home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose', 'application_type']
    to_integer_columns = ['mths_since_last_delinq', 'mths_since_last_record', 'mths_since_last_major_derog', 'collections_12_mths_ex_med']
    to_date_columns = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']

    data = DataTransform(df)
    
    dataframe = data.to_object(to_object_columns)
    dataframe = data.to_float(to_float_columns)
    dataframe = data.to_category(to_category_columns)
    dataframe = data.to_integer(to_integer_columns)
    dataframe = data.to_datetime(to_date_columns)

    print(dataframe.head())

    datatypes = dataframe.dtypes 

    print(datatypes)