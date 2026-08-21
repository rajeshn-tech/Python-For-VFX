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

# Topic 3 - Parameters & Arguments

## Definition

Parameters and Arguments allow a Function to receive different values.

This makes a Function reusable with different data.

---

## Why Do We Need It?

Without Parameters and Arguments, a Function usually works with fixed data.

Example:

```python
def show_artist():
    print("Artist: Rajesh")
```

This Function always prints the same Artist.

Using a Parameter:

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
artist    -> Parameter
"Rajesh"  -> Argument
```

---

## Example 1 - String Argument

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

The same Function works with different Arguments.

---

## Example 3 - Number Argument

```python
def show_priority(priority):
    print("Priority:", priority)

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
    print("Processing:", job_name)

print("Render Started")

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
artist    -> Parameter
"Rajesh"  -> Argument
```

```text
Parameter -> Receives the value
Argument  -> Actual value passed to the Function
```

---
# Topic 4 - Multiple Parameters

## Definition

A Function can have more than one Parameter.

Multiple Parameters allow a Function to receive multiple values at the same time.

---

## Why Do We Need Multiple Parameters?

Sometimes a Function needs more than one piece of information.

For example, a render job may contain:

- Job Name
- Artist
- Status
- Priority

Instead of creating separate Functions for every value, we can pass multiple values to one Function.

---

## Syntax

```python
def function_name(parameter1, parameter2):
    code
```

Function Call:

```python
function_name(argument1, argument2)
```

---

## Example 1 - Two Parameters

```python
def show_frame(shot, frame):
    print("Shot:", shot)
    print("Frame:", frame)

show_frame("SH030", 1050)
```

### Output

```text
Shot: SH030
Frame: 1050
```

Here:

```text
Parameters = shot, frame
Arguments  = "SH030", 1050
```

The values are passed according to their positions.

```text
shot  <- "SH030"
frame <- 1050
```

---

## Example 2 - Three Parameters

```python
def show_render_job(job_name, artist, status):
    print("Job:", job_name)
    print("Artist:", artist)
    print("Status:", status)

show_render_job("ABC_SH020", "Amit", "Rendering")
```

### Output

```text
Job: ABC_SH020
Artist: Amit
Status: Rendering
```

Here:

```text
Parameters = job_name, artist, status

Arguments = "ABC_SH020", "Amit", "Rendering"
```

The Arguments are assigned to the Parameters according to their positions.

```text
job_name <- "ABC_SH020"
artist   <- "Amit"
status   <- "Rendering"
```

---

## Argument Order is Important

The order of Arguments matters when calling a Function.

Example:

```python
def show_job(job_name, artist, priority):
    print("Job:", job_name)
    print("Artist:", artist)
    print("Priority:", priority)

show_job("Rajesh", 80, "SH010")
```

### Output

```text
Job: Rajesh
Artist: 80
Priority: SH010
```

Python follows the position of each Argument.

```text
job_name <- "Rajesh"
artist   <- 80
priority <- "SH010"
```

Python does not automatically understand that `"Rajesh"` should be the Artist or `"SH010"` should be the Job Name.

The correct Function call would be:

```python
show_job("SH010", "Rajesh", 80)
```

### Output

```text
Job: SH010
Artist: Rajesh
Priority: 80
```

---

## Missing Arguments

Required Parameters must receive their Arguments.

Example:

```python
def show_job(job_name, artist, status):
    print("Job:", job_name)
    print("Artist:", artist)
    print("Status:", status)

show_job("SH010", "Rajesh")
```

The Function has three Parameters:

```text
job_name
artist
status
```

But only two Arguments are provided:

```text
job_name <- "SH010"
artist   <- "Rajesh"
status   <- Missing
```

Python will raise a `TypeError`.

### Error

```text
TypeError: show_job() missing 1 required positional argument: 'status'
```

The Function does not execute because a required Argument is missing.

---

## Production Example

```python
def show_render_job(job_name, artist, status, priority):
    print("Job Name:", job_name)
    print("Artist:", artist)
    print("Status:", status)
    print("Priority:", priority)

show_render_job(
    "ABC_SH010_Comp_v001",
    "Rajesh",
    "Rendering",
    80
)
```

### Output

```text
Job Name: ABC_SH010_Comp_v001
Artist: Rajesh
Status: Rendering
Priority: 80
```

This allows one Function to receive and process multiple pieces of render job information.

---

## Important Points

- A Function can have multiple Parameters.
- Parameters are separated by commas.
- Arguments are also separated by commas.
- Arguments are assigned to Parameters according to their positions.
- The first Argument goes to the first Parameter.
- The second Argument goes to the second Parameter.
- The order of Arguments is important.
- Wrong Argument order may produce incorrect data without causing an error.
- Missing a required Argument causes a `TypeError`.
- String Arguments use quotes.
- Number Arguments do not require quotes.

---

## Summary

```python
def show_job(job_name, artist, status):
    print(job_name)
    print(artist)
    print(status)

show_job("SH010", "Rajesh", "Rendering")
```

```text
Parameters:
job_name, artist, status

Arguments:
"SH010", "Rajesh", "Rendering"

Mapping:

1st Argument -> 1st Parameter
2nd Argument -> 2nd Parameter
3rd Argument -> 3rd Parameter
```

Multiple Parameters allow one Function to receive multiple values.

---

# Topic 5 - Default Parameters

## Definition

A Default Parameter is a Parameter that already has a default value.

If no Argument is provided for that Parameter, Python uses the default value.

---

## Why Do We Need Default Parameters?

Default Parameters are useful when a Function commonly uses the same value.

For example, a render job may have `"Pending"` as its default status.

Instead of passing `"Pending"` every time, we can set it as a default value.

---

## Syntax

```python
def function_name(parameter="Default Value"):
    code
```

Example:

```python
def show_status(status="Pending"):
    print("Status:", status)
```

Here:

```text
status="Pending" -> Default Parameter
"Pending"        -> Default Value
```

---

## Example 1 - Using the Default Value

```python
def show_status(status="Rendering"):
    print("Status:", status)

show_status()
```

### Output

```text
Status: Rendering
```

No Argument was provided.

Therefore, Python uses the default value `"Rendering"`.

---

## Example 2 - Overriding the Default Value

```python
def show_status(status="Rendering"):
    print("Status:", status)

show_status("Completed")
```

### Output

```text
Status: Completed
```

The Argument `"Completed"` was provided.

Therefore, Python uses `"Completed"` instead of the default value `"Rendering"`.

---

## Default Value vs Argument

```python
def show_department(department="Compositing"):
    print("Department:", department)

show_department()
show_department("Lighting")
```

### Output

```text
Department: Compositing
Department: Lighting
```

First Function Call:

```text
show_department()

No Argument
      ↓
Use Default Value
      ↓
"Compositing"
```

Second Function Call:

```text
show_department("Lighting")

Argument = "Lighting"
      ↓
Use Argument
      ↓
Default Value is not used
```

---

## Required Parameter and Default Parameter

A Function can contain both Required Parameters and Default Parameters.

```python
def show_job(job_name, status="Pending"):
    print("Job:", job_name)
    print("Status:", status)
```

Here:

```text
job_name          -> Required Parameter
status="Pending"  -> Default Parameter
"Pending"         -> Default Value
```

---

## Example - Using Required and Default Parameters

```python
def show_job(job_name, status="Pending"):
    print("Job:", job_name)
    print("Status:", status)

show_job("SH010")
```

### Output

```text
Job: SH010
Status: Pending
```

Mapping:

```text
job_name <- "SH010"
status   <- No Argument
               ↓
           "Pending"
```

`job_name` receives the Argument `"SH010"`.

No Argument is provided for `status`, so Python uses its default value.

---

## Overriding a Default Parameter

```python
def show_job(job_name, status="Pending"):
    print("Job:", job_name)
    print("Status:", status)

show_job("SH010", "Completed")
```

### Output

```text
Job: SH010
Status: Completed
```

Mapping:

```text
job_name <- "SH010"
status   <- "Completed"
```

Because an Argument was provided for `status`, the default value `"Pending"` is not used.

---

## Multiple Default Parameters

A Function can contain multiple Default Parameters.

```python
def show_render_job(job_name, artist, status="Pending", priority=50):
    print("Job:", job_name)
    print("Artist:", artist)
    print("Status:", status)
    print("Priority:", priority)

show_render_job("SH020", "Rajesh")
```

### Output

```text
Job: SH020
Artist: Rajesh
Status: Pending
Priority: 50
```

Here:

```text
Required Parameters:
job_name
artist

Default Parameters:
status="Pending"
priority=50

Arguments:
"SH020"
"Rajesh"

Default Values Used:
"Pending"
50
```

---

## Parameter Order

Required Parameters must come before Default Parameters.

### Correct

```python
def show_job(job_name, status="Pending"):
    print(job_name)
    print(status)
```

```text
Required -> Default
```

### Incorrect

```python
def show_job(status="Pending", job_name):
    print(job_name)
    print(status)
```

This causes a `SyntaxError`.

```text
SyntaxError: non-default argument follows default argument
```

### Rule

```text
Required Parameters -> First
Default Parameters  -> After
```

---

## Production Example

```python
def show_render(job_name, status="Pending"):
    print("Job:", job_name)
    print("Status:", status)

show_render("ABC_SH010")
show_render("XYZ_SH020", "Completed")
```

### Output

```text
Job: ABC_SH010
Status: Pending
Job: XYZ_SH020
Status: Completed
```

First Call:

```text
Argument = "ABC_SH010"
Status   = Default "Pending"
```

Second Call:

```text
Arguments = "XYZ_SH020", "Completed"
Status    = "Completed"
```

---

## Important Points

- A Default Parameter already has a value.
- Default values are defined using `=`.
- If no Argument is provided, the default value is used.
- If an Argument is provided, it overrides the default value.
- A Default Value is not automatically an Argument.
- Arguments are values provided during Function calls.
- Required Parameters must come before Default Parameters.
- A Function can contain multiple Default Parameters.

---

## Summary

```python
def show_job(job_name, status="Pending"):
    print("Job:", job_name)
    print("Status:", status)
```

```text
job_name          -> Required Parameter
status="Pending"  -> Default Parameter
"Pending"         -> Default Value
```

Without a status Argument:

```python
show_job("SH010")
```

```text
Status -> Pending
```

With a status Argument:

```python
show_job("SH010", "Completed")
```

```text
Status -> Completed
```

Simple Rule:

```text
Argument not provided -> Use Default Value
Argument provided     -> Use Argument
```

---


# Topic 6 - return Statement

## Definition

The `return` statement sends a value back from a Function.

The returned value can be stored in a variable and used later in the program.

---

## Why Do We Need return?

Sometimes we do not only want to display a result.

We may want to:

- Store the result
- Use it in another calculation
- Pass it to another part of the program
- Reuse it later

`return` allows a Function to send its result back.

---

## Syntax

```python
def function_name():
    return value
```

Example:

```python
def get_priority():
    return 80
```

---

## Example 1 - Returning a Value

```python
def get_priority():
    return 80

priority = get_priority()

print("Priority:", priority)
```

### Output

```text
Priority: 80
```

### How It Works

```text
get_priority()
      ↓
return 80
      ↓
80 comes out of the Function
      ↓
priority = 80
      ↓
Priority: 80
```

---

## Example 2 - Returning a String

```python
def get_status():
    return "Completed"

status = get_status()

print("Status:", status)
```

### Output

```text
Status: Completed
```

---

## Example 3 - Returning a Calculation

```python
def calculate_frames(start_frame, end_frame):
    total_frames = end_frame - start_frame + 1
    return total_frames

frames = calculate_frames(1001, 1010)

print("Total Frames:", frames)
```

### Output

```text
Total Frames: 10
```

### How It Works

```text
start_frame = 1001
end_frame   = 1010

total_frames = 1010 - 1001 + 1
             = 10

return 10
      ↓
frames = 10
```

---

## Production Example

```python
def calculate_render_time(frames, time_per_frame):
    total_time = frames * time_per_frame
    return total_time

render_time = calculate_render_time(10, 5)

print("Render Time:", render_time)
```

### Output

```text
Render Time: 50
```

The Function calculates the render time and returns the result.

---

## print() vs return

`print()` displays a value on the screen.

```python
def get_frames():
    print(100)

get_frames()
```

### Output

```text
100
```

`return` sends the value back from the Function.

```python
def get_frames():
    return 100

frames = get_frames()

print(frames)
```

### Output

```text
100
```

The main difference is:

```text
print() -> Displays the result

return  -> Sends the result back
           so it can be stored and reused
```

---

## return Stops the Function

When Python reaches `return`, the Function stops immediately.

Example:

```python
def check_render():
    print("Checking Render...")
    return "Completed"
    print("Render Finished")

status = check_render()

print("Status:", status)
```

### Output

```text
Checking Render...
Status: Completed
```

This line does not run:

```python
print("Render Finished")
```

Because the Function stops when Python reaches:

```python
return "Completed"
```

---

## Function Flow with return

```text
Function Starts
      ↓
Code Executes
      ↓
return
      ↓
Value is sent back
      ↓
Function Stops
```

---

## Important Points

- `return` sends a value back from a Function.
- A returned value can be stored in a variable.
- A Function can return Strings, Numbers, Boolean values, and other data types.
- A Function can return the result of a calculation.
- `print()` only displays a value.
- `return` allows the value to be reused later.
- The Function stops immediately when Python reaches `return`.
- Code written after `return` does not execute.

---

## Summary

```python
def get_priority():
    return 80

priority = get_priority()
```

```text
return 80
      ↓
Function sends 80 back
      ↓
priority = 80
```

Simple Rule:

```text
print() -> Show the value
return  -> Send the value back
```

---