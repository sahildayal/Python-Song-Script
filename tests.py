import pandas as pd

# Load Excel file
excel_file = r"C:\Users\Sahil Dayal\Desktop\fundingtype\Funding_Type_Script.xlsx"
df = pd.read_excel(excel_file)

# Mapping of Funding Type to Funding Type Code
funding_type_mapping = {
    'Community Rated': 'COM',
    'Experience Rated': 'EXP',
    'Level Funded': 'LVL',
    'Self Funded': 'SFD',
    'Reference Based Pricing': 'RBP',
    'Other': 'OTH',
    'Undefined': 'UND'
}

# Group entries by Funding Type
grouped_entries = df.groupby('FUNDING_TYPE')

# Open SQL script file for writing
sql_script_file = "update_script_latest.sql"
with open(sql_script_file, 'w') as sql_file:
    # Set up SQL script header
    sql_file.write("ALTER SESSION SET CURRENT_SCHEMA=PAI;\n")
    sql_file.write("SET VERIFY OFF;\n")
    sql_file.write("SPOOL update_script.log;\n")
    sql_file.write("-- UPDATE PAI.CLT_SUBPLAN\n")

    # Initialize total rows count
    total_rows_count = 0
    
    # Iterate over each group
    for funding_type, group in grouped_entries:
        # Initialize rows count for this group
        rows_count = 0

        # Generate the list of (CS_CLT_ID, CS_SUBPLAN_CODE) tuples for this group
        id_tuples = group.apply(lambda row: f"({row['CLI_CLIENT_ID']}, '{row['CS_SUBPLAN_CODE']}')", axis=1).tolist()
        id_tuples_str = ', '.join(id_tuples)

        # Calculate number of chunks
        chunk_size = 1000
        num_chunks = -(-len(id_tuples) // chunk_size)

        # Generate SQL UPDATE statement for this group with chunks
        for i in range(num_chunks):
            chunk_start = i * chunk_size
            chunk_end = min((i + 1) * chunk_size, len(id_tuples))
            chunk_id_tuples_str = ', '.join(id_tuples[chunk_start:chunk_end])
            where_clause = f"(CS_CLT_ID, CS_SUBPLAN_CODE) IN ({chunk_id_tuples_str})"
            if i > 0:
                sql_file.write(" OR ")
            else:
                sql_file.write("WHERE\n(")
            sql_file.write(where_clause)
            rows_count += chunk_end - chunk_start

        # Generate SQL UPDATE statement for this group
        funding_type_code = funding_type_mapping[funding_type]
        sql_update = f")\n)\nAND CS_FTR_CODE <> '{funding_type_code}';\n\n"
        sql_file.write(f"UPDATE PAI.CLT_SUBPLAN SET CS_FTR_CODE = '{funding_type_code}'\n")
        sql_file.write(sql_update)

        # Add rows count for this group to total rows count
        total_rows_count += rows_count

    # Write additional SQL statements
    sql_file.write("SPOOL OFF;\n")

print("SQL script generation completed.")
