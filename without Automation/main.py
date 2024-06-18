import pandas as pd
import os

parent_csv_path = '/content/housing.csv'
parent_df = pd.read_csv(parent_csv_path)

parent_df.head()

child_columns = {
    'child1.csv': ['longitude', 'latitude'],
    'child2.csv': ['housing_median_age', 'total_rooms'],
    'child3.csv': ['total_bedrooms', 'longitude'],
    # Add more child CSV definitions here if needed
}

for child_csv, columns in child_columns.items():
    if all(col in parent_df.columns for col in columns):
        child_df = parent_df[columns]
        child_df.to_csv(child_csv, index=False)
    else:
        print(f"One or more columns in {columns} are not in the parent CSV")

def update_child_csvs(parent_csv_path, child_columns):
    parent_df = pd.read_csv(parent_csv_path)
    
    for child_csv, columns in child_columns.items():
        if all(col in parent_df.columns for col in columns):
            child_df = parent_df[columns]
            child_df.to_csv(child_csv, index=False)
        else:
            print(f"One or more columns in {columns} are not in the parent CSV")

parent_df.at[0, 'longitude'] = 122.25
parent_df.to_csv(parent_csv_path, index=False)


update_child_csvs(parent_csv_path, child_columns)


child1_df = pd.read_csv('child1.csv')
print(child1_df)
child2_df = pd.read_csv('child2.csv')
print(child2_df)
child3_df = pd.read_csv('child3.csv')
print(child3_df)
