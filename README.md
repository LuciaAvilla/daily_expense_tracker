# Daily Expense Tracker 

A simple and efficient command-line interface (CLI) application built with **Python** to help users monitor their daily spending. This project was developed as part of my studies in **Systems Analysis and Development**.

## Features

* **Add Expenses:** Input daily costs as floating-point numbers.
* **View History:** List all recorded expenses with automatic indexing.
* **Financial Insights:** Calculate the total sum and the average of all expenses.
* **Data Management:** Option to clear all records or exit the system safely.
* **User-Friendly Flow:** Includes "Press Enter" pauses to improve readability in the terminal.

## Technologies Used

* **Python 3.x**

## Concepts applied: 
    * While Loops (Main Application Loop)
    * List Manipulation (`append`, `clear`, `sum`, `len`)
    * String Formatting (f-strings)
    * Input handling and Type Casting (`float`)

##  How to Run

1. **Clone the repository:**
  * git clone [https://github.com/LuciaAvilla/daily_expense_tracker.git](https://github.com/LuciaAvilla/daily_expense_tracker.git)
2. **Navigate to the project folder:**
  * cd daily_expense_tracker
3. **Run the application:**
  * python main.py
  
   
   
  

## Logic Highlights
One of the key parts of this project is the use of list comprehension and built-in functions to handle data efficiently:
``` 
# Calculating average with built-in functions
total = sum(expenses)
average = total / len(expenses)
``` 
---

Developed by Lucia Avilla 🚀
