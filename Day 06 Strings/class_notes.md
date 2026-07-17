# Day 06 - Strings

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