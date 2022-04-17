import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats


def KolmogorovTest(dataset, variable, apply_box_cox=False, plot_histogram=False):

    """
    This function computes Kolmogorov test to check if the variable
    is normaly distributed

    H0: The variable follows a normal distribution
    H1: The variable do not follow a normal distribution

    if p_value < 0.05 you can reject the null hypohesis

    Arguments:
        dataset: pandas dataframe

        variable: variable to performe the Kolmogorov test     
    """

    if apply_box_cox:
        x = stats.boxcox(dataset[variable].to_numpy())[0]
    else:
        x = dataset[variable].to_numpy()

    ktest = stats.kstest(x, 'norm')
    print('------------------------------------------------------------------------------')
    print(f'statistic={ktest[0]}, p_value={ktest[1]}\n')
    if ktest[1] < 0.05:
        print(f'Since {ktest[1]} < 0.05 you can reject the null hypothesis')
    else:
        print(f'Since {ktest[1]} > 0.05 you cannot reject the null hypothesis')
    print('------------------------------------------------------------------------------\n')
    if plot_histogram:
        fig = px.histogram(dataset, x=variable, nbins=30, marginal='box')
        fig.update_traces(marker_line_width=1, marker_line_color="white", opacity=0.9)
        fig.show()
        
 
def LeveneTest(dataset, target_variable, input_varaible):

    """
    Levene’s test is used to check that variances are equal for all 
    samples when your data comes from a non normal distribution. This
    function is created to work only when target variable is binary 

    H0: variances_1 = variances_2 = variances.
    H2: variances_1 != variances_2 != variances.

    if p_values < 0.05 rejecct the null hypothesis
    """

    y_unique = dataset[target_variable].unique()
    
    y1 = dataset.loc[dataset[target_variable] == y_unique[0] ,input_varaible].to_numpy()
    y2 = dataset.loc[dataset[target_variable] == y_unique[1] ,input_varaible].to_numpy()

    levene = stats.levene(y1, y2)

    print('------------------------------------------------------------------------------')
    print(f'statistic={levene[0]}, p_value={levene[1]}\n')
    if levene[1] < 0.05:
        print(f'Since {levene[1]} < 0.05 you can reject the null hypothesis')
    else:
        print(f'Since {levene[1]} > 0.05 you cannot reject the null hypothesis')
    print('------------------------------------------------------------------------------\n')

        
        
        
        
        
        
       
