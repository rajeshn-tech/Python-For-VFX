# Project 01 - Render Report Generator

## Project Introduction

## Topics 

- Project Overview
- Problem Statement
- Project Goal
- Input and output
- Features
- Data Flow
- Real VFX Use Case

---

# Topic 1 - Project Overview

## What is this Project?

The **Render Report Generator** is a Python automation tool that reads a render report from an Excel file, processes the data, and generates a clean summary report.

The Tool automatically calculates:

- Complete Jobs.
- Total Frames.
- Total Render Time.
- Daily Summary.
- Monthly Summary.

---

## Why Do we need this tool?

In a production environment, render frams generate thousands of render jobs every day.

Manually calculating is slow, repetitive, and error-prone.

This tool automates the entire reporting process.

## Project Goal

The goal of this project is to build a production-style Python tool that can:

- Read Excel files
- Process render data
- Generate summary reports
- Save the output as a text report

---

# Topic 2 - Input and Output

## Input

The tool reads data from:

```text
input.xlsx
```

The Excel file contains information such as:

- Job Status
- Finished Date
- Frame Range
- Render Time

---

# Output

The tool generates:

```text
output_report.txt
```

The report includes:

- Daily Summary
- Monthly Summary
- Total Jobs
- Total Frames
- Total Render Time

---

# Topic 3 - Features

## Features of the Tool

- Read Excel File
- Automatically Detect Required Columns
- Filter Completed Jobs
- Calculate Frame Count
- Convert Render Time
- Generate Daily Smmary
- Generate Monthly Summary
- Export Report to Text File

---

# Topic 4 - Data Flow

## Project Workflow

```text
input.xlsx
      │
      ▼
Read Excel File
      │
      ▼
Read Every Row
      │
      ▼
Check Job Status
      │
      ▼
Completed Jobs
      │
      ▼
Calculate Frames
      │
      ▼
Calculate Render Time
      │
      ▼
Store Daily Summary
      │
      ▼
Store Monthly Summary
      │
      ▼
Generate output_report.txt
```

---

# Topic 5 - Real VFX Example

Imagine a VFX studio renders more than **10000 jobs** every day.

a supervisor wants to know:

- How many jobs completed today?
- How many frames were renderd?
- What was the total render time?

Instead of manually calculation everything, this Python tool generates the report automatically.

---

## Production Note

Tool like this are commonly developed by:

- Pipeline TDs
- Pipeline Developers
- Automation Engineers
- Technical Directors

These tool help studios save time and reduce manual work.

---

# Today's Learning

- Introduction to the Project
- Problem Statement
- Project Goal
- Input and Output
- Features
- Data Flow
- Real Production use Case

### Reading Excel using Pandas

## Topics

- What is Pandas?
- Importing Pandas
- Reading an Excel File
- DataFrame
- Viewing Data
- Coloumns
- Row
- Basic DataFrame Fuctions

---

# Topic 1 - What is Pandas?

Pandas is a Python library used for working with structured data.

It provides powerful tools to:

- Read Excel files
- Read CSV files
- Process large datasets
- Filters data
- Sort data
- Analyze data

Panda is one of the most widely used liberaries in Data Analysis and Pipeline Automation.

---

## Why do we use Pandas?

Python cannot read Excel files directly.

Pandas provides built-in fuctions that make reading and processing Excel files simple.

Without Pandas, reading Excel data would be much more difficult.

---

## Production Example

A render farm exports a report containing thousands of render jobs.

Instead of manually opening Excel and calculating totals, a Pipeline TD uses Pandas to process the report automatically.

---

# Topic 2 - Importing Pandas

## Syntax

```python
import pandas as pd
```

---

## Explanation

import

imports a Python liberary.

pandas

Library name.

pd

alias (short name).

Instead of writing

```python
pandas.read_excel()
```

we write

```python
pd.read_excel()
```

This is the standard convention used by Python developers.

---

# Topic 3 - Reading an Excel File

## Syntax

```python
df = pd.read_excel("input.xlsx")
```

---

## Explanation

read_excel()

Reads an Excel file.

input.xlsx

The file to read.

df

Stores the Excel data as a DataFrame.

---

# Topic 4 - What is a DataFrame?

A DataFrame is a table of data.

it contains:

- Row
- Coloumn

Example

|-----------|-----------|-------------|
| Status    | Frames    | Render Time |
|-----------|-----------|-------------|
| Completed | 1001-1050 | 00:00:20    |
| Failed    | 2001-2050 | 00:00:15    |
|-----------|-----------|-------------|


This table becomes a DataFrame after reading it with Pandas.

---

# Topic 5 - Viewing Data

```python
print(df)
```

---

## Display First 5 Rows

```python
print(df.head())
```

---

## Display Last 5 Rows

```python
print(df.tail())
```

---

## Display Column Names

```python
print(df.columns)
```

---

## Display Data Information

```python
print(df.info())
```

This Show:

- Number of rows
- Number of coloumns
- Column names
- Data types
- Missing values

---

## Production Note

Always inspect the data before writing any processing logic.

Never assume that:

- Column names are correct.
- Data types are correct.
- Every row contains valid data.

Checking the DataFrame frist helps avoid bugs.

---

# Python Concepts Used

|---------------|-------------------------|
| Concept       | Purpose                 |
|---------------|-------------------------|
| import        | Import external library |
|---------------|-------------------------|
| Alias (as)    | Short library name      |
|---------------|-------------------------|
| Variable      | Store DataFrame         |
|---------------|-------------------------|
| Fuction       | read_excel()            |
|---------------|-------------------------|
| String        | File name               |
|---------------|-------------------------|
| Object        | DataFrame               |
|---------------|-------------------------|

# Today's Learning

- Pandas
- Importing Libraries
- Reading Excel
- DataFrame
- Viewing Data
- Understanding Rows and Columns
