# Day 02 - User Input & Data Types

## Topics

- input()
- Data Types
- type()
- Type Conversion

---

# Topic 1 - input()

## What is input()?

The `input()` function is used to take information from the user while the program is running.

## Syntax

```python
variable_name = input("Enter Value : ")
```

## Example

```python
name = input("Enter Your Name : ")

print(name)
```

## Important Rule

`input()` always returns a **String (str)**, even if the user enters a number.

### Example

Input

```
25
```

Output Type

```python
<class 'str'>
```

## Real VFX Example

```text
Project Name      → String
Sequence Name     → String
Shot Name         → String
Artist Name       → String
Width             → Integer
Height            → Integer
Gamma             → Float
Render Completed  → Boolean
```

---

# Topic 2 - Data Types

## Common Data Types

| Data Type | Example |
|-----------|---------|
| String | "Rajesh" |
| Integer | 1920 |
| Float | 2.2 |
| Boolean | True |

### Example

```python
artist_name = "Rajesh"
width = 1920
gamma = 2.2
render_completed = True
```

---

# Topic 3 - type()

## What is type()?

The `type()` function is used to check the data type of a variable.

## Syntax

```python
print(type(variable_name))
```

## Example

```python
width = 1920

print(type(width))
```

### Output

```python
<class 'int'>
```

---

# Topic 4 - Type Conversion

## What is Type Conversion?

Type conversion is used to change one data type into another.

## Common Functions

```python
int()
float()
str()
bool()
```

## Example

```python
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print(num1 + num2)
```

## Production Note

Type conversion is commonly used in VFX pipelines when reading values from:

- User Input
- Nuke Panels
- EXR Metadata
- CSV Files
- JSON Files