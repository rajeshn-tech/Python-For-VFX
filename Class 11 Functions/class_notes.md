# Class 11 - Functions

# Topic 1 - What is a Function?

## Definition

A Function is a reusable block of code that performs a specific task.

A Function is created using the `def` keyword.

---

## Why Do We Need a Function?

Functions help us avoid writing the same code again and again.

For example, a render report may need to display job information multiple times.

Instead of repeating the same `print()` statements, we can create a Function and call it whenever required.

---

## Syntax

```python
def function_name():
    code
```

To run the Function:

```python
function_name()
```

---

## Example 1 - Render Report Header

```python
def show_report_header():
    print("===================================")
    print("VFX RENDER JOB REPORT")
    print("===================================")

show_report_header()
```

### Output

```text
===================================
VFX RENDER JOB REPORT
===================================
```

---

## Example 2 - Display Render Status

```python
def show_render_status():
    print("Shot: SH010")
    print("Status: Rendering")

show_render_status()
```

### Output

```text
Shot: SH010
Status: Rendering
```

---

## Example 3 - Multiple Function Calls

```python
def show_render_status():
    print("Checking Render...")

show_render_status()
show_render_status()
show_render_status()
```

### Output

```text
Checking Render...
Checking Render...
Checking Render...
```

---

## Function Definition vs Function Call

### Function Definition

```python
def show_report():
    print("Render Report")
```

This creates the Function.

It does not run the Function.

### Function Call

```python
show_report()
```

This calls and runs the Function.

### Output

```text
Render Report
```

---

## Production Example

```python
def show_job_info():
    print("Job Name: ABC_SH010_Comp_v001")
    print("Artist: Rajesh")
    print("Status: Rendering")

show_job_info()
```

### Output

```text
Job Name: ABC_SH010_Comp_v001
Artist: Rajesh
Status: Rendering
```

This Function will later become part of the Class 11 mini project.

---

## Important Points

- `def` is used to create a Function.
- A Function has a name.
- Function code must be indented.
- A Function does not run until it is called.
- Use `function_name()` to call a Function.
- A Function can be called multiple times.
- Functions help reduce repeated code.

---

## Summary

```python
def show_report():
    print("Render Report")
```

Creates a Function.

```python
show_report()
```

Calls and runs the Function.

---


# Topic 2 - Creating & Calling Functions

## Definition

A Function must first be created and then called to execute its code.

There are two main steps:

1. Create / Define a Function
2. Call / Run the Function

---

## Step 1 - Creating a Function

A Function is created using the `def` keyword.

### Syntax

```python
def function_name():
    code
```

### Example

```python
def show_job_name():
    print("Job Name: ABC_SH010_Comp_v001")
```

In this example:

```text
def           -> Creates the Function
show_job_name -> Function Name
()            -> Parentheses
:             -> Starts the Function block
```

The indented code belongs to the Function.

Creating a Function does not execute it.

---

## Step 2 - Calling a Function

To execute a Function, write its name followed by parentheses `()`.

### Syntax

```python
function_name()
```

### Example

```python
def show_job_name():
    print("Job Name: ABC_SH010_Comp_v001")

show_job_name()
```

### Output

```text
Job Name: ABC_SH010_Comp_v001
```

`show_job_name()` calls the Function and executes the code inside it.

---

## Function Execution Flow

```python
def show_status():
    print("Status: Rendering")

print("Report Started")

show_status()

print("Report Finished")
```

### Output

```text
Report Started
Status: Rendering
Report Finished
```

### How It Works

```text
def show_status()
        ↓
Function is created
Function does not run yet

print("Report Started")
        ↓
Report Started

show_status()
        ↓
Function is called
Status: Rendering

print("Report Finished")
        ↓
Report Finished
```

---

## Calling a Function Multiple Times

A Function can be called multiple times.

```python
def check_job():
    print("Checking Job...")

check_job()
check_job()
```

### Output

```text
Checking Job...
Checking Job...
```

The Function is created once but called twice.

Therefore, the code inside the Function executes twice.

---

## Production Example

```python
def show_render_status():
    print("Status: Rendering")

print("VFX RENDER JOB REPORT")

show_render_status()

print("Report Complete")
```

### Output

```text
VFX RENDER JOB REPORT
Status: Rendering
Report Complete
```

This type of Function will later be used in the Class 11 mini project.

---

## Important Points

- Use `def` to create a Function.
- Creating a Function does not execute it.
- Use `function_name()` to call a Function.
- A Function runs only when it is called.
- A Function can be called multiple times.
- Function code must be indented.
- Python executes the Function code when it reaches the Function call.

---

## Summary

```python
def show_job():
    print("Render Job")
```

Creates the Function.

```python
show_job()
```

Calls and runs the Function.

```text
Create / Define -> def function_name()
Call / Run      -> function_name()
```

---


# Topic 3 Parameters & Arguments

## Definition

Parameters and Arguments allow a Function to receive different values.

This makes a Function reusable with different data.

---

## Why Do We Need It?

Without Parameters and Arguments, a Function usually works with fixed data.

Example:

```python
def show_artist(artist):
        print("Artist:", artist)
```

Now we can pass different Artist names when calling the Function.

---

## Parameter

A Parameter is the name written inside the Function definition.

It receives the value passed to the Function.

### Example

```python
def show_artist(artist):
        print("Artist:", artist)
```

Here: 

```text
artist -> Parameter
```

---

## Argument

An Argument is the actual value passed when calling the Function.

### Example

```python
show_artist("Rajesh")
```

Here:

```text
"Rajesh" -> Argument
```

---

## Parameter vs Argument

```python
def show_artist(artist):
        print("Artist:", artist)

show_artist("Rajesh")
```

```text
artist   -> Parameter
"Rajesh" -> Argument
```

---

## Example 1 String Argument

```python
def show_status(status):
        print("Status:", status)

show_status("Rendering")
```

### Output

```text
Status: Rendering
```

---

## Example 2 - Multiple Function Calls

```python
def show_status(status):
        print("Status:", status)

show_status("Rendering")
show_status("Completed")
show_status("Pending")
```

### Output

```text
Status: Rendering
Status: Completed
Status: Pending
```

The same function works with different Arguments.

---


## Example 3 - Number Argument

```python
def show_priority(priority):
        print("Priority:", Priority)

show_priority(80)
show_priority(50)
```

### Output

```text
Priority: 80
Priority: 50
```

Arguments can also be Numbers.

---

## Production Example

```python
def show_job(job_name):
        print("Processing", job_name)

print(""Render Started)

show_job("ABC_SH010")
show_job("XYZ_SH020")

print("Render Finished")
```

### Output

```text
Render Started
Processing: ABC_SH010
Processing: XYZ_SH020
Render Finished
```

This type of Function can be used to process different VFX jobs using the same code.

---

## Important Points

- A Parameter is written inside the Function definition.
- An Argument is passed during the Function call.
- Parameters receive Arguments.
- Arguments can be Strings, Numbers, Boolean values, and other data types.
- The same Function can be called with different Arguments.
- Different Arguments can produce different outputs.

---

## Summary

```python
def show_artist(artist):
        print("Artist:", artist)

show_artist("Rajesh")
```

```text
artist   -> Parameter
"Rajesh" -> Argument
```

```text
Parameter -> Receives the value
Argument  -> Actual value passed to the Function
```

---

