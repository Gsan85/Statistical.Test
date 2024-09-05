import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.stats.proportion as smprop

def main():
    st.title("Statistical Test Selector and Calculator")

    # Step 1: Determine the type of data and research question
    test_type = st.selectbox(
        "What type of test do you want to perform?",
        ["Test for one mean", "Test for equality of means", "Test for one proportion", 
         "Test for equality of proportions", "Test of independence", "Analysis of Variance (ANOVA)"]
    )

    # Step 2: Select the appropriate test
    if test_type == "Test for one mean":
        perform_one_sample_ttest()
    elif test_type == "Test for equality of means":
        perform_two_sample_ttest()
    elif test_type == "Test for one proportion":
        perform_one_sample_proportion_test()
    elif test_type == "Test for equality of proportions":
        perform_two_sample_proportion_test()
    elif test_type == "Test of independence":
        perform_chi_square_test()
    elif test_type == "Analysis of Variance (ANOVA)":
        perform_anova()

def perform_one_sample_ttest():
    st.subheader("One-Sample T-Test")

    # Step 3: Formulate hypotheses
    st.write("Null Hypothesis (H0): The sample mean is equal to the population mean.")
    st.write("Alternative Hypothesis (H1): The sample mean is not equal to the population mean.")

    # Step 4: Set significance level
    alpha = st.number_input("Enter the significance level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01)

    # Step 5: Collect data
    data = st.text_input("Enter the sample data (comma-separated values)")
    pop_mean = st.number_input("Enter the population mean")

    if st.button("Perform Test"):
        # Step 6: Perform the test
        if data:
            sample = np.array([float(x.strip()) for x in data.split(',')])
            t_statistic, p_value = stats.ttest_1samp(sample, pop_mean)

            # Step 7: Compare p-value and draw conclusion
            st.write(f"T-statistic: {t_statistic}")
            st.write(f"P-value: {p_value}")
            
            if p_value < alpha:
                st.write("Conclusion: Reject the null hypothesis.")
                st.write("There is significant evidence to suggest that the sample mean is different from the population mean.")
            else:
                st.write("Conclusion: Fail to reject the null hypothesis.")
                st.write("There is not enough evidence to suggest that the sample mean is different from the population mean.")

def perform_two_sample_ttest():
    st.subheader("Two-Sample T-Test")

    st.write("Null Hypothesis (H0): The means of the two populations are equal.")
    st.write("Alternative Hypothesis (H1): The means of the two populations are not equal.")

    alpha = st.number_input("Enter the significance level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01)

    data1 = st.text_input("Enter the first sample data (comma-separated values)")
    data2 = st.text_input("Enter the second sample data (comma-separated values)")

    if st.button("Perform Test"):
        if data1 and data2:
            sample1 = np.array([float(x.strip()) for x in data1.split(',')])
            sample2 = np.array([float(x.strip()) for x in data2.split(',')])
            t_statistic, p_value = stats.ttest_ind(sample1, sample2)

            st.write(f"T-statistic: {t_statistic}")
            st.write(f"P-value: {p_value}")
            
            if p_value < alpha:
                st.write("Conclusion: Reject the null hypothesis.")
                st.write("There is significant evidence to suggest that the means of the two populations are different.")
            else:
                st.write("Conclusion: Fail to reject the null hypothesis.")
                st.write("There is not enough evidence to suggest that the means of the two populations are different.")

def perform_one_sample_proportion_test():
    st.subheader("One-Sample Proportion Test")

    st.write("Null Hypothesis (H0): The sample proportion is equal to the hypothesized population proportion.")
    st.write("Alternative Hypothesis (H1): The sample proportion is not equal to the hypothesized population proportion.")

    alpha = st.number_input("Enter the significance level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01)

    count = st.number_input("Enter the number of successes", min_value=0, step=1)
    nobs = st.number_input("Enter the total number of observations", min_value=1, step=1)
    value = st.number_input("Enter the hypothesized population proportion", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    if st.button("Perform Test"):
        z_statistic, p_value = smprop.proportions_ztest(count, nobs, value)

        st.write(f"Z-statistic: {z_statistic}")
        st.write(f"P-value: {p_value}")
        
        if p_value < alpha:
            st.write("Conclusion: Reject the null hypothesis.")
            st.write("There is significant evidence to suggest that the sample proportion is different from the hypothesized population proportion.")
        else:
            st.write("Conclusion: Fail to reject the null hypothesis.")
            st.write("There is not enough evidence to suggest that the sample proportion is different from the hypothesized population proportion.")

def perform_two_sample_proportion_test():
    st.subheader("Two-Sample Proportion Test")

    st.write("Null Hypothesis (H0): The proportions in the two populations are equal.")
    st.write("Alternative Hypothesis (H1): The proportions in the two populations are not equal.")

    alpha = st.number_input("Enter the significance level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01)

    count1 = st.number_input("Enter the number of successes in sample 1", min_value=0, step=1)
    nobs1 = st.number_input("Enter the total number of observations in sample 1", min_value=1, step=1)
    count2 = st.number_input("Enter the number of successes in sample 2", min_value=0, step=1)
    nobs2 = st.number_input("Enter the total number of observations in sample 2", min_value=1, step=1)

    if st.button("Perform Test"):
        z_statistic, p_value = smprop.proportions_ztest([count1, count2], [nobs1, nobs2])

        st.write(f"Z-statistic: {z_statistic}")
        st.write(f"P-value: {p_value}")
        
        if p_value < alpha:
            st.write("Conclusion: Reject the null hypothesis.")
            st.write("There is significant evidence to suggest that the proportions in the two populations are different.")
        else:
            st.write("Conclusion: Fail to reject the null hypothesis.")
            st.write("There is not enough evidence to suggest that the proportions in the two populations are different.")

def perform_chi_square_test():
    st.subheader("Chi-Square Test of Independence")

    st.write("Null Hypothesis (H0): There is no association between the two categorical variables.")
    st.write("Alternative Hypothesis (H1): There is an association between the two categorical variables.")

    alpha = st.number_input("Enter the significance level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01)

    st.write("Enter the contingency table data:")
    rows = st.number_input("Number of rows", min_value=2, value=2, step=1)
    cols = st.number_input("Number of columns", min_value=2, value=2, step=1)

    data = []
    for i in range(rows):
        row = st.text_input(f"Enter data for row {i+1} (comma-separated values)")
        if row:
            data.append([int(x.strip()) for x in row.split(',')])

    if st.button("Perform Test") and len(data) == rows:
        chi2, p_value, dof, expected = stats.chi2_contingency(data)

        st.write(f"Chi-square statistic: {chi2}")
        st.write(f"P-value: {p_value}")
        st.write(f"Degrees of freedom: {dof}")
        
        if p_value < alpha:
            st.write("Conclusion: Reject the null hypothesis.")
            st.write("There is significant evidence to suggest an association between the two categorical variables.")
        else:
            st.write("Conclusion: Fail to reject the null hypothesis.")
            st.write("There is not enough evidence to suggest an association between the two categorical variables.")

def perform_anova():
    st.subheader("One-Way ANOVA")

    st.write("Null Hypothesis (H0): The means of all groups are equal.")
    st.write("Alternative Hypothesis (H1): At least one group mean is different from the others.")

    alpha = st.number_input("Enter the significance level (alpha)", min_value=0.01, max_value=0.1, value=0.05, step=0.01)

    num_groups = st.number_input("Enter the number of groups", min_value=2, value=3, step=1)

    groups = []
    for i in range(num_groups):
        group = st.text_input(f"Enter data for group {i+1} (comma-separated values)")
        if group:
            groups.append([float(x.strip()) for x in group.split(',')])

    if st.button("Perform Test") and len(groups) == num_groups:
        f_statistic, p_value = stats.f_oneway(*groups)

        st.write(f"F-statistic: {f_statistic}")
        st.write(f"P-value: {p_value}")
        
        if p_value < alpha:
            st.write("Conclusion: Reject the null hypothesis.")
            st.write("There is significant evidence to suggest that at least one group mean is different from the others.")
        else:
            st.write("Conclusion: Fail to reject the null hypothesis.")
            st.write("There is not enough evidence to suggest that any group mean is different from the others.")

if __name__ == "__main__":
    main()
