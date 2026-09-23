# Student Marks Pandas

## 📌 Project Overview

This project demonstrates basic data manipulation and preprocessing using **Python Pandas**.

A student dataset is created containing student names, ages, gender, and marks. The data is then processed using Pandas to calculate the average marks, handle missing values, convert gender values into numerical values, filter students based on marks, and remove an unnecessary column.

## 🎯 Objectives

* Create a DataFrame using Pandas
* Display student data
* Calculate the average marks
* Replace missing marks with the average
* Convert gender values into numerical values
* Filter students who scored 75 or above
* Remove the Age column

## 🛠️ Technologies Used

* Python
* Pandas

## 📊 Dataset

The dataset contains the following columns:

* **Name** – Student name
* **Age** – Student age
* **Gender** – M or F
* **Marks** – Student marks

## 🔄 Data Processing

The program performs the following steps:

1. Creates student data using a Python dictionary.
2. Converts the data into a Pandas DataFrame.
3. Calculates the average of the available marks.
4. Replaces missing `"NaN"` marks with the average mark.
5. Converts Gender:

   * M → 2
   * F → 1
6. Filters students with marks greater than or equal to 75.
7. Removes the Age column.
8. Displays the final processed DataFrame.

## 📈 Final Result

After processing the data, the students with marks of **75 or above** are displayed.

The missing marks are replaced with the calculated average of **75.2**.

## ▶️ How to Run

Make sure Python and Pandas are installed.

Open the terminal in the project folder and run:

```bash
python student_marks.py
```

## 📁 Project Structure

```text
Student-Marks-Pandas/
│
├── student_marks.py
└── README.md
```

## 👩‍💻 Author

**DudekulaRizwana**

## ⭐ Conclusion

This project demonstrates basic Pandas operations such as DataFrame creation, data cleaning, value replacement, data transformation, filtering, and column removal.

## 🙏 Thank You

Thank you for visiting this project!
