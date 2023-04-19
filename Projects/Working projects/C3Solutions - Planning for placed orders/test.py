
import pandas as pd

# URL of the webpage to parse
url = 'https://c3solutions.ru/catalog/bloki-raspredeleniya-pitaniya/brp-s-upravleniem/'

# Use pandas to read the HTML table into a dataframe
df = pd.read_html(url)[0]

# Filter the dataframe to only include rows that contain 'C3.PS' in the item number column
df = df[df.iloc[:,0].str.contains('C3.PS')]

# Extract the columns of interest into a new dataframe with explicit column names
df_filtered = pd.DataFrame(data=df.iloc[:,[0,1,2,3,4]].values, columns=['Item Number', 'Description', 'Width', 'Length', 'Height'])

# Reset the index of the filtered dataframe
df_filtered = df_filtered.reset_index(drop=True)

# Print the filtered dataframe for testing
print(df_filtered)

# Save the filtered dataframe to a CSV file
df_filtered.to_csv('item_data.csv', index=False)