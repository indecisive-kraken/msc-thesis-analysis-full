import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D


# 1. -- Check if the file is of valid type, after that Pandas loads the data -- (you can add more file suffixes with an additional if statement and with filepaths = ['.xlsx', 'xlsm',])
data = input('Please specify the Excel file with the data: ')
df = pd.read_excel(data, sheet_name='ENCODED_DATA')
y = df['Q1']

scaling = StandardScaler()
scaling.fit(df)

Scaled_data = scaling.transform(df)

principal = PCA(0.9999999999)
principal = principal.fit(Scaled_data)

x = principal.fit_transform(Scaled_data)

print(x.shape)

explained_variance = principal.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

for i, var_ratio in enumerate(explained_variance):
    print(f"PC{i+1}: {var_ratio:.4f} (Cumulative: {cumulative_variance[i]:.4f}")

print(principal.explained_variance_ratio_)

# Get the loadings
loadings = principal.components_.T  # shape: (n_features, n_components)

# Combine with feature names
for i, component in enumerate(loadings.T):
    print(f'\nPrincipal Component {i+1}:')
    for feature, loading in zip(df, component):
        print(f'{feature}: {loading:.3f}')
print(loadings)


#Importance

# Get squared loadings
squared_loadings = principal.components_.T ** 2  # shape: (n_features, n_components)

# Weight squared loadings by the explained variance ratio
# Each variable's importance is the weighted sum of squared loadings across all components
variable_importance = np.sum(squared_loadings * principal.explained_variance_ratio_, axis=1)

# Now you have the total importance score for each variable
for i, importance in enumerate(variable_importance):
    print(f"Variable {i+1}: Importance {importance:.4f}")

plt.figure(figsize=(10,10))
plt.scatter(x,y)

fig = plt.figure(figsize=(10,10))
axis = fig.add_subplot(111, projection='3d')

axis.scatter(principal[:, 0], principal[:, 1], principal[:, 2])
axis.set_xlabel('PC1')
axis.set_ylabel('PC2')
axis.set_zlabel('PC3')
plt.title('3D PCA Plot (First 3 Principal Components')
plt.show