import pandas as pd

columns = ["client_name", "project_type", "price", "is_completed"]
df = pd.read_csv("C:/Users/LOQ/DesignTracker/projects.txt", names=columns)
print(df)
total_price = df['price'].sum()
completed_projects = df[df['is_completed'] == False]
sorted_df = completed_projects.sort_values(by='price', ascending=False)
print(total_price)
print(completed_projects)
print(sorted_df)
 