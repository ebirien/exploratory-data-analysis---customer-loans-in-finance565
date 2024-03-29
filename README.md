# Exploratory Data Analysis - Customer Loans in Finance
## Project Description
This project is a part of the requirements for the Aicore data analytics certification. It was undertaken for a large financial institution, where loans managiment forms a critical component of business operations.

Exploratory data analysis was conducted on the loan portfolio data, with the aim of gaining a deeper understanding of the risk and return associated with the business' loans.

The aim of this project was to demonstrate a working advanced knowledge of Exploratory data analysis with Pandas and Python programming language. Several python classes were created to extract data from the cloud, convert columns to the correct format, get information from the DataFrame, perform EDA transformation on the data, remove/impute missing data, and visualise insights from the data.

The project involved the following tasks:
1. Setting up the development environment
  - Github
  - Visual studio code

2. Extraction of the loans data from the cloud
  - Created a python class for data extraction
  - Extracted the data from RDS database hosted in AWS cloud
  - Familiarised myself with the data in preparation for EDA
  ### Screenshot of Python Data Extraction Class
  ![Data Extraction Class](/RDSDatabaseConnector.png)

3. Exploratory Data Analysis (EDA)
  - Converted columns to the correct format
  - Created a python class to get information from the DataFrame
  - Remove/impute missing values in the data
  - Performed transformations on skewed columns
  - Removed outliers from the data
  - Dropped overly correlated columns

  ### Screenshot of Python Data Conversion Class
  ![Data Conversion Class](/DataTransform.png)
  
  ### Screenshot of Python Dataframe Info Class
  ![Dataframe Info Class](/DataframeInfo.png)

  ### Screenshot of Python Plotter Info Class
  ![Plotter Class](/Plotter.png)

  ### Screenshot of Skewness Before Transform
  ![Skewness Before Transform](/Skewness_Before_Transform.png)

  ### Screenshot of Skewness After Transform
  ![Skewness After Transform](/Skewness_After_Transform.png)

  ### Screenshot of Outliers Before Transform
  ![Outliers Before Transform](/Outliers_Before_Transform.png)

  ### Screenshot of Skewness After Transform
  ![ouliers After Transform](/Outliers_After_Transform.png)

4. Analysis and Visualisation
  - Determined the current state of the loans
  - Calculated loss
  - Calculated projected loss
  - Computed possible loss
  - Identified indicators of loss

## Installation Instructions
Download the following files to a named folder in your computer.
- loan_payments.py
- dtype_transform.py
- dataframe_info.py
- data_transform.py
- data_plotter.py
- eda.ipynb

  ### Screenshot of Total Payment vs Projected Loss Plot
  ![Projected Loss Plot](/Projected_Loss.png)

## Usage Instructions
To run the project simply open the eda.ipynb file with any interactive python notebook program and go through the various steps in the notebook.

## File Structure
- loan_payments.py
- dtype_transform.py
- dataframe_info.py
- data_transform.py
- data_plotter.py
- eda.ipynb
- db_utils.py
- LICENSE file
- .gitignore file
- README.md file

## License Information
MIT License
