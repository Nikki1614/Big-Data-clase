
import pandas as pd

# URL del dataset
url = "http://cicresearch.ca/CICDataset/CICDarknet2020/Dataset/Darknet.CSV"


df = pd.read_csv(url)

#print(df.head())
#print(df.info())


#df1=df.dropna() #Elimina campos con celdas que esten vacias
#print(len(df))
#print(len(df1))
df2=df.fillna("Vacio") #Llena los campos vacios
df2["Timestamp"]= pd.to_datetime(df2["Timestamp"])

print(df2["Timestamp"])
df2["Flow ID"] = df2["Flow ID"].astype(str)
df2["Src IP"] = df2["Src IP"].astype(str)
df["Dst IP"]=df2["Dst IP"].astype(str)
df2["Timestamp"]= pd.to_datetime(df2["Timestamp"])

df2["Label"]=df2["Label"].astype('category')
df2["Label"]=df2["Label"].astype('category')

#Tipos modificados despues de conversión
print(df2.dtypes)
#Verificar si esta convirtiendo los objetos en string

print(df["Flow ID"].apply(type).value_counts())
print(df["Dst IP"].apply(type).value_counts())
print(df["Src IP"].apply(type).value_counts())

df2.to_csv("Darknetlimpio.csv", index=False)
