# STEP 1A
# Import SQL Library and Pandas
import sqlite3  
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


employee_data = pd.read_sql("""SELECT * FROM employees""", conn)

print(employee_data.columns.tolist())


print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Replace None with your code
df_first_five = employee_data[["employeeNumber", "lastName"]]

# STEP 3
# Replace None with your code
df_five_reverse = employee_data[["lastName", "employeeNumber"]]

# STEP 4
# Replace None with your code
df_alias = employee_data[["lastName","employeeNumber"]].rename(columns={"employeeNumber":"ID"})

# STEP 5
# Replace None with your code
df_executive = employee_data.assign(
    role=employee_data["jobTitle"].apply(
        lambda x: "Executive" if x in [
            "President",
            "VP Sales",
            "VP Marketing"
        ] else "Not Executive"
    )
)

# STEP 6
# Replace None with your code
df_name_length = employee_data[["lastName"]].assign(
    name_length=employee_data["lastName"].str.len()
)[["name_length"]]

# STEP 7
# Replace None with your code
df_short_title = employee_data[["jobTitle"]].assign(
    short_title=employee_data["jobTitle"].str[:20]
)[["short_title"]]

# STEP 8
# Replace None with your code
total_amount = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered, 2)) AS total_amount
    FROM orderDetails;
""", conn)

# STEP 9
# Replace None with your code
df_day_month_year = 