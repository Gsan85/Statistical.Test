import streamlit as st
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.proportion as sm_proportion

# Title of the app
st.title("Statistical Test Selector")

# Introduction
st.write("""
This app will help you choose the correct statistical test based on your data and hypothesis, 
following the framework from the lecture slides. The app will also provide you with the Python code for running the test.
""")

# Step 1: Data type selection
st.header("Step 1: What type of data do you have?")
data_type = st.selectbox(
    "Select the type of data you are working with:",
    ["Continuous", "Proportions", "Categorical"]
)

# Step 2: Test selection based on data type
if data_type == "Continuous":
    st.subheader("You are working with continuous data.")
    test_scenario = st.selectbox(
        "Choose your test scenario:",
        ["One sample mean", "Two sample means", "More than two sample means"]
    )

    if test_scenario == "One sample mean":
        st.write("**Use a Z-test or t-test depending on the standard deviation knowledge.**")
        std_known = st.radio("Is the population standard deviation known?", ("Yes", "No"))
        if std_known == "Yes":
            st.write("**Z-test** is appropriate when the population standard deviation is known.")
            st.code("""
import numpy as np
import scipy.stats as stats

# Replace with your data
sample_data = np.array([data])
pop_mean = population_mean
pop_std = population_std
n = len(sample_data)

z_stat = (np.mean(sample_data) - pop_mean) / (pop_std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")
        else:
            st.write("**t-test** is appropriate when the population standard deviation is unknown.")
            st.code("""
import numpy as np
import scipy.stats as stats

# Replace with your data
sample_data = np.array([data])
pop_mean = population_mean

t_stat, p_value = stats.ttest_1samp(sample_data, pop_mean)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
""")

    elif test_scenario == "Two sample means":
        st.write("**Two-sample t-test or z-test** depending on standard deviation knowledge.")
        std_known = st.radio("Are the population standard deviations known?", ("Yes", "No"))
        if std_known == "Yes":
            st.write("**Two-sample z-test** is appropriate when population standard deviations are known.")
            st.code("""
import numpy as np
import scipy.stats as stats

# Replace with your data
sample_data1 = np.array([data1])
sample_data2 = np.array([data2])
pop_std1 = std_dev1
pop_std2 = std_dev2
n1, n2 = len(sample_data1), len(sample_data2)

z_stat = (np.mean(sample_data1) - np.mean(sample_data2)) / np.sqrt((pop_std1**2 / n1) + (pop_std2**2 / n2))
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")
        else:
            st.write("**Two-sample t-test** is appropriate when population standard deviations are unknown.")
            equal_var = st.radio("Do the two groups have equal variances?", ("Yes", "No"))
            st.code(f"""
import numpy as np
import scipy.stats as stats

# Replace with your data
sample_data1 = np.array([data1])
sample_data2 = np.array([data2])

t_stat, p_value = stats.ttest_ind(sample_data1, sample_data2, equal_var={equal_var == 'Yes'})
print(f"T-statistic: {{t_stat}}, P-value: {{p_value}}")
""")

    else:
        st.write("**ANOVA** is used when comparing the means of more than two groups.")
        st.code("""
import numpy as np
import scipy.stats as stats

# Replace with your data for multiple groups
sample_data1 = np.array([data1])
sample_data2 = np.array([data2])
sample_data3 = np.array([data3])

f_stat, p_value = stats.f_oneway(sample_data1, sample_data2, sample_data3)
print(f"F-statistic: {f_stat}, P-value: {p_value}")
""")

elif data_type == "Proportions":
    st.subheader("You are working with proportions.")
    test_scenario = st.selectbox(
        "Choose your test scenario:",
        ["One proportion", "Two proportions"]
    )

    if test_scenario == "One proportion":
        st.write("**Use a one-sample z-test for proportions.**")
        st.code("""
import statsmodels.stats.proportion as sm_proportion

count = number_of_successes  # Replace with your data
nobs = total_observations
p_value = sm_proportion.proportions_ztest(count, nobs)
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")
    else:
        st.write("**Use a two-sample z-test for proportions.**")
        st.code("""
import statsmodels.stats.proportion as sm_proportion

count = np.array([successes_group1, successes_group2])
nobs = np.array([total_obs_group1, total_obs_group2])
z_stat, p_value = sm_proportion.proportions_ztest(count, nobs)
print(f"Z-statistic: {z_stat}, P-value: {p_value}")
""")

elif data_type == "Categorical":
    st.subheader("You are working with categorical data.")
    st.write("**Use a Chi-square test of independence.**")
    st.code("""
import numpy as np
import scipy.stats as stats

# Replace with your observed data table
observed = np.array([[data_row1], [data_row2]])

chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)
print(f"Chi-square statistic: {chi2_stat}, P-value: {p_value}")
""")

# Conclusion
st.write("Based on your selections, the corresponding statistical test and Python code are provided.")
