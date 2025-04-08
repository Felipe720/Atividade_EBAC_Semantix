import pandas as pd
from sklearn.preprocessing import LabelEncoder


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv(r'C:\Users\Felip\Downloads\Ecommerce_Consumer_Behavior_Analysis_Data.csv')
print(df.head())

print(df.shape)
print(df.dtypes)
print('Valores Nulos:\n', df.isnull().sum())

df_tratado = df.fillna('Unknown')
print('Valores Nulos:\n', df_tratado.isnull().sum())

ensino = df_tratado['Education_Level'].unique()
print(ensino)

education_ordem = {"Bachelor's": 1, "High School": 2, "Master's": 3}
df_tratado['Education_Level_Ord'] = df['Education_Level'].map(education_ordem)

label_encoder = LabelEncoder()
df_tratado['Gender_cod'] = label_encoder.fit_transform(df['Gender'])
df_tratado['Marital_Status_cod'] = label_encoder.fit_transform(df['Marital_Status'])

df_tratado['Purchase_Amount'] = df_tratado['Purchase_Amount'].str.replace('$', '', regex=False)
df_tratado['Purchase_Amount'] = df_tratado['Purchase_Amount'].astype(float)


bins = [17, 23, 29, 35, 41, 47, 60]
labels = ['18-23', '24-29', '30-35', '36-41', '42-47', '48-60']
df_tratado['Age_range'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df_tratado.dtypes)
print(df_tratado['Purchase_Amount'].sum())
print(df_tratado.head())


print('Correlação: \n',df_tratado[['Purchase_Amount', 'Age','Gender_cod', 'Marital_Status_cod','Education_Level_Ord', 'Frequency_of_Purchase', 'Time_Spent_on_Product_Research(hours)', 'Customer_Satisfaction', 'Return_Rate']].corr())

df_tratado.to_csv('Df_tratado.csv', index=False)