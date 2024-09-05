import streamlit as st
import numpy as np
import scipy.stats as stats
import statsmodels.stats.proportion as sm_proportion
import statsmodels.api as sm

# Title
st.title("Statistical Test Selector")

# Introduction
st.write("""
This app will help you select the appropriate statistical test for your problem, and then generate the Python code for it. 
Select the appropriate options based on the nature of your data and hypothesis.
""")

# Step 1: Ask the type of data
st.subheader("Step 1: What kind of data are you dealing with?")
data_type = st.selectbox(
    "Choose the type of data you're working with:",
    ("Compare Means", "Compare Proportions", "Categorical Data", "Correlation/Regression")
)

# Step 2: Ask details based on the type of data

if data_type == "Compare Means":
    st.write("You are comparing one or more means.")
    
    num_groups = st.radio(
        "How many groups do you have?",
        ("One", "Two", "Three or more")
    )
    
    if num_groups == "One":
        st.write("You are testing one sample mean against a known population mean.")
        std_known = st.radio("Is the population standard deviation known?", ("Yes", "No"))
        
        if std_known == "Yes":
            st.write("**Use a Z-test**")
            st.write("""
            **Python Code for Z-test:**
            """)
            st.code("""
import numpy as np
import scipy.stats as stats

sample_data = np.array([data])  # Replace with your sample data
pop_mean = population_mean  # Replace with population mean
pop_std = population_std  # Replace with population standard deviation
n = len(sample_data)
z_stat = (np.mean(sample_data) - pop_mean) / (pop_std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")
        
        else:
            st.write("**Use a one-sample t-test**")
            st.write("""
            **Python Code for One-sample t-test:**
            """)
            st.code("""
import numpy as np
import scipy.stats as stats

sample_data = np.array([data])  # Replace with your sample data
pop_mean = population_mean  # Replace with population mean
t_stat, p_value = stats.ttest_1samp(sample_data, pop_mean)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
""")
    
    elif num_groups == "Two":
        st.write("You are comparing the means of two independent groups.")
        equal_var = st.radio("Assume equal variance between the two groups?", ("Yes", "No"))
        
        st.write("**Use a two-sample t-test**")
        st.write("""
        **Python Code for Two-sample t-test:**
        """)
        st.code(f"""
import numpy as np
import scipy.stats as stats

sample_data1 = np.array([data1])  # Replace with your first sample data
sample_data2 = np.array([data2])  # Replace with your second sample data
t_stat, p_value = stats.ttest_ind(sample_data1, sample_data2, equal_var={equal_var == 'Yes'})
print(f"T-statistic: {{t_stat}}, P-value: {{p_value}}")
""")
    
    else:
        st.write("You are comparing the means of three or more groups.")
        st.write("**Use ANOVA (Analysis of Variance)**")
        st.write("""
        **Python Code for One-way ANOVA:**
        """)
        st.code("""
import numpy as np
import scipy.stats as stats

sample_data1 = np.array([data1])  # Replace with first group data
sample_data2 = np.array([data2])  # Replace with second group data
sample_data3 = np.array([data3])  # Replace with third group data
f_stat, p_value = stats.f_oneway(sample_data1, sample_data2, sample_data3)
print(f"F-statistic: {f_stat}, P-value: {p_value}")
""")

elif data_type == "Compare Proportions":
    st.write("You are comparing proportions.")
    
    num_groups = st.radio(
        "How many groups are you comparing?",
        ("One", "Two")
    )
    
    if num_groups == "One":
        st.write("You are testing one proportion against a hypothesized proportion.")
        st.write("**Use a one-sample z-test for proportions**")
        st.write("""
        **Python Code for One-sample Z-test for Proportions:**
        """)
        st.code("""
import statsmodels.stats.proportion as sm_proportion

count = number_of_successes  # Replace with the number of successes
nobs = total_observations  # Replace with total number of observations
p_value = sm_proportion.proportions_ztest(count, nobs)
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")
    
    else:
        st.write("You are comparing proportions between two groups.")
        st.write("**Use a two-sample z-test for proportions**")
        st.write("""
        **Python Code for Two-sample Z-test for Proportions:**
        """)
        st.code("""
import statsmodels.stats.proportion as sm_proportion

count = np.array([successes_group1, successes_group2])
nobs = np.array([total_obs_group1, total_obs_group2])
z_stat, p_value = sm_proportion.proportions_ztest(count, nobs)
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")

elif data_type == "Categorical Data":
    st.write("You are working with categorical data (e.g., contingency tables).")
    
    st.write("**Use a Chi-Square test of independence**")
    st.write("""
    **Python Code for Chi-Square Test:**
    """)
    st.code("""
import numpy as np
import scipy.stats as stats

observed = np.array([[data_row1], [data_row2]])  # Replace with observed data table
chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)
print(f"Chi-square statistic: {chi2_stat}, P-value: {p_value}")
""")

elif data_type == "Correlation/Regression":
    st.write("You are dealing with correlation or regression analysis.")
    
    corr_type = st.radio(
        "What kind of relationship are you testing?",
        ("Correlation", "Linear Regression")
    )
    
    if corr_type == "Correlation":
        st.write("**Use Pearson or Spearman correlation based on data type**")
        corr_method = st.radio("Select the correlation method:", ("Pearson (Parametric)", "Spearman (Non-parametric)"))
        
        if corr_method == "Pearson (Parametric)":
            st.write("""
            **Python Code for Pearson Correlation:**
            """)
            st.code("""
import numpy as np
import scipy.stats as stats

x = np.array([data_x])  # Replace with data for variable X
y = np.array([data_y])  # Replace with data for variable Y
corr, p_value = stats.pearsonr(x, y)
print(f"Pearson correlation: {corr}, P-value: {p_value}")
""")
        
        else:
            st.write("""
            **Python Code for Spearman Correlation:**
            """)
            st.code("""
import numpy as np
import scipy.stats as stats

x = np.array([data_x])  # Replace with data for variable X
y = np.array([data_y])  # Replace with data for variable Y
corr, p_value = stats.spearmanr(x, y)
print(f"Spearman correlation: {corr}, P-value: {p_value}")
""")
    
    else:
        st.write("**Use Linear Regression**")
        st.write("""
        **Python Code for Linear Regression:**
        """)
        st.code("""
import numpy as np
import statsmodels.api as sm

X = np.array([data_X])  # Replace with predictor data
y = np.array([data_y])  # Replace with response data
X = sm.add_constant(X)  # Add constant term for intercept
model = sm.OLS(y, X).fit()
print(model.summary())
""")
