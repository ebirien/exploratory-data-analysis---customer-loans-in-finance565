import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PowerTransformer

class DataFrameTransform:
    '''
    This class contains the methods which are used for DataFrame transformation.

    Parameters:
    -----------
    data_frame: DataFrame
        A Pandas DataFrame from which information will be generated.

    Methods:
    --------
    drop_null_columns()
        Drops columns with more that 50% NULL values.
    
    impute_null_values()
        Imputes null values in the DataFrame.

    transform_columns()
        Transforms to identified columns of the DataFrame to reduce skewness.

    treat_outliers()
        Treats the outliers via the capping method.
    '''
    def __init__(self, data_frame) -> None:
        self.df = data_frame

    def drop_null_columns(self):
        '''This method drops columns with more that 50% NULL values, and rows of date columns with NULL values.
              
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        # Get all columns in dataframe
        cols = self.df.columns
        drop_cols = []
        date_cols = []
        
        # delete columns with more than 50 % null values.
        for col in cols:
            if 100*(self.df[col].isnull().sum()/len(self.df)) > 50:
                drop_cols.append(col)
       
        self.df = self.df.drop(columns = drop_cols)
        
        # delete rows of date columns with NULL values.
        new_cols = self.df.columns
        for col in new_cols:
            if self.df[col].dtype == 'datetime64[ns]':
                date_cols.append(col)        

        self.df.dropna(subset = date_cols, inplace = True)

        # Resetting the indices using df.reset_index()
        self.df = self.df.reset_index(drop=True)
    
        return self.df           
       
    
    def impute_null_values(self):         
        '''This method imputes null values in the DataFrame.
              
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''
        for feature in self.drop_null_columns().columns:

            if self.df[feature].dtype == 'category':
                self.df[feature] = self.df[feature].fillna(self.df[feature].mode()[0])

            elif self.df[feature].dtype == 'float64' or self.df[feature].dtype == 'Int64' or self.df[feature].dtype == 'int64' or self.df[feature].dtype ==  'object':
                self.df[feature] = self.df[feature].fillna(self.df[feature].median())
 
        return self.df
    
    
    # DO NOT USE THIS METHOD
    def transform_columns(self):
        '''This method transforms to identified columns of the DataFrame to reduce skewness.
              
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''  
        #select only the numeric columns in the DataFrame
        df = self.impute_null_values().select_dtypes(include=['float64']) # include=np.number
        
        # Model Creation
        p_scaler = PowerTransformer(method='yeo-johnson')
        # yeojohnTr = PowerTransformer(standardize=True)   # not using method attribute as yeo-johnson is the default

        # fitting and transforming the model
        df_yjt = pd.DataFrame(p_scaler.fit_transform(df), columns=df.columns)

        return df_yjt   
    


    # Capping - change the outlier values to upper or lower limit values
    def treat_outliers(self):
        '''This method treats the outliers via the capping method.
              
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        ''' 
        # select only the numeric columns in the DataFrame
        df = self.transform_columns().select_dtypes(include=['float64'])
        new_df = df.copy()
       
        for feature in df.columns:
 
            q1 = new_df[feature].quantile(0.25) 
            q3 = new_df[feature].quantile(0.75) 
            iqr = q3 - q1
            lower_limit = q1 - 1.5 * iqr
            upper_limit = q3 + 1.5 * iqr  

            new_df.loc[new_df[feature]<=lower_limit, feature] = lower_limit
            new_df.loc[new_df[feature]>=upper_limit, feature] = upper_limit

        return new_df        




if __name__ == "__main__":
    
    import dtype_transform as tf
    import dataframe_info as dx
    df = pd.read_csv('loan_payments.csv')
    to_object_columns = ['id', 'member_id', 'policy_code']
    to_float_columns = ['loan_amount'] 
    to_category_columns = ['term', 'grade', 'sub_grade', 'employment_length', 'home_ownership', 'verification_status', 'loan_status', 'payment_plan', 'purpose', 'application_type']
    to_integer_columns = ['mths_since_last_delinq', 'mths_since_last_record', 'mths_since_last_major_derog', 'collections_12_mths_ex_med']
    to_date_columns = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']

    data = tf.DataTransform(df)

    new_df = data.to_object(to_object_columns)
    new_df = data.to_float(to_float_columns)
    new_df = data.to_category(to_category_columns)
    new_df = data.to_integer(to_integer_columns)
    new_df = data.to_datetime(to_date_columns)   

    info = dx.DataFrameInfo(new_df)
    # print(info.describe_columns())
    # print(info.extract_stats())
    # print(info.count_distinct_categories())
    # info.print_dataframe_shape()
    # print(info.generate_null_counts())
  
    fill_df = DataFrameTransform(new_df)
    
    print(fill_df.drop_null_columns())
    # print(fill_df.impute_null_values())
    # print(fill_df.treat_outliers())