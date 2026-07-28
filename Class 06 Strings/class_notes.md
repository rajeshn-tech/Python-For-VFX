# Class 06 - Strings

## Topic 1 - What is String?

### Definition

A String is a sequence of characters.

A character means a single letter, number, space, or symbol.

A String is a collection (sequence) of one or more characters.

A character can be:

- Alphabet
- Number
- Space
- Symbol
- Special Character

## Examples

```python
"Hello"
"Rajesh"
"Shot010"
"1920x1080"
"ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"
```

Strings are written inside quotes.

Python treats everything inside the quotes as text.

> **Note**
>
> Everything inside quotes is treated as text by Python, even if it contains only numbers.

Example:

```python
"500"    # String
500      # Integer
```

---

## Python Execution Flow

Example:

```python
project = "ABC"
```

### Step 1

Python reads the variable name.

```text
project
```

↓

### Step 2

Python sees the assignment operator.

```text
=
```

↓

### Step 3

Python reads the value.

```text
"ABC"
```

↓

### Step 4

Python detects the quotes.

↓

Python understands that the value is a **String**.

↓

Python creates a **String Object** in memory.

↓

The variable **project** stores a reference to that String Object.

---

## Visual Flow

```text
        "ABC"
          │
          ▼
   String Object
          │
          ▼
 Variable: project
```

---

## Summary

- A String is a sequence of characters.
- A character can be a letter, number, space, or symbol.
- Strings are always written inside quotes.
- Everything inside quotes is treated as text.
- Python creates a String Object in memory and the variable refers to that object.


# Topic 2 - Creating Strings

## What does "Creating a String" mean?

Creating a String means storing text inside a variable.

General Syntax:

```python
variable_name = "text"
```

Python stores the text as a String Object in memory and the variable refers to that object.

---

## Examples

```python
project = "ABC"
artist  = "Rajesh"
software = "Nuke"
version = "v001"
extension = ".nk"
```

All of the above values are Strings because they are written inside quotes.

---

## Production Example

```python
file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"
```

Here,

- `file_name` -> Variable Name
- `=` -> Assignment Operator
- `"ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"`

---

## Pyhton Execution Flow

Example:

```python
artist = "Rajesh"
```

Step 1

Python reads the variable name.

↓

Step 2

Python sees the assignment operator (`=`).

↓

Step 3

Python reads the value.

↓

Step 4

Quotes are detected.

↓

Python creates a String Object in memory.

↓

The variable `artist` refers to that String Object.

---

## Summary

- Creating a String means storing text inside a variable.
- Strings are enclosed inside quotes.
- Python stores the String in memory.
- The variable refers to the String Object.


# Topic 3 - Single Quotes

## What are Single Quotes?

Single quotes (`' '`) are one of the ways to create a String in Python.

General Syntax:

```python
variable_name = 'text'
```

Python treats everything inside the single quotes as a String.

---

## Examples

```python
project = 'ABC'
artist = 'Rajesh'
software = 'Nuke'
department = 'COMP'
```

All of the above values are Strings because they are enclosed inside single quotes.

---


## Production Example

```python
file_name = 'ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk'
```

Even though the file name contains letters, numbers, underscore, and dot, Python treats it as a single String.

---

## Python Execution Flow

Example:

```python
artist = 'Rajesh'
```

Step 1
Python reads the variable name.
↓

Step 2

Python reads the assignment operator (`=`).

↓

Step 3

Python reads the value.

↓

Step 4

Python detects the single quotes.

↓

Python creates a String Object.

↓

The variable refers to that String Object.

---

## Important Note

Single quotes and double quotes create the same String.

```python
'Rajesh'

"Rajesh"
```

Both are Strings.

There is no difference in the data type.

---

## Summary

- Single quotes are used to create Strings.
- Everything inside single quotes is treated as text.
- Python creates a String Object in memory.
- Single quptes and double quotes both create Strings.


# Topic 4 -  Double Quotes

## What are Double Quotes?

Double quotes(`" "`) are one of the ways to create a String in Python.

General Syntax:

```python
variable_name = "text"
```

Python treats everythinginside the double quotes as a String.

---

## Examples

```python
project = "ABC"

artist = "Rajesh"

software = "Nuke"

department = "COMP"
```

Al of the above values are Strings because they are enclosed inside double quotes.

---

## Production Example

```python
file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"
```

Even though the file name contains letters, numbers, underscores, and a dot, Python treats it as a single String.

---

## Python Execution Flow

Example:

```python
artist = "Rajesh"
```

Step 1

Python reads the variable name.

↓

Step 2

Python reads the assignment operator (`=`).

↓

Step 3

Python reads the value.

↓

Step 4

Python detects the double quotes.

↓

Python creates a String Object.

↓

The variable refers to that String Object.

---

## Important Note

Singele quotes and double quotes create the same String.

```python
'Rajesh'

"Rajesh"
```
Both are Strings.

There is no difference in the data type.

---

## Summary

- Double quotes are used to create Strings.
- Everything inside double quotes is treated as text.
- Python creates a String Object in memory.
- Single quotes and double quotes both create Strings.


# Topic 5 - Triple Quotes

## What are Triple Quotes?

Triple quotes (`''' '''` or `''' '''`) are used to create multi-line Strings.

Pyhton treats everythings written between the opening and closing triple quotes as a single String.

---

Using Triple Double Qoutes

```python
text = """
This is line 1.
This is line 2.
This is line 3.
"""
```

Using Triple Single Quotes

```python
text = '''
This is line 1.
This is line 2.
This is line 3.
'''
```

Both create a String.

---

## Example 

```python
message = """
Welcome to Python
For VFX
Pipeline Development
"""
```

---

## Production Example 

```python
render_log = """
Project : ABC
Sequence : XYZ5120
Shot : SH010
Artist : Rajesh
Status : Complete
"""
```

The Complete block is stored as a single String.

---

## Python Execution Flow

Example:

``` Python
message = """
Hello
World
"""
```

Step 1

Python reads the variable name.

↓

Step 2

Python sees the assignment operator (`=`).

↓

Step 3

Python detects the opening triple quotes.

↓

Step 4

Python keeps reading every line until it finds the closing triple quotes.

↓

Step 5

Python creates one multi-line String Object.

↓

Step 6

The variable refers to that String Object.

---


## Summary

- Triple quotes create multi-line Strings.
- Triple single quotes and triple double quotes both same work.
- Everything between the opening and closing triple quotes becomes one String.

# Flow Diagram

Opening Triple Quotes
        │
        ▼
Read Line 1
        │
        ▼
Read Line 2
        │
        ▼
Read Line 3
        │
        ▼
Closing Triple Quotes
        │
        ▼
Create One String Object


# Topic 6 -  String Indexing

## What is String Indexing?

String Indexing means accessing a single character from a String using its position.

Python starts counting from **0**, not 1.

General Syntax:

```python
string_name[index]
```

---

## Example 

```python
artist = "Rajesh"
print(artist[0])
```

Output:

```text
R
```

---

## Character Positions

```text
String : R a j e s h
Index  : 0 1 2 3 4 5
```

---

## Production Example 

```python
file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

print(file_name[0])
```

Output

```text
A
```

---


## Summary

- Index means position.
- Python starts indexing from 0.
- Indexing returns one character.
- Strings are ordered collection of characters.


# Topic 7 - Negative Indexing

## What is Negative Indexing?

Negative Indexing means accessing characters from the **end of a String**.

Python starts negative indexing from **-1**.

General Syntax:

```python
string_name[-index]
```

---

## Example

```python
artist = "Rajesh"

print(artist[-1])
```

Output:

```text
h
```

---

## Character Positions

```text
character :  R  a  j  e  s  h
Positive  :  0  1  2  3  4  5
Negative  : -6 -5 -4 -3 -2 -1
```

---

## Production Example

```python
file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

print(file_name[-1])
```

Output

```text
k
```

---

## Summary

- Positive indexing starts from the beginning.
- Negative indexing starts from the end.
- `-1` always means the last character.


# Topic 8 - String Slicing

## What is string Slicing?

String Slicing is used to extract multiple characters from a String.

Indexing returns one character.

Slicing returns a part of the String.

---

## General Syntax

```python
string_name[start : stop]
```

- start -> Starting Index
- stop  -> Ending Index (Not Included) 

Python returns characters from `start` up to **but not including** `stop`.

---

## Example

```python
artist = "Rajesh"

print(artist[0:3])
```

Output

```test
Raj
```

---

## Character Positions

```text
character : R a j e s h
Index     : 0 1 2 3 4 5 
```

`artist[0:3]`

- Start = 0 Include
- Stop  = 3 Not Include

Result

```text
Raj
```

---

## Summary

- Indexing returns one character.
- Slicing returns multiple characters.
- Stop index is never included.


# Topic 8 - String Slicing (Part-2)

## Different Forms of Slicing

### 1. string[:stop]

Start from index 0.

Stops before the given index.

Example

```python
project = "ABCDEFG"

print(project[:3])
```

Output

```text
ABC
```

---

### 2. string[start:]

Starts from the given index.

Goes till the end of the String.

Example

```python
project = "ABCDEFG"

print(project[3:])
```

Output

```text
DEFG
```

---

### 3. string[:]

Returns the complete String.

Example

```python
project = "ABCDEFG"

print(project[:])
```

Output

```text
ABCDEFG
```

---

### 4. string(start:stop:step)
Returns character using a step value.

Examle

```python
project = "ABCDEFG"

print(project[0:7:2])
```

Output

```text
ACEG
```

---

## Summary

- `[:stop]`           -> Beginning to stop
- `[start:]`          -> Start to end
- `[:]`               -> Complete String
- `[start:stop:step]` -> Skip character using step


# Topic 9 - String Methods

## What are String Methods?

String Methods are built-in functions used to perform different operations on a String.

String Methods help us:

- Convert text to uppercase or lowercase
- Capitalize words
- Replace text
- Split text into multiple parts
- Remove spaces unwanted spaces
- Find the position of text
- Count characters or words

String Methods are widely used in:

- File naming
- Path handling
- Excel file processing
- Render log processing
- Nuke scripting
- VFX pipeline automation

---

## General Syntax

```python
string_name.method_name()
```

Example

```python
artist = "Rajesh"
print(artist.upper())
```

Output

```text
RAJESH
```

# Important Concept

Strings are immutable.

This means a String Methods return a new String instead of modifying the orginal String.

Example:

```python
artist = "Rajesh"
new_artist = artist.upper()

print(artist)
print(new_artist)
```

Output

```text
Rajesh
RAJESH
```

The original value remains unchanged.

---

## Common String Methods

|-----------|------------------------|
| Method    | Purpose                |
|-----------|------------------------|
| upper()   | Convert to Uppercase   |
|-----------|------------------------|
| lower()   | Convert to Lowercase   |
|-----------|------------------------|
| title()   | Frist Latter Capitaliez|
|-----------|------------------------|
| replace() | Replace Text           |
|-----------|------------------------|
| split()   | Split String           |
|-----------|------------------------|
| strip()   | Remove Extra Spaces    |
|-----------|------------------------|
| find()    | Find Position          |
|-----------|------------------------|
| count()   | Count characters       |
|-----------|------------------------|

---

## Upper()
# Purpose

The `upper()` method converts all lowercase characters in a String to uppercase.

It returns a new String.

# Syntax

```python
string.upper()
```

## Example

```python
artist = "Rajesh"
uppercase_artist = artist.upper()
print(uppercase_artist)
```

Output:

```text
RAJESH
```

## Production Example

```python
department = "Comp"

Clean_department = department.upper()

print(clean_department)
```

Output:

```text
COMP
```
This can be useful when production data contains inconsistent letter cases.

# Example:

comp
Comp
COMP

After using `upper()`:

COMP
COMP
COMP

## Important

`upper()` does not modify the original String.

```python
department = "comp"

department.upper()

print(department)
```

Output:

```text
comp
```

---

To store the converted value:

```python
department = department.upper()
```

## Summary

- Converts text to uppercase
- Returns a new String
- Does not modify the orginal String
- Useful for standardizing production data


## lower()

## Purpose

The `lower()` method converts all uppercase characters in a String to lowercase.

It returns a new String.

## Syntax

```python
string.lower()
```

# Example

```python
artist = "RAJESH"
lowercase_artist = artist.lower()

print(lowercase_artist)
```

Output:

```text
rajesh
```

## Production Example

```python
file_extension = ".EXR"

clean_extension = file_extension.lower()

print(clean_extension)
```

Output

```text
.exr
```

This is useful when checking file extensions.

# Example:

```python
file_name = "render_output.EXR"

if file_name.lower().endswith(".exr"):
        print("EXR File Found")
```

## Important

`lower()` is commonly used before comparisons.

```python
status = "COMPLETED"

if status.lower() == "completed":
        print("Job Finished")
```

Output:

```text
Job Finished
```

## Summary

- Converts text to lowercase
- Returns a new String
- Useful for case-insensitive comparisons
- Commonly used while validating filenames and extension

## title()

## Purpose

The `title` method converts the first character of every word to uppercase.

The remaining characters are converted to lowercase.

# Syntax

```python
string.title()
```

---

## Example

```python
artist = "rajesh navsagar"
formatted_artist = artist.title()

print(formatted_artist)
```

Output:

```text
Rajesh Navsagar
```

---

## Another Example

```pyhon
department = "compositing department" 
print(department.title())
```

---

Output:

```text
Compositing Department
```

---

## Production Example

```python
artist_name  = "RAJESH NAVSAGAR"
display_name = artist_name.title()

print(display_name)
```

Output:

```text
Rajesh navsagar
```

---

This method is useful when displaying names, departments, titles, and report headings. 

## Important

`title()` may not always be suitable for technical filenames.

## Example

```python
file_name = "abc_xyz_v001,nk"

print(file_name.title())
```

Output:

```text
Abc_Xyz_V001.Nk
```

---

This can change technical naming unexpectedly.

Therefore, use `title()` mainly for display text, not for production filenames.

---

## Summary

- Capitalizes the first letter of every word
- Returns a new String
- Useful for names, titles, and reports
- Should be used carefully with technical filenames

---

## replace()

The `replace()` method replaces one part of a String with another.

It returns a new String.

## Syntax

```python
string.replace(old_value, new_value)
```

## Example

```python
text = "Python is difficult"

new_text = text.replace("difficult", "easy")

print(new_text)
```

Output:

```text
Python is easy
```

---

# Production Example

```python
file_name = "ABC_XYZ5120_DPT_Depth_v001.nk"

new_file_name = file_name.replace("v001", "v002")

print(new_file_name)
```

Output:

```text
ABC_XYZ5120_DPT_Depth_v002.nk
```

## Replace Department Name

```python
file_name = "ABC_XYZ5120_DPT_Depth_v001.nk" 
new_file_name = file_name.replace("Depth", "Comp") 

print(new_file_name)
```


Output

```text
ABC_XYZ5120_DPT_Comp_v001.nk
```

# Replace Path Separator

```python
file_path = "C:/Project/Shot/Render" 
windows_path = file_path.replace("/", "\\") 

print(windows_path)
```
Output

```text
C:\Project\Shot\Render
```

---

## Important

The search is case-sensitive.

```python
artist = "Rajesh" 

print(artist.replace("rajesh", "Rahul"))
```

Output:

```text
Rajesh
```

No replacement happens because:

Rajesh

and:

rajesh

are different.

---

# Replace Limited Occurrences

The optional third argument controls how many replacements should happen.

# Syntax:

```python
string.replace(old_value, new_value, count)
```


Example:

```python
text = "Comp Comp Comp" 
print(text.replace("Comp", "Paint", 1))
```

Output:

```text
Paint Comp Comp
```

Only the first occurrence is replaced.

---

## Summary

- Replaces text inside a String
- Returns a new String
- Search is case-sensitive
- Commonly used in versioning, and path conversion

---


## split()

### Purpose

The `split()` method is used to devide a String into multiple parts.

Instead of returning a string, it returns a list.

---

## Why do we need split()?

In production, a single filename often contains multiple pieces of information.

Example

```test
ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk
```

This filename contains:

- Project
- Sequence
- Department
- Element
- Shot Number
- Artist
- Version

Using `split()`, we can separate all these values.

---

## Syntax

```python
string.split(separator)
```

The separator tells Python where to cut the String.

---

## Example 1

```python
text = "Apple, Banana, Mango"
print(text.split(","))
```

Output

```text
['Apple', 'Banana', 'Mango']
```

---

## Example 2

```python
name = "Rajesh Navsagar"
print(name.split(" "))
```

Output
```text
['Rajesh', 'Navsagar']
```

## Default Separator

If no separator is provided, Python split the String using spaces.

```python
name = "Rajesh Navsagar"

print(name.split())
```

Output:


```text
['Rajesh', 'Navsagar']
```

Using:

```python
name.split()
```

is usually better than:

```python
name.split(" ")
```

because it handles multiple spaces more safely.

---


## Production Example

```python
file_name  = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"
parts = file_name.split("_")
print(parts)
```

Output

```text
['ABC',
'XYZ5120',
'DPT',
'Depth',
'element',
'01',
'Rajesh',
'v002.nk']
```

---

## Access Individual Part

```python
parts = file_name.split("_")
print(parts[0])
print(parts[1])
print(parts[2])
```

Output

```text
ABC
XYZ5120
DPT
```

---
## Store Individual Values

```python
project = parts[0]
sequence = parts[1]
department = parts[2]
element = parts[3]
artist = parts[6]
version_and_extension = parts[7]
```

### Memory

```
Orginal String

ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk

               │
            split("_")

               ▼

[
 'ABC',
 'XYZ5120',
 'DPT',
 'Depth',
 'element',
 '01',
 'Rajesh',
 'v002.nk'
]
```

---

## Split with Maximum Number

The optional second argument controls the maximum number of splits.

# Syntax:

```python
string.split(separator, maxsplit)
```

Example:

```python
text = "ABC_XYZ_DPT_Comp"

print(text.split("_", 2))
```

Output

```text
['ABC', 'XYZ', 'DPT_Comp']
```

Python performs only two slits.

---

## Important

split() does not modify the orginal String.

It returns a new List.

The separator itself is not included in the result.

# Example:

```python
text = "ABC_XYZ"

print(text.split("_"))
```

Output

```text
['ABC', 'XYZ']
```

The underscore is removed during splitting.


---

## Summary

- Splits a String into multiple parts.
- Returns a List.
- Uses a separator to divide the String.
- One of the most important methods in Python automations and VFX pipelines.


## strip()

## Purpose

The `strip()` method is used to remove extra spaces or specified characters from the beginning and the end of a String.

It does not remove characters from the middle of the String.

---

## Why do we need strip()?

Data coming from the following sources may contain unwanted spaces:

- Excel files 
- CSV files
- Text files
- User input
- Render logs
- Copied production reports


Using `strip()`, we can clean the data before processing it.

---

## Syntax

```python
string.strip()
```

---

## Example 1

```python
artist = "  Rajesh  "

print(artist.strip())
```

Output

```text
Rajesh
```

---

## Example 2

```python
text = "---Python---"
print(text.strip("-"))
```

Output

```text
Python
```

## Important

`strip()` removes characters only from the beginning and the end.

It does not remove characters from the middle.

Example

```python
text = "Py thon"
print(text.strip())
```

Output

```text
Py thon
```

The spaces in the middle remains unchanged.


---

##  Production Example

```python
status = "   Completed  "
clean_status = status.strip()
print(clean_status)
```

Output

```text
Completed
```
---

## Comparison Problem

```python
status = " Completed " 

print(status == "Completed")
```

Output

```text
False
```


The comparison fails because the original value contains spaces.

correct approach:

```python
status = " Completed " 

clean_status = status.strip() 

print(clean_status == "Completed")
```

Output

```text
True
```

---

## lstrip()

The `lstrip()` method removes unwanted spaces or characters only from the left side.

```python
text = " Python " 

print(text.lstrip())
```

Output:

```text
Python
```

The right-side spaces remain.

---

## rstrip()

The `rstrip()` method removes unwanted spaces or characters only from the right side.

```python
text = " Python "

print(text.rstrip())
```

Output


```text
Python
```

The left-side spaces remain.

---


### Summary

- Removes unwanted spaces. 
- strip() cleans both sides
- lstrip() cleans the left side
- rstrip() cleans the right side
- Returns a new String.
- Frequently used while cleaning Excel, CSV, log, and user-input data.


## find()

### Purpose

The `find()` method searches for a character or substring inside a String.

It returns the index of first match.

If the value is not fount, it returns `-1`.

---

## Syntax

```python
string.find(value)
```

---

## Example 1 

```python
artist = "Rajesh"

print(artist.find("j"))
```

Output

```text
2
```

---

## Example 2

```python
artist = "Rajesh"

print(artist.find("z"))
```

Output

```text
-1
```

## Production Example

```python
file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

print(file_name.find("Depth"))
```

Output

```text
16
```

---


## Important

- Returns the index of the first matching value.
- Returns `-1` if the value is not fount.
- Search in case-sensitive.

Example


```python
text = "Python"

print(text.find("python"))
```

Output

```text
-1
```

---

### Summary

- Searches for text inside a String.
- Returns the first matching index.
- Returns `-1` if the value is not found.
- Commonly used while searching filenames, paths, and log files.

---

## Count()

### Purpose

The `count()` method counts how many times a character or substring appears inside a String. 

It returns an integer.

---

## Syntax

```python
string.count(value)
```

## Example 1

```python
text = "banana"

print(text.count("a"))
```

Output

```text
3
```

---

## Example 2

```python
artist = "Rajesh Navsagar"

print(artist.count("a"))
```

Output

```text
4
```

---

## Production Example

```python
file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

print(file_name.count("_"))
```

Output

```text
7
```

---

## Important

The search is case-sensitive.

Example

```python
text = "Comp comp COMP"

print(text.count("Comp"))
```

Output

```text
1
```

---

### Summary

- Count characters or substrings.
- Returns an integer.
- Search is case-sensitive.
- Frequently used for filename validation and text analysis.

---

## Topic Summary

- `upper()` converts text to uppercase.
- `lower()` converts text to lowercase.
- `title()` capitalizes the first letter of each word.
- `replace()` replaces one value with another.
- `split()` divides a String into multiple parts.
- `strip()` removes unwanted spaces or characters.
- `find()` returns the position of a value.
- `count()` counts how many times a value appears.
- String Methods are widely used in file handling, report generation, text processing, and VFX pipeline automation.


# Topic 10 - String Operators

## What are String Operators?

String Operators are special operattors used to perform operationas on Strings.

Python provides two main String operators.

- `+` (Concatenation)
- `*` (Repetition)

These operators are widely used in:

- File Naming
- Folder paths
- Report Generation
- Log Messages
- Nuke Scripts
- VFX Pipeline Automation

---

# Concatenation Operator (+)

## Purpose

The `+` operator joins two or more Strings together.

This process is called **Concatenation**

---

## Syntax

```python
string1 + string2
```

---

## Example 1

```python
first_name = "Rajesh"

last_name = "Navsagar"

full_name = first_name + last_name

print(full_name)
```

Output

```text
RajeshNavsagar
```

---

## Example 2

```python
first_name = "Rajesh"
last_name  = "Navsagar"

full_name = first_name + " " + last_name

print(full_name)
```

---

## Production Example

```python
show = "ABC"

shot = "XYZ5120"

file_name = show + "_" + shot + ".nk"
print(file_name)
```

Output

```text
ABC_XYZ5120.nk
```

---

## Important

The `+` operator works only with Strings.

Incorrect

```python
age = 25

print("Age : " + age)
```

This produces a TypeError.

Correct

```python
age = 25
print("Age : " + str(age))
```

Output

```text
Age : 25
```

---

### Summary

- Joins multiple Strings.
- Creates a new String.
- Commonly used for filenames, path, report, and log messages.

---

## Repetition Operator (*)

## Purpose

The `*` operator repeats a String multiple times.

---

## Syntax

```python
string * number
```
---


## Example 1

```python
print("Python " * 3)
```
Output

```text
Python Python Python
```

---

## Example 2

```python
print("=" * 40)
```

Output

```text
========================================
```

---

## Production Example

```python
print("=" * 60)
print("Render Report")

print("=" * 60)
```

Output

```text
============================================================
Render Report
============================================================
```
This technique is commonly used while formatting console reports.

---

## Important

The second value must be an integer.

Correct

```python
print("A" * 5)
```

Output

```text
AAAAA
```

Incorrect

```python
print("A" * 2.5)
```

This produces a TypeError.

---


## Summary

Python provides two String Operators.

| Operator |     Purpose    |
|----------|----------------|
|    `+`   | Join Strings   |
|    `*`   | Repeat Strings |
|----------|----------------|

Both operators are widely used in VFX production for:

- File Naming
- Folder Paths
- Render Reports
- Log Messages
- Console Formatting


# Topic 11 - Membership Operators

## What are Membership Operators?

Membership Operators are used to check whether a value exists inside another object.

Python provides two Membership Operators.

- `in`
- `not in`

These operators return:

- True 
- False

---

# in operators

## Purpose

The `in` operators check whether a value exists inside a String.

---

## Syntax

```python
value in string
```

## Example 1

```python
file_name = "ABC_XYZ5120_Depth_v001.exr"

print("Depth" in file_name)
```

Output

```text
True
```

---

## Example 2

```python
file_name = "ABC_XYZ5120_Depth_v001.exr"

print("Comp" file_name)
```

Output

```text
False
```

---

## Production Example

```python
file_name = "ABC_XYZ5120_Depth_v001.exr"

if "Depth" in file_name:
        print("Depth Pass Found")
```

Output

```text
Depth Pass Found
```

---

### Summary

- Check if a value exists.
- Returns True or False.

---

# not in Operator

## Purpose

The `not in` operator check whether a value does NOT exit.

---

## Syntax

```python
value not in strinf
```

---

## Example 

```python
file_name = "ABC_XYZ5120_Depth_v001.exr"
print("Beauty" not in file_name)
```

Output

```text
True
```

---

## Production Example

```python
status = "Completed"

if "Failed" not in status:
        print("Job Successful")
```

---

### Summary

- Check if a value is absent.
- Returns True or False.

---

# Topic Summary

|-----------|------------------------------|
| Operator  |  Purpose                     |
|-----------|------------------------------|
| in        | Check if value exists        |
|-----------|------------------------------|
| not in    | Check if value does not exit |
|-----------|------------------------------|


# Topic 12 - Escape Characters

## What are Escape Characters?

Escape Characters are special characters that start with a backslash (`\`).

They are used to represent special characters inside a String.

Some common Escape Characters are:

- `\n` -> New Line
- `\t` -> Tab Space
- `\"` -> Double Quote
- `\'` -> Single Quote
- `\\` -> Backslash

---

# New Line (\n)

## Purpose

The `\n` escape character moves the cursor to the next line.

---

## Example

```python
print("Render Started\nRender Finished")
```

Output

```text
Render Started
Render Finished
```

---

# Tab Space (\t)

## Purpose

The `\t` escape character inserts a tab space.

---

## Example

```python
print("Shot\tStatus")
```

Output

```text
Shot    Status
```

---

# Double Quote(\\")

## Purpose

Used to print double quotes inside a String.

---

## Example

```python
print("Artist said\"Render Completed\"")
```

Output

```text
Artist said "Render Completed"
```

---

# Single Quote (\\')

## Purpose

Used to print a single quote inside a String.

---

## Example

```python
print('Artist\'s Render')
```

Output

```text
Artist's Render
```

---

# Backslash (\\\\)

## Purpose

Used to print a backslash.

---

## Example

```python
print("D:\\Projects\\ABC")
```

Output

```text
D:\Projects\ABC
```

---

## Production Example

```python
print("Render Report\n")
print("Shot\tStatus")
print("Shot001\tCompleted")
print("Shot002\tRendering")
```

Output

```text
Render Report

Shot    Status
Shot001 Completed
Shot002 Rendering
```

---

## Summary

Common Escape Characters

|---------|--------------|
| Escape  | Purpose      |
|---------|--------------|
| `\n`    | New Line     |
|---------|--------------|
| `\t`    | Tab Space    |
|---------|--------------|
| `\"`    | Double Quote |
|---------|--------------|
| `\'`    | Single Quote |
|---------|--------------|
| `\\`    | Backslash    |
|---------|--------------|


# Topic 13 - Useful String Methods

## Introduction

Python provides many useful String Methods for checking and validating text.

In this topic, we will learn:

- `startwith()`
- `endswith()`
- `isdigit()`
- `isalpha()`
- `isalnum()`
- `isspace()`

These method return:

- `True`
- `False`

They are commonly used in:

- File Validation
- Version Checking
- Extension Checking
- User Input Validation
- Shot Name Validation
- Pipeline Automation

---

# startswith()

## Purpose

The `startswith()` method check whether a String starts with a specific value.

---

## Syntax

```python
string.startswith(value)
```

---

## Example 1

```python
file_name = "ABC_XYZ5120_v001.nk" 

print(file_name.startswith("ABC"))
```

Output

```text
True
```

---

## Example 2

```pyhton
file_name = "ABC_XYZ5120_v001.nk"

print(file_name.startswith("XYZ"))
```

Output

```text
False
```

---

## Production Example

```python
file_name = "TBO_SFE5120_v002.nk"

if file_name.startswith("TBO"):
        print("TBO Show File")
```

Output

```text
TBO Show File
```

---

### Summary

- Checks the beginning of a String.
- Returns `True` or `False`.
- Useful for validating show names and prefixes.

---

# endswith()

## Purpose

The `endswith()` method checks whether a String ends with a specific value.

---


## Syntax

```python
string.endswith(value)
```

---

## Example 1

```python
file_name = "ABC_XYZ5120_v001.nk"

print(file_name.endswith(".nk"))
```

Output

```text
True
```

---

## Example 2

```python
file_name = "ABC_XYZ5120_v001.nk"

print(file_name.endswith(".exr"))
```

Output

```text
False
```

---

## Production Example

```python
file_name = "ABC_XYZ5120_Depth_v001.exr"

if file_name.endswith(".exr"):
        print("EXR File Found")
```

Output

```text
EXR File Found
```

---

### Summary

- Checks the end of a String.
- Returns `True` or `False`.
- Useful for checking file extensions.

---

# isdigit()

## Purpose

The `isdigit()` method check whether all characters in a String are digit.

---

## Syntax

```python
string.isdigit()
```

## Example 1

```python
frame = "1001"

print(frame.isdigit())
```

Output

```text
True
```

---

## Example 2

```python
frame = "Frame1001"

print(frame.isdigit())
```

Output

```text
False
```

---

## Production Example

```python
frame_input = "1050"

if frame_input.isdigit():
        print("Valid Frame Number")
```

Output

```text
Valid Frame Number
```

---

## Important

A negative number contains '-', so it returns `False`.

```python
number = "-25"

print(number.isdigit())
```

Output
```text
False
```
---

### Summary

- Checks whether all character are number.
- Useful for frame numbers, version number, and numric input.

---

# isalpha()

## Purpose

The `isalpha()` method checks whether all characters in a String are alphabet letters.

---

## Syntax

```python
string.isalpha()
```

---

## Example 1

```python
artist = "Rajesh"

print(artist.isalpha())
```

Output

```text
True
```

---

## Example 2

```python
artist = "Rajesh123"

print(artist.isalpha())
```

Output

```text
False
```

---

## Important

Spaces are not alphabet characters.

```python
artist = "Rajesh Navsagar"

print(artist.isalpha())
```

Output

```text
False
```

---

## Production Example

```python
department = "Compositing"

if department.isalpha():
        print("Valid Department Name")
```

---

### Summary

- Check whether all characters are letters.
- Numbers, spaces, and symbols return `False`.

---

# isalnum()

## Purpose

The `isalnum()` method checks whether all characters are letters or numbers.

Alphanumric means:

- Alphabet
- Number

---

## Syntax

```python
string.isalnum()
```

---

## Example 1

```python
shot_name = "Shot001"

print(shot_name.isalnum())
```

Output

```text
True
```

---

## Example 2

```python
shot_name = "shot_001"
print(shot_name.isalnum())
```

Output

```text
False
```

The underscore `_` is a special character.

---

## Oroduction Example

```python
asset_name = "CarModel101"

if asset_name.isalnum():
        print("Valid Asset Name")
```

Output

```text
Valid Asset Name
```

---

### Summary

- Accepts letters and numbers.
- Space and special characters return `False`.

---

# isspace()

## Purpose

The `isspace()` method checks whether all characters in a String are spaces.

---

## Syntax

```python
string.isspace()
```

---

## Example 1

```python
text = " "

print(text.isspace())
```

Output

```text
True
```

---

## Example 2

```python
text =" ABC "

print(text.isspace())
```

Output

```text
False
```

---

## Production Example

```python
artist_input = " "

if artist_input.isspace():
        print("Artist Name Cannot Be Empty")
```

Output

```text
Artist Name Cannot Be Empty
```

---

### Summary

- Check Whether the String contains only whitespace.
- Useful for validating empty-looking user input.

---

# Combined Production Example

```python
file_name = "TBO_SFE5120_v002.exr"

if file_name.startswith("TBO") and file_name.endswith(".exr"):
        print("Valid TBO EXR File")
else:
        print("Invalid File")
```

Output

```text
Valid TBO EXR File
```

---


# Topic Summary

|----------------|-----------------------------------|
| Method         | Purpose                           |
|----------------|-----------------------------------|
| `startswith()` | Checks the beginning of a String  |
|----------------|-----------------------------------|
| `endswith()`   | Checks the end of a String        |
|----------------|-----------------------------------|
| `isdigit()`    | Checks for digits only            |
|----------------|-----------------------------------|
| `isalpha()`    | Checks for letters only           |
|----------------|-----------------------------------|
| `isalnum()`    | Checks for letters and numbers    |
|----------------|-----------------------------------|
| `isspace()`    | Checks for spaces only            |
|----------------|-----------------------------------|


These methods are useful for validating:

- File Names
- File Extensions
- Frame Numbers
- Artist Names
- Shot Names
- User Inputs


# Topic 14 Real VFX Production Examples

## Introduction

In production, we rarely use a single String Method.

Instead, multiple String Methods and Operators are used together to validate, process, and organize data.

Common use cases include:

- File Name Validation
- Shot Name Validation
- Render Output Validation
- Version Checking
- Department Detection
- Pipeline Automation

---

# Example 1 File Extension Validation

```python
file_name = "ABC_XYZ5120_Depth_v002.exr"

if file_name.endswith(".exr"):
        print("Valid EXR File")
else:
        print("Invalid File")
```

Output

```text
Valid EXR File
```

---

# Example 2 - Show Validation

```python
file_name = "ABC_XYZ5120_Depth_v002.exr"

if file_name.startwith("ABC"):
        print("ABC Project")
```

Output

```text
ABC Project
```

---

# Example 3 - Department Detection

```python
file_name = "ABC_XYZ5120_Depth_v002.exr"

if "Depth" in file_name:
        print("Depth Pass")
```

Output

```text
Depth Pass
```

---

# Example 4 - Frame Validation

```python
frame = "1050"

if frame.isdigit():
        print("Valid Frame")
```

Output

```text
Valid Frame
```

---

# Example 5 - Artist Name Validation

```python
artist = "Rajesh"

if artist.isalpha():
        print("Valid Artist Name")
```

Output

```text
Valid Artist Name
```

---

# Example 6 - Asset Name Validation

```python
asset = "CarMode101"

if asset.isalnum():
        print("Valid Asset")
```

Output

```text
Valid Asset
```

---

# Example 7 - Empty Input Validation

```python
artist = "  "

if artist.isspace():
        print("Artist Name Required")
```

Output

```text
Artist Name Required
```

---

# Example 8 - Complete Production Validation

```python
file_name = "ABC_XYZ5120_Depth_v002.exr"

if(
        file_name.startwith("ABC")
        and file_name.endswith(".exr")
        and "Depth" in file_name
):
        print("Process File")
else:
        print("Skip File")
```

Output

```text
Process File
```

---

## Production Workflow

A typical pipeline validation may check:

- Show Name
- Shot Name
- Depratment
- Version
- File Extension
- Frame Number

Only after all validations pass, the file is processed.

---

## Summary

Strings are used throughout VFX production for:

- File Names
- Render Outputs
- Folder Paths
- Shot Names
- Asset Names
- Reports
- Automation Scripts

Learning String Methods helps in building production-ready Python tools.



# Topic 15 - Practice Questions

## Objective

Practice all String concepts learned in This Class.

These Questions are designed to improve logical and strengthen understanding of Strings before moving to the Mini Project.

Topic Covered

- String Indexing
- String Slicing
- String Methods
- String Operators
- Membership Operators
- Escape Characters
- Useful String Methods

The solutions should be written in `practice.py`.


# Topic 16 - Output Prediction

## Objective

Improve logical thinking by predicting the output before executing the program.

Predicting the output helps understand how Python executes code internally.

Always follow these steps:

1. Read the code carefully. 
2. Predict the output.
3. Run the program.
4. Compare your prediction with the actual output.
5. Understand any mistakes.

Output Prediction is one of the best ways to improve programming skills.

---

## Benefits.

- Improves Logical Thinking
- Increases Problem Solving Skill
- Helps Find Mistakes
- Builds Confidence
- Improves Debugging Skills

---

## Summary

Always predict the output before running the program.

This habit helps you become a better Python programmer.


# Topic 17 - Mini Project

## Project Name - File Name Analyzer

---

## Objective

Create a Python program that analyzes a production file file name and extracts useful information 

The program should practice all important String concepts learned in This Class.

---

## Concepts Used

- String Indexing
- String Slicing
- split()
- startwith()
- endswith()
- in
- count()
- replace()


---

## Input

```text
ABC_XYZ5120_Depth_v001.exr
```

---

## Expected Output

```text
==============================
FILE REPORT
==============================

Show Name   : ABC
Shot Name   : XYZ5120
Department  : Depth
Version     : V001
Extension   : exr

Valid EXR   : True
Depth Pass  : True
Starts With : ABC

==============================
```

---


## Learnig Outcome

After completing this project, you will be able to:

- Read production file names.
- Extract information using String Methods.
- Validate file names.
- Build clean console reports.

This project simulates a simple production pipeline tool.




