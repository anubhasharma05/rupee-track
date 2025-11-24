# rupee-track
This project is a simple and efficient Expense Tracking System built using Python, Pandas, and Matplotlib. It allows users to record, categorize, and analyze their daily expenses in Indian Rupees (INR).  The program begins by generating a sample dataset of common expenses. These sample records are saved into a CSV file show how the system works.
 RUPEE TRACK (PYTHON PROJECT)

(1) Overview
This Python-based application serves as a simple and functional Expense Tracking System, designed to help users record, organize, and analyze their day-to-day expenditures. The project demonstrates essential Python programming concepts, including file handling, data processing, functions, basic automation, and the integration of external libraries such as Pandas and Matplotlib.

The system is capable of creating sample expense data in INR, loading user-provided expense files, converting date formats, extracting monthly spending patterns, and categorizing expenses based on their descriptions. The project provides a modular foundation suitable for academic demonstrations, further enhancements, or practical personal finance management.

(2) Key Functionalities

1. Sample Data Generation
Automatically creates a CSV file (sample_expenses.csv) containing example expense entries in INR.
Helps in testing and understanding the data format.

2. Data Loading & Processing
Reads an external CSV file containing expense records.
Converts date values to Python datetime format.
Extracts the corresponding month from each expense entry.
Categorizes expenses (e.g., groceries, fuel, dining) based on the description field.

3. Error Handling
If the CSV file is missing, the program safely initializes an empty dataset without crashing.

4. Modular Design
Functions are separated into logical units for better readability and reusability.
Suitable for extension into a full budgeting or visualization system.  

(3) Technologies / Libraries Used
1. Python 3.x — Core programming language
2. Pandas — For data manipulation and analysis
3. Matplotlib — For plotting and visualization (extendable by user)
4. OS Module — For file path handling (optional use)

(4) Steps to Install & Run the Project

4.1 Install Dependencies
Open a terminal / command prompt and install the required external libraries:
pip install pandas matplotlib

4.2 Project Files
Ensure the following Python file(s) are present in your project directory:
main.py or any file containing the functions:
create_sample_data()
load_and_process_data()
categorize_expense() (user-defined)

These functions handle the core functionality of the project.

4.3 Running the Application
1. Execute the Python script in your terminal/IDE:
python main.py

2. From the program, you may:
Generate sample expenses
Load and process a CSV file
Display the processed DataFrame
Extend the script to show graphs or summaries

(5) Example Functions Used

5.1 Sample Data Function
Creates sample expenses in INR and saves them as sample_expenses.csv.

5.2 Data Processing Function
Loads the CSV file, converts dates, extracts months, and applies categorization.

5.3 Categorization Function
Maps textual descriptions to defined categories (e.g., Food, Transport, Café, etc.).

(6) Possible Extensions
The current implementation can be enhanced with:

1. Monthly Spending Summary
2. Category-wise Pie Charts / Bar Charts
3. Budget Alerts
4. GUI Application (Tkinter / PyQt)
5. Exporting Reports to PDF
6. Database Integration (SQLite / MySQL)

(7) Conclusion
This project provides a clear and practical introduction to data handling and analysis in Python. It demonstrates real-world applications of Pandas, file processing, modular function design, and basic visualization. The system serves as a strong base for both academic projects and personal use, offering flexibility for future improvements.
