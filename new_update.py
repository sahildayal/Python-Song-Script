import pandas as pd

# Read Excel file
excel_file = "C:\\Users\\Sahil Dayal\\Desktop\\fundingtype\\Funding_Type_Script.xlsx"
df = pd.read_excel(excel_file)

# Group by Funding Type
grouped = df.groupby('FUNDING_TYPE')

# Function to generate SQL script for each group
def generate_sql_script(group_df, funding_type):
    sql_script = ""
    for index, row in group_df.iterrows():
        cli_client_id = row['CLI_CLIENT_ID']
        cs_subplan_code = row['CS_SUBPLAN_CODE']
        sql_script += f"OR (cs_clt_id = {cli_client_id} and cs_subplan_code = '{cs_subplan_code}')\n"
    with open(f"update_script_{funding_type.replace(' ', '').lower()}.txt", "w") as file:
        file.write(sql_script)

# Iterate over groups and generate SQL scripts
for name, group in grouped:
    generate_sql_script(group, name)
