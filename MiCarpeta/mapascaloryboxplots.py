import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set(style="whitegrid")

file_path = "/Users/alansantana/Documents/Herramients_Computacionales/Facebook_Marketplace_data.csv"
df = pd.read_csv(file_path)
df.head()

print(df.columns.tolist())

#print("Info del DataFrame")
#df.info()

df_clean = df.copy()
if 'Unnamed: 0' in df_clean.columns:
    df_clean = df_clean.drop(columns=['Unnamed: 0'])

order_by_reactions = df_clean.groupby('num_shares')['num_reactions'].median().sort_values(ascending=False).index
order_by_comments = df_clean.groupby('num_shares')['num_comments'].median().sort_values(ascending=False).index
print('Columnas finales:', df_clean.columns.tolist())
print('Shares (top 5 by reactions):', list(order_by_reactions)[:5])

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_clean, x='num_reactions', y='num_shares')
plt.title('Boxplot of Number of Reactions vs Number of Shares')
plt.xlabel('Number of Reactions')
plt.xticks(rotation=90)
plt.ylabel('Number of Shares')
plt.show()

plt.hist(df_clean['num_reactions'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Number of Reactions')
plt.xlabel('Number of Reactions')
plt.ylabel('Frequency')
plt.show()

corr = df_clean[["num_reactions", "num_comments", "num_shares", "num_likes"]].corr()
corr

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de calor de correlaciones")
plt.show()