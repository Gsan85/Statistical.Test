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

# Additional Options for Distribution Functions
if data_type == "Continuous":
    st.subheader("You are working with continuous data.")
    distribution = st.selectbox(
        "Choose the type of distribution function to calculate:",
        ["PMF", "PDF", "CDF"]
    )

    dist_name = st.selectbox(
        "Choose the distribution:",
        ["Normal", "Binomial", "Poisson"]
    )

    if distribution == "PMF":
        if dist_name == "Binomial":
            st.write("**Probability Mass Function (PMF) for Binomial Distribution**")
            trials = st.number_input("Number of trials", min_value=1, value=10)
            probability = st.number_input("Probability of success", min_value=0.0, max_value=1.0, value=0.5)
            k = st.number_input("Number of successes", min_value=0, value=3)

            st.code(f"""
import scipy.stats as stats

trials = {trials}
probability = {probability}
k = {k}

pmf = stats.binom.pmf(k, trials, probability)
print(f"PMF: {{pmf}}")
""")
        elif dist_name == "Poisson":
            st.write("**Probability Mass Function (PMF) for Poisson Distribution**")
            mu = st.number_input("Mean rate (mu)", min_value=0.0, value=2.0)
            k = st.number_input("Number of events", min_value=0, value=3)

            st.code(f"""
import scipy.stats as stats

mu = {mu}
k = {k}

pmf = stats.poisson.pmf(k, mu)
print(f"PMF: {{pmf}}")
""")
    
    elif distribution == "PDF":
        if dist_name == "Normal":
            st.write("**Probability Density Function (PDF) for Normal Distribution**")
            mean = st.number_input("Mean", value=0.0)
            std_dev = st.number_input("Standard deviation", min_value=0.0, value=1.0)
            x = st.number_input("Value for PDF", value=0.0)

            st.code(f"""
import scipy.stats as stats

mean = {mean}
std_dev = {std_dev}
x = {x}

pdf = stats.norm.pdf(x, mean, std_dev)
print(f"PDF: {{pdf}}")
""")
    
    elif distribution == "CDF":
        if dist_name == "Normal":
            st.write("**Cumulative Distribution Function (CDF) for Normal Distribution**")
            mean = st.number_input("Mean", value=0.0)
            std_dev = st.number_input("Standard deviation", min_value=0.0, value=1.0)
            x = st.number_input("Value for CDF", value=0.0)

            st.code(f"""
import scipy.stats as stats

mean = {mean}
std_dev = {std_dev}
x = {x}

cdf = stats.norm.cdf(x, mean, std_dev)
print(f"CDF: {{cdf}}")
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
z_stat, p_value = sm_proportion.proportions_ztest(count, nobs)
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
