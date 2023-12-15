import pandas as pd
import numpy as np

class DataFrameInfo:
    '''
    This class contains the methods which are used to get information from the DataFrame.

    Parameters:
    -----------
    data_frame: DataFrame
        A Pandas DataFrame from which information will be generated.

    Methods:
    --------
    describe_columns()
        Describes all the columns in the DataFrame to check their data types
    
    extract_stats()
        Extracts statistical values: median, standard deviation and mean from the columns of the DataFrame

    count_distinct_categories()
        Counts distinct values in the categorical columns of the DataFrame

    print_dataframe_shape()
        Prints out the shape of the DataFrame

    generate_null_counts()
        Generates a count/percentage count of NULL values in each column
    '''
    def __init__(self, data_frame) -> None:
        self.df = data_frame
        self.dtdf = pd.DataFrame()

    def describe_columns(self):
        '''This method describes all the columns in the DataFrame to check their data types.
        
        Returns:
        --------
        dtypes
            The data types of all the columns in the DataFrame
        '''
        return self.df.dtypes 

    def extract_stats(self):
        '''This method extracts statistical values: median, standard deviation and mean from the columns of the DataFrame.
        
        Returns:
        --------
        data
            A dataset of median, standard deviation and mean of all the columns in the DataFrame
        '''
        # Get all dataframe columns with float and integer data types
        cols = self.df.select_dtypes(include=['float64', 'int64', 'Int64']).columns
        # Define an empty list of rows
        rows_list = []
        # Populate list of rows
        for col in cols:
            rows_list.append([col, self.df[col].median(), self.df[col].std(), self.df[col].mean()])
        
        # Convert the list into dataframe rows
        data = pd.DataFrame(rows_list)
        # Add column headers
        data.columns = ['column', 'median', 'std', 'mean']  
        return data

    def count_distinct_categories(self):
        '''This method counts distinct values in the categorical columns of the DataFrame.
        
        Returns:
        --------
        data
            A dataset of categorical columns and their distinct counts
        '''
        columns = self.df.select_dtypes(include=['category']).columns
        new_df = self.df[columns[:]]
        return new_df.nunique()


    def print_dataframe_shape(self):
        '''This method prints out the shape of the DataFrame.
        
        '''
        print(f'Shape of DataFrame: [{self.df.shape[0]} rows x {self.df.shape[1]} columns]\n')


    def generate_null_counts(self):
        '''This method generates a count/percentage count of NULL values in each column.
        
        Returns:
        --------
        data
            A dataset of column, count and % null count
        '''
        # Get all columns in dataframe
        cols = self.df.columns
        # Define an empty list of null column rows
        null_coulmn_rows = []
        # Populate list of null column rows
        for col in cols:
            # if self.df[col].isnull().sum() > 0:
            null_coulmn_rows.append([col, self.df[col].count(), 100*(self.df[col].isnull().sum()/len(self.df))])
        
        # Convert the list into dataframe rows
        data = pd.DataFrame(null_coulmn_rows)
        # Add columns headers
        data.columns = ['column', 'count', '% null count']  
        return data
       


if __name__ == "__main__":
    df = pd.read_csv('loan_payments.csv')
    to_object_columns = ['id', 'member_id', 'policy_code']
    to_float_columns = ['loan_amount'] 
    to_category_columns = ['term', 'grade', 'sub_grade', 'employment_length', 'home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose', 'application_type']
    to_integer_columns = ['mths_since_last_delinq', 'mths_since_last_record', 'mths_since_last_major_derog', 'collections_12_mths_ex_med']
    to_date_columns = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']

    import dtype_transform as tf
    data = tf.DataTransform(df)

    new_df = data.to_object(to_object_columns)
    new_df = data.to_float(to_float_columns)
    new_df = data.to_category(to_category_columns)
    new_df = data.to_integer(to_integer_columns)
    new_df = data.to_datetime(to_date_columns) 

    info = DataFrameInfo(new_df)
    # print(info.describe_columns())
    # print(info.extract_stats())
    # print(info.count_distinct_categories())
    # info.print_dataframe_shape()
    # print(info.generate_null_counts())