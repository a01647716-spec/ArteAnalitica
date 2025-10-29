import pandas as pd
file_path = "/Users/alansantana/Documents/Herramients_Computacionales/spotify.csv"
df = pd.read_csv(file_path)
df.head()

print("Info del DataFrame")
df.info()
print("df.describe")
df.describe
print("columnas del DataFrame:")
df.columns
#print("conteo de tipos de contenido")
#conteo_tipo = df['type'].value_counts
#print conteo_año

# Valores nulos por columna
print("Valores nulos por columna:")
valores_nulos = df.isnull().sum()
print(valores_nulos)

df.shape

top_artists = df['artists'].value_counts().head(10)
print(top_artists)

media = df['popularity'].mean()
mediana = df['popularity'].median()
moda = df['popularity'].mode()[0]
desviacion_estandar = df['popularity'].std()
print("Estadísticas descriptivas de la columna 'popularity':")
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}, Desviación Estándar: {desviacion_estandar}")  

media = df['duration_ms'].mean()
mediana = df['duration_ms'].median()
moda = df['duration_ms'].mode()[0]
desviacion_estandar = df['duration_ms'].std()
print("Estadísticas descriptivas de la columna 'duration_ms':")
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}, Desviación Estándar: {desviacion_estandar}")  

