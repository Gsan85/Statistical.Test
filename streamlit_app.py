import streamlit as st
import pandas as pd

# Function to display Python code based on the test selected
def display_python_code(test):
    st.subheader(f"Python code for {test}:")
    
    if test == 't-test':
        st.code("""
import scipy.stats as stats

# Assuming data is in two pandas series: group1 and group2
t_stat, p_val = stats.ttest_ind(group1, group2)
print(f'T-test statistic: {t_stat}, p-value: {p_val}')
        """)
        
    elif test == 'ANOVA':
        st.code("""
import scipy.stats as stats

# Assuming data is in a pandas dataframe df with a column 'group' and 'values'
f_stat, p_val = stats.f_oneway(df['values'][df['group'] == 'Group1'],
                               df['values'][df['group'] == 'Group2'],
                               df['values'][df['group'] == 'Group3'])
print(f'ANOVA F-statistic: {f_stat}, p-value: {p_val}')
        """)
        
    elif test == 'Chi-square':
        st.code("""
import scipy.stats as stats

# Assuming data is in a contingency table (observed values)
chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)
print(f'Chi-square statistic: {chi2_stat}, p-value: {p_val}')
        """)
    
    elif test == 'Correlation':
        st.code("""
import scipy.stats as stats

# Assuming data is in two pandas series: x and y
corr, p_val = stats.pearsonr(x, y)
print(f'Pearson correlation coefficient: {corr}, p-value: {p_val}')
        """)
    
    elif test == 'Regression':
        st.code("""
import statsmodels.api as sm

# Assuming data is in a pandas dataframe df with columns 'X' and 'y'
X = sm.add_constant(df['X'])
model = sm.OLS(df['y'], X).fit()
print(model.summary())
        """)

# Title and instructions
st.title("Statistical Test Selector")
st.write("Choose the type of test based on your hypothesis and the nature of your data.")

# User input: type of hypothesis
hypothesis_type = st.selectbox(
    "What is the type of your hypothesis?",
    ['Comparison of Means', 'Association Between Variables', 'Prediction']
)

# User input: number of groups or variables
if hypothesis_type == 'Comparison of Means':
    num_groups = st.selectbox("How many groups do you have?", [2, 3, 'More than 3'])
    if num_groups == 2:
        test = 't-test'
    else:
        test = 'ANOVA'
elif hypothesis_type == 'Association Between Variables':
    data_type = st.selectbox("What is the type of your data?", ['Categorical', 'Continuous'])
    if data_type == 'Categorical':
        test = 'Chi-square'
    else:
        test = 'Correlation'
elif hypothesis_type == 'Prediction':
    test = 'Regression'

# Display selected test
st.write(f"Selected test: **{test}**")

# Display Python code for selected test
display_python_code(test)
