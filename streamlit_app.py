import streamlit as st
import numpy as np
import scipy.stats as stats
import statsmodels.stats.proportion as sm_proportion
import statsmodels.stats.multicomp as mc

# Set up the Streamlit app layout
st.title("Statistical Test Selector App")
st.write("Select the appropriate test based on the nature of your data and hypothesis.")

# Step 1: Select the type of test
test_type = st.selectbox(
    "What type of test do you want to perform?",
    ("Test for One Mean", "Test for Equality of Means", 
     "Test for One or Two Proportions", "Test of Independence (Chi-Square)", 
     "Analysis of Variance (ANOVA)", "Shapiro Test (Normality)", 
     "Levene Test (Equal Variances)")
)

# Step 2: Define Hypotheses
st.subheader("Formulate Hypotheses")
null_hypothesis = st.text_input("Enter the null hypothesis (H₀):")
alt_hypothesis = st.text_input("Enter the alternative hypothesis (H₁):")
alpha = st.slider("Choose significance level (alpha):", 0.01, 0.10, 0.05)

# Step 3: Data Entry
st.subheader("Data Entry")
if test_type in ["Test for One Mean", "Shapiro Test (Normality)"]:
    sample_data = st.text_area("Enter your sample data (comma-separated):")
    sample_data = np.array([float(x) for x in sample_data.split(',')])
elif test_type in ["Test for Equality of Means", "Levene Test (Equal Variances)", "Analysis of Variance (ANOVA)"]:
    sample_data1 = st.text_area("Enter sample data for Group 1 (comma-separated):")
    sample_data2 = st.text_area("Enter sample data for Group 2 (comma-separated):")
    sample_data1 = np.array([float(x) for x in sample_data1.split(',')])
    sample_data2 = np.array([float(x) for x in sample_data2.split(',')])
elif test_type == "Test for One or Two Proportions":
    count = st.number_input("Enter the number of successes:", value=0, min_value=0)
    nobs = st.number_input("Enter the total number of observations:", value=1, min_value=1)

# Step 4: Choose the right test and compute
if st.button("Run Test"):

    # Test for One Mean (One-sample t-test)
    if test_type == "Test for One Mean":
        pop_mean = st.number_input("Enter the population mean:", value=0.0)
        t_stat, p_value = stats.ttest_1samp(sample_data, pop_mean)
    
    # Test for Equality of Means (Two-sample t-test)
    elif test_type == "Test for Equality of Means":
        t_stat, p_value = stats.ttest_ind(sample_data1, sample_data2)
    
    # Test for Proportions (Z-test)
    elif test_type == "Test for One or Two Proportions":
        z_stat, p_value = sm_proportion.proportions_ztest(count, nobs)
    
    # Test of Independence (Chi-Square)
    elif test_type == "Test of Independence (Chi-Square)":
        observed = np.array([[int(x) for x in st.text_area("Enter the observed frequency table (comma-separated rows)").split(',')],
                            [int(x) for x in st.text_area("Enter the observed frequency table (next row)").split(',')]])
        chi2, p_value, _, _ = stats.chi2_contingency(observed)
    
    # ANOVA (F-test)
    elif test_type == "Analysis of Variance (ANOVA)":
        f_stat, p_value = stats.f_oneway(sample_data1, sample_data2)
    
    # Shapiro Test (Normality)
    elif test_type == "Shapiro Test (Normality)":
        shapiro_stat, p_value = stats.shapiro(sample_data)
    
    # Levene Test (Equal Variances)
    elif test_type == "Levene Test (Equal Variances)":
        levene_stat, p_value = stats.levene(sample_data1, sample_data2)

    # Step 5: Compare p-value with alpha and display the result
    st.subheader("Test Results")
    st.write(f"Test Statistic: {t_stat if 't_stat' in locals() else (f_stat if 'f_stat' in locals() else shapiro_stat if 'shapiro_stat' in locals() else chi2 if 'chi2' in locals() else z_stat if 'z_stat' in locals() else levene_stat if 'levene_stat' in locals())}")
    st.write(f"P-value: {p_value}")
    
    if p_value < alpha:
        st.write("Since p-value < alpha, we reject the null hypothesis (H₀).")
    else:
        st.write("Since p-value ≥ alpha, we fail to reject the null hypothesis (H₀).")
