import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import reshape
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from scripts.data.get_data_path import open_data_file

def t_SNE_Visual():

        df = open_data_file()
        y = df[['Q1']]
        x1 = df[['Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
                'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
                'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

        # x2 = df['Q2', 'Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6']

        all = df[['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','BSMAS1','BSMAS2','BSMAS3','BSMAS4','BSMAS5','BSMAS6','Gender', 'Education_L', 'Education_P', 'Education_Highest', 'Age_Group',
                'Time_Spent_M', 'Time_Spent_H', 'Empl_st_sfemp', 'Empl_st_employee', 'Empl_st_st', 'Empl_st_oth',
                'Instagram_index', 'Facebook_index', 'TikTok_index', 'H_Problem', 'Attach_S', 'Attach_S_N']]

        standardized_x = StandardScaler().fit_transform(x1)
        standardized_y = StandardScaler().fit_transform(y)

        # print(x_split.info())
        # print(y_split.info())

        tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=500)
        z = tsne.fit_transform(standardized_x)

        df = pd.DataFrame()
        df["y"] = np.arange(0,len(standardized_y),1)
        df["comp-1"] = z[:, 0]
        df["comp-2"] = z[:, 1]


        sns.scatterplot(data = df, x="comp-1", y="comp-2", hue=df.y.tolist(), palette = sns.color_palette("hls", 3)).set(title="Iris data T-SNE projection")

        plt.title('T-SNE scatterplot')
        plt.tight_layout()
        plt.savefig("TSNE2.png")

        # df_all = pd.DataFrame()
        # df_all["y"] = y
        # df_all["comp-1"] = z[:,0]
        # df_all["comp-2"] = z[:,1]
        #
        # sns.scatterplot(x="comp-1", y="comp-2", hue=df_all.y.tolist(), palette = sns.color_palette("hls",4), data=df_all).set(title="All variables QoL")
        # plt.title("t-SNE of all vars")
        # plt.savefig("t-sne_visual_2nd.png")


t_SNE_Visual()