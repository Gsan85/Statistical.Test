import streamlit as st
import numpy as np
import scipy.stats as stats
import statsmodels.stats.proportion as sm_proportion
import statsmodels.stats.multicomp as mc

# Set up the Streamlit app layout
st.title("Statistical Test Selector App")
st.write("Select the appropriate test based on the nature of your data and hypothesis.")

# Step 1: Guide through the selection process
st.subheader("Step 1: What is the nature of your data?")
data_type = st.selectbox(
    "What kind of data do you have?",
    ("One Sample Mean", "Two Sample Means", "Proportions", "Categorical Data")
)

# Step 2: Provide explanations and options for the statistical test based on user input
if data_type == "One Sample Mean":
    st.write("You are testing a sample mean against a known population mean.")
    
    # Ask if the population standard deviation is known
    std_known = st.radio(
        "Is the population standard deviation known?",
        ("Yes", "No")
    )
    
    # Explanation
    if std_known == "Yes":
        st.write("""
        **Use a z-test:** The population standard deviation is known, so the z-test is appropriate.
        - Null Hypothesis (H₀): Sample mean = population mean
        - Alternative Hypothesis (H₁): Sample mean ≠ population mean (two-tailed) or one-tailed if specified.
        """)
        # Sample Data Input
        sample_data = st.text_area("Enter your sample data (comma-separated):")
        sample_data = np.array([float(x) for x in sample_data.split(',')])
        pop_mean = st.number_input("Enter the population mean:", value=0.0)
        pop_std = st.number_input("Enter the population standard deviation:", value=1.0)
        
        # Python code for z-test
        st.code(f"""
import numpy as np
import scipy.stats as stats

sample_data = np.array({sample_data.tolist()})
pop_mean = {pop_mean}
pop_std = {pop_std}
n = len(sample_data)
z_stat = (np.mean(sample_data) - pop_mean) / (pop_std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
print(f"Z-statistic: {{z_stat}}, P-value: {{p_value}}")
""")
    else:
        st.write("""
        **Use a t-test:** The population standard deviation is unknown, so the t-test is appropriate.
        - Null Hypothesis (H₀): Sample mean = population mean
        - Alternative Hypothesis (H₁): Sample mean ≠ population mean (two-tailed) or one-tailed if specified.
        """)
        # Sample Data Input
        sample_data = st.text_area("Enter your sample data (comma-separated):")
        sample_data = np.array([float(x) for x in sample_data.split(',')])
        pop_mean = st.number_input("Enter the population mean:", value=0.0)
        
        # Python code for one-sample t-test
        st.code(f"""
import numpy as np
import scipy.stats as stats

sample_data = np.array({sample_data.tolist()})
pop_mean = {pop_mean}
t_stat, p_value = stats.ttest_1samp(sample_data, pop_mean)
print(f"T-statistic: {{t_stat}}, P-value: {{p_value}}")
""")

elif data_type == "Two Sample Means":
    st.write("You are comparing the means of two independent samples.")
    
    # Ask about population standard deviations
    equal_var = st.radio(
        "Assume equal variance between the two groups?",
        ("Yes", "No")
    )
    
    # Explanation
    st.write("""
    **Use a two-sample t-test:** This test compares the means of two independent samples.
    - Null Hypothesis (H₀): Mean of sample 1 = Mean of sample 2
    - Alternative Hypothesis (H₁): Mean of sample 1 ≠ Mean of sample 2 (two-tailed) or one-tailed if specified.
    """)
    
    # Sample Data Input
    sample_data1 = st.text_area("Enter sample data for Group 1 (comma-separated):")
    sample_data2 = st.text_area("Enter sample data for Group 2 (comma-separated):")
    sample_data1 = np.array([float(x) for x in sample_data1.split(',')])
    sample_data2 = np.array([float(x) for x in sample_data2.split(',')])

    # Python code for two-sample t-test
    st.code(f"""
import numpy as np
import scipy.stats as stats

sample_data1 = np.array({sample_data1.tolist()})
sample_data2 = np.array({sample_data2.tolist()})
t_stat, p_value = stats.ttest_ind(sample_data1, sample_data2, equal_var={equal_var == 'Yes'})
print(f"T-statistic: {{t_stat}}, P-value: {{p_value}}")
""")

elif data_type == "Proportions":
    st.write("You are comparing proportions between groups or testing a single proportion.")
    
    # Explanation
    st.write("""
    **Use a z-test for proportions:** This test compares the proportions of one or two groups.
    - Null Hypothesis (H₀): The proportions are equal (or the proportion equals a certain value in the one-sample case).
    - Alternative Hypothesis (H₁): The proportions are not equal (or the proportion does not equal a certain value).
    """)
    
    # Data Input
    count = st.number_input("Enter the number of successes:", value=0, min_value=0)
    nobs = st.number_input("Enter the total number of observations:", value=1, min_value=1)
    
    # Python code for z-test for proportions
    st.code(f"""
import statsmodels.stats.proportion as sm_proportion

count = {count}
nobs = {nobs}
z_stat, p_value = sm_proportion.proportions_ztest(count, nobs)
print(f"Z-statistic: {{z_stat}}, P-value: {{p_value}}")
""")

elif data_type == "Categorical Data":
    st.write("You are testing for independence between two categorical variables.")
    
    # Explanation
    st.write("""
    **Use a Chi-square test of independence:** This test determines if two categorical variables are independent of each other.
    - Null Hypothesis (H₀): The variables are independent.
    - Alternative Hypothesis (H₁): The variables are not independent.
    """)
    
    # Data Input
    observed = st.text_area("Enter the observed frequency table (comma-separated rows):")
    observed = np.array([list(map(int, row.split(','))) for row in observed.split('\n')])
    
    # Python code for Chi-square test
    st.code(f"""
import numpy as np
import scipy.stats as stats

observed = np.array({observed.tolist()})
chi2, p_value, _, _ = stats.chi2_contingency(observed)
print(f"Chi-square statistic: {{chi2}}, P-value: {{p_value}}")
""")
