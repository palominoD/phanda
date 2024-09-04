import pandas as pd

print ('start execute main.py')

df = pd.read_csv('ap.csv')

# Obtiene los valores únicos de la columna "edad"
valores_unicos = df["LLDP"].unique()
# Imprime los valores únicos
print(valores_unicos)


filtered_df = df[df['LLDP'] == 'SW_PRINCIPAL']
print(filtered_df)

num_rows = len(filtered_df)
output_file = 'SW_PRINCIPAL.csv'
filtered_df.to_csv(output_file, index=False)
print(f"Found {num_rows} rows. Output saved to {output_file}.")
