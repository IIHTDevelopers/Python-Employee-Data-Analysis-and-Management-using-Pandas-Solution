import pandas as pd


class EmployeeAnalysis:
    def __init__(self, file_path):
        """Load CSV data into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def highest_age_employee(self):
        """Find the employee ID with the highest age."""
        max_age = self.df.loc[self.df["Age"].idxmax(), "Name"]
        return max_age

    def filter_sales_department(self):
        """Filter the DataFrame to show employees in the Sales department."""
        return self.df[self.df["Department"] == "Sales"]

    def add_age_category(self):
        """Add a new column 'Age Category' to the DataFrame."""
        bins = [0, 30, 40, float('inf')]
        labels = ['Young', 'Mid-aged', 'Old']
        self.df["Age Category"] = pd.cut(self.df["Age"], bins=bins, labels=labels)

    def export_updated_csv(self, output_file="updated_employee_data.csv"):
        """Save the updated DataFrame to a new CSV file."""
        self.df.to_csv(output_file, index=False)
