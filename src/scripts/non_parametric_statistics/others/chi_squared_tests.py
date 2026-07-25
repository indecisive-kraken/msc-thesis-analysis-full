import pandas as pd
import scipy.stats as stats

data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='INDIV_VAR_REG')

print(df.info())
df.head()

# user_dataframe = df[['Q1', 'Q2', 'D1', 'D2', 'D3', 'D4', 'BSMAS', 'Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
#         'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
#         'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

usr_df = df[['Q1','Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
        'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
        'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N', 'BSMAS']]


#Made it a function so that it can be called multiple times and for multiple instances

def contingency_table_generator():

    try:
        initial_column = str(input("Please input the column name: "))
        print("Inputted Column: ", initial_column)
    except:
        print('The provided column was not found in the dataframe')

    index_initial_col = usr_df.columns.get_loc(initial_column)
    print("The index of the initial column: ", index_initial_col)

    df1 = usr_df.iloc[:, :index_initial_col]
    df2 = usr_df.iloc[:, index_initial_col:]
    index_arr1 = list([df1.columns.get_loc(c) for c in df1.columns if c in df1])
    index_arr2 = list(df2.columns.get_loc(c) for c in df2.columns if c in df2)
    index_initial_df = list(usr_df.columns.get_loc(c) for c in usr_df.columns if c in usr_df)

    index_arr = [index_arr1, index_arr2]

    print(df1)
    print(df2)
    print(index_arr1)
    print(index_arr2)

    index_counter = index_initial_col
    index_counter_2 = index_initial_col
    check_edge_case = index_counter_2 ## -here! find an alternative logical condition
    edge_case_increment = 0

    for ind in index_arr:

        print("Check", ind)
        # print("Testing", df1.columns[index_counter - 1], type(df1.columns[index_counter - 1]))

        print("Check and the columns of all dataframes")

        print(df1.info())
        print(df2.info())

        # You have an array like object (dataframe) that you want to split, needs edge case handling and index_counter_2 != check_edge_case
        # example: target column for the split
        #   ic -=1  <-|->  ic += 1
        #  |q1|q2|q3|q4|q5|q6|q7|q8|...
        #   .. .. .. .. .. .. .. ..
        #   .. .. .. .. .. .. .. ..

        df1['BSMAS'] = df2.iloc[:, 0].copy()

        if index_initial_col > 0:

            while index_counter > 0:

                cont = pd.crosstab(index=df1[df1.columns[index_initial_col]], columns=df1[df1.columns[index_counter - 1]])
                print(cont)
                res = stats.chi2_contingency(cont)

                print("Results of first dataframe: \n", res)

                index_counter -= 1

            while index_counter_2 > 0:

                cont2 = pd.crosstab(index=df2[df2.columns[0]], columns=df2[df2.columns[len(index_arr2) -1]])
                print(cont2)
                res2 = stats.chi2_contingency(cont2)

                print("Results of the second dataframe: \n", res2)

                index_counter_2 -= 1

        else:

            while edge_case_increment < len(index_initial_df) :

                cont = pd.crosstab(index=usr_df[usr_df.columns[0]], columns=usr_df[usr_df.columns[edge_case_increment + 1]])
                print(cont)

                res = stats.chi2_contingency(cont)

                print("Results of the initial dataframe (edge case, first element): \n", res)
                edge_case_increment += 1

        print("Index Counters before decrementing", index_counter, index_counter_2)

        print("Index Counters after decrementing", index_counter, index_counter_2)


contingency_table_generator()

#and index_counter != 0