import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("DATA")
Age_dict = {}

for label, condition in age_bins.items():
    df = Age_Sorted.loc[condition]

    if df.empty:
        continue  # Skip if no data in this group

    # Compute descriptive stats for all numeric columns
    mean = df.mean(numeric_only=True)
    mode = df.mode(numeric_only=True).iloc[0] if not df.mode(numeric_only=True).empty else None
    std = df.std(numeric_only=True)

    # Store in dictionary
    Age_dict[label] = {
        'mean': mean,
        'mode': mode,
        'std': std
    }

    # Convert to DataFrame and export
    stats_df = pd.DataFrame({
        'mean': mean,
        'mode': mode,
        'std': std
    })
    stats_df.to_csv(f'desc_stats_per_age_group{label}.csv')

# Optional: Combine all stats into one summary DataFrame
resultsdf14 = pd.concat({
    label: pd.DataFrame(stats) for label, stats in Age_dict.items()
}, names=['Age_Group', 'Statistic'])

resultsdf14.to_csv('summary_stats_all_groups.csv')

import pandas as pd

# Assuming your original DataFrame is called `all`
# and it includes the relevant education and employment columns

# Define the education and employment indicator columns
education_cols = ['Education_L', 'Education_P', 'Education_Highest']
employment_cols = ['Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth']

# ---------- Loop 1: Education ----------
education_stats = {}

for col in education_cols:

    if all[col].values == 1 and all[col].values == 0:
        df_edu_1 = all[all[col + "only 1s"] == 1]  # Filter where this education level applies
        df_edu_0 = all[all[col + "only 0s"] == 0]

    if df_edu_1.empty or df_edu_0.empty:
        continue  # Skip if no data in this group

    mean = df_edu_1.mean(numeric_only=True)
    mode = df_edu_1.mode(numeric_only=True).iloc[0] if not df_edu_1.mode(numeric_only=True).empty else None
    std = df_edu_1.std(numeric_only=True)

    mean_0 = df_edu_0.mean(numeric_only=True)
    mode_0 = df_edu_0.mode(numeric_only=True).iloc[0] if not df_edu_1.mode(numeric_only=True).empty else None
    std_0 = df_edu_0.std(numeric_only=True)

    education_stats[col] = {
        'mean': mean,
        'mode': mode,
        'std': std
    }

    # Save individual CSV for this education group
    edu_stats_df = pd.DataFrame({
        'mean': mean,
        'mode': mode,
        'std': std
    })
    edu_stats_df.to_csv(f'desc_stats_education_yes{col}.csv')

    education_stats[col] = {
        'mean': mean_0,
        'mode': mode_0,
        'std': std_0
    }

    # Save individual CSV for this education group
    edu_stats_df = pd.DataFrame({
        'mean': mean_0,
        'mode': mode_0,
        'std': std_0
    })
    edu_stats_df.to_csv(f'desc_stats_education_no{col}.csv')

# Optional combined summary
combined_edu_df = pd.concat({
    col: pd.DataFrame(stats) for col, stats in education_stats.items()
}, names=['Education_Level', 'Statistic'])

combined_edu_df.to_csv('summary_stats_education_all.csv')


# ---------- Loop 2: Employment ----------
employment_stats = {}

for col in employment_cols:
    df_emp = all[all[col] == 1]  # Filter where this employment status applies

    if df_emp.empty:
        continue  # Skip if no data in this group

    mean = df_emp.mean(numeric_only=True)
    mode = df_emp.mode(numeric_only=True).iloc[0] if not df_emp.mode(numeric_only=True).empty else None
    std = df_emp.std(numeric_only=True)

    employment_stats[col] = {
        'mean': mean,
        'mode': mode,
        'std': std
    }

    # Save individual CSV for this employment group
    emp_stats_df = pd.DataFrame({
        'mean': mean,
        'mode': mode,
        'std': std
    })
    emp_stats_df.to_csv(f'desc_stats_employment_{col}.csv')

# Optional combined summary
combined_emp_df = pd.concat({
    col: pd.DataFrame(stats) for col, stats in employment_stats.items()
}, names=['Employment_Status', 'Statistic'])

combined_emp_df.to_csv('summary_stats_employment_all.csv')