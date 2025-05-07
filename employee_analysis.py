
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Extended_Employee_Performance_and_Productivity_Data.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Convert hire_date to datetime
df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')

# Create Month-Year column
df['hire_month'] = df['hire_date'].dt.to_period('M')

# Basic stats
print("Summary Statistics:")
print(df.describe())

# Average performance score per department
dept_perf = df.groupby('department')['performance_score'].mean().sort_values()
print("\nDepartment-wise Performance:\n", dept_perf)

# Line chart - Monthly performance trend
monthly_perf = df.groupby('hire_month')['performance_score'].mean()
monthly_perf.plot(marker='o', title='Monthly Average Performance Score', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Avg Performance Score")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_performance_trend.png")
plt.close()

# Bar chart - Department performance
dept_perf.plot(kind='barh', color='skyblue', title='Avg Performance by Department', figsize=(8,5))
plt.xlabel("Average Score")
plt.tight_layout()
plt.savefig("department_performance.png")
plt.close()

# Correlation heatmap
numerics = df.select_dtypes(include='number')
plt.figure(figsize=(10, 8))
sns.heatmap(numerics.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()
