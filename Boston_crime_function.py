
def top_n(data_series, n):
    """
    This function print the top crime rate based on any varible we pass.

    :data_series: Takes the column name
    :n: The number of top records 

    """
    return data_series.value_counts().iloc[:n]


def ExploreData(dtaframe):
    """
    This function print these features of a data frame:
    1. Number of Rows
    2. Number of Columns
    3. Column names and their data types

    :dtaframe: Takes data frame as the input:

    """
    print("\nNumber of Columns: {}".format(len(dtaframe.columns)))
    print("\nNumber of Rows: {}".format(len(dtaframe)))
    print("\nColumns and their data types: \n\n{}".format(dtaframe.dtypes))


def PrintColValues(dataframe):
    """
    This function finds the uniques values present in each column in a data frame and prints it.
    The output is column name along with the unique values it has.
    If a column has more than 30 unique values, then it just print the number of unique values that column has.

    :dataframe: Takes data frame as the input:

    """
    for c in list(dataframe.columns):
        n = dataframe[c].unique()
        if len(n) < 30:
            print(c)
            print(n)
        else:
            print(c + ': ' + str(len(n)) + ' unique values')


def Remove_Outliers(dta, col):

    """
    This function is used to detect outliers using 3 sigma rule.
    That means any data point outside of 3 SD from the mean is an outlier.
    It takes 1-D data frame or a column as the input and returns a list of values which are outliers.

    :dta: Input data frame:
    :col: Input list of column or 1D data frame:

    """
    OldLen = len(dta)
    # Remove Outliers
    dta = dta[abs(dta[col] - dta[col].mean()) <= (3 * dta[col].std())]
    NewLen = len(dta)
    Num = OldLen - NewLen
    print("There were total {} outliers removed from the dataframe.".format(Num))



