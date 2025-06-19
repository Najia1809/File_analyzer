# Text & CSV File Analyzer

An intelligent and interactive file analyzer built using Streamlit. This web app allows users to upload `.txt` or `.csv` files, login securely, and analyze the content through various on-click functions such as statistics, graphs, preprocessing, and more.

## Features

- User Authentication (Login & Signup)
- File Upload (`.txt` and `.csv`)
- Analysis
  - Line Count
  - Word Count
  - Character Count
  - Head & Tail
  - Descriptive Statistics
  - Null Value Cleaning
  - Dynamic Histogram Graph
- Smart button-based logic for both file types

## Dataset Used

For demonstration, a small HR Dataset (50 rows) is used, containing the following columns:

- EmployeeID
- Department
- Gender
- Age
- Salary
- PerformanceScore

This dataset simulates real-world employee data for presenting meaningful analysis.

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- JSON (for user storage)

## File Structure

project/
|
├── main.py             # Main Streamlit App Launcher
├── login.py            # Login screen logic
├── signup.py           # Signup page logic
├── analyzer.py         # Core logic for file analysis
├── users.json          # Stores usernames and passwords

## Created By

Najia Khan  
BS Artificial Intelligence — 2st Semester  
Project: File Analyzer with Streamlit
