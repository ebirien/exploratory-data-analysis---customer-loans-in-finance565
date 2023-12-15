import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns


class Plotter:
    '''
    This class contains the methods which are used to visualise insights from the data.

    Parameters:
    -----------
    data_frame: DataFrame
        A Pandas DataFrame from which information will be generated.

    Methods:
    --------
    visualise_nulls_impute()
        Visualises the data to check if all the null values have been imputed.
    
    visualise_outliers()
        Visualises the data to determine if the columns contain outliers.
    '''    
    def __init__(self, data_frame) -> None:
        self.df = data_frame
       
    
    def visualise_nulls_impute(self): 
        '''This method plots the data to check if all the null values have been imputed. It allows us to visualise missing values if any as a bar chart.      
              
        Returns:
        --------
        plot
            A Bar chart plot
        '''       
        return msno.bar(self.df)
    
    
    def visualise_skewness(self):
        '''This method plots the data to visualise the skew. It uses Seaborn's Histogram with KDE line plot to achieve this.       
              
        Returns:
        --------
        plot
            Seaborn's Histogram with KDE line plot.
        '''  
        #select only the numeric columns in the DataFrame
        df = self.df.select_dtypes(include=['float64'])
        plt.figure(figsize=(18,14))

        for i in list(enumerate(df.columns)):
            fig_cols = 4
            fig_rows = int(len(df.columns)/fig_cols) + 1
            plt.subplot(fig_rows, fig_cols, i[0]+1)
            sns.histplot(data = df[i[1]], kde=True)

        # Show the plot
        plt.tight_layout()
        return plt.show()
    
    # Boxplot with Seaborn
    def visualise_outliers(self):
        '''This method visualises the data to determine if the columns contain outliers. It uses Seaborn's Boxplot to achieve this.       
              
        Returns:
        --------
        plot
            Seaborn's Boxplot.
        ''' 
        #select only the numeric columns in the DataFrame
        df = self.df.select_dtypes(include=['float64'])
        plt.figure(figsize=(18,14))

        for i in list(enumerate(df.columns)):
            fig_cols = 4
            fig_rows = int(len(df.columns)/fig_cols) + 1
            plt.subplot(fig_rows, fig_cols, i[0]+1)
            sns.boxplot(data=df[i[1]]) 

        # Show the plot
        plt.tight_layout()
        return plt.show()
    

if __name__ == "__main__":

    import pandas as pd

    df = pd.read_csv('loan_payments.csv')
    import dtype_transform as tt
    import dataframe_info as dx
    import data_transform as dt
    object = tt.DataTransform(df)
    new_df = object.change_datatypes()   

    info = dx.DataFrameInfo(new_df)

    dropped_df =  info.drop_null_rows_columns()

    fill_df = dt.DataFrameTransform(dropped_df)
    fill_df.fill_missing_values()

    plot = Plotter(fill_df.fill_missing_values())
    # plot.visualise_nulls_removal()     
    # plot.visualise_skewness()
    plot.visualise_outliers()