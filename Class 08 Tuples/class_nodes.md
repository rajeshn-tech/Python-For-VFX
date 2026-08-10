# Class 8 - Tuples

## Topic 01 - What is Tuple?

---

## Definition

A Tuple is a collection of multiple values stored in a single variable.

Tuples are enclosed inside parentheses `()`.

---

## Why Do We Need a Tuple?

Without a Tuple:

```python
width = 1920
height = 1080
```

If there are many fixed values, we need multiple variables.

Instead, we use one Tuple.

Tuples can store:

- Strings
- Numbers
- Boolean
- Mixed Data Types

Tuple is useful when data should not change.

---

## Syntax

```python
tuple_name = (item1, item2, item3)
```

---

## Example 1

```python
shows = ("ABC", "XYZ", "KLM")

print(shows)
```

### Output

```text
('ABC', 'XYZ', 'KLM')
```

---

## Example 2

```python
frames = (1001, 1002, 1003)
print(frames)
```

### Output

```text
(1001, 1002, 1003)
```

```python
data = ("Rajesh", 1001, True)

print(data)
```

### Output

```text
('Rajesh', 1001, True)
```

---


## Example 3

```python
resolution = (1920, 1080)

print(resolution)
```

### Output

```text
(1920, 1080)
```

## Production Example

```python
plate_resolution = (4096, 2160)

print(plate_resolution)
```

### Output

```text
(4096, 2160)
```

Tuples are commonly used to store fixed values such as image resolution.


---

## Important Points

- Tuple stores multiple values.
- Uses parentheses `()`.
- Items are separated by commas.
- Tuple are ordered.
- Tuples are immutable (cannot be modified).

---

## Summary

Use a Tuple when you want to store multiple related values that should not change.

---


# Topic 2 - Creating Tuples

## Definition

A Tuple is created by placing values inside parentheses `()`.

Items are separated by commas.

---

## Why Do We Need Different Ways to Create Tuples?

Examples:

- Store artist names
- Store frame numbers
- Store resolution
- Store RGB values

---

## Syntax 

```python
tuple_name = (item1, item2, item3)
```

---

## Creating an Empty Tuple

```python
empty_tuple = ()

print(empty_tuple)
```

### Output

```text
()
```

---

## Creating a Tuple with Multiple Values

```python
shows = ("ABC", "XYZ", "KLM")

print(shows)
```

### Output

```text
('ABC', 'XYZ', 'KLM')
```

---

## Creating a Tuple with Different Data Types

```python
data = ("Rajesh", 1001, True)

print(data)
```

### Output

```text
('Rajesh', 1001, True)
```

---


## Single Item Tuple

A single value inside parentheses is **not** considered a Tuple.

Use a comma after the value.

Correct:


```python
shot = ("SH010",)

print(shot)
```

### Output

```text
('SH010',)
```

Incorrect:

```python
shot = ("SH010")

print(shot)
```

### Output

```text
SH010
```

---

## Production Example

```python
render_resolution = (4096, 2160)

print(render_resolution)
```

### Output

```text
(4096, 2160)
```

---

## Important Points

- Tuples use parentheses `()`.
- Items are separated by commas.
- Empty Tuple is `()`.
- A single-item Tuple must have a trailing comma.
- Tuples can store different data types.

---

## Summary

- Create Tuples using parentheses.
- Separate items with commas.
- Use `()` for an empty Tuple.
- Add a comma for a single-item Tuple.

---

# Topic 3 - Tuple Indexing

## Definition

Indexing is used to access individual items from a Tuple.

Python starts indexing from `0`.

---

## Why Do We Need Indexing?

Instead of printing the complete Tuple, we can access a specific item.

For Example:

- Get a Show Name
- Get a Frame Number
- Get an Artist Name
- Get Width or Height from a Resolution

---

### Syntax

```python
tuple_name[index]
```

---

## Positive Indexing

```text
Tuple

('ABC', 'XYZ', 'KLM')

 Index

   0      1      2
```

---

## Example 1

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[0])
```

### Output

```text
ABC
```

---

## Example 2

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[1])
```

### Output

```text
XYZ
```

---

## Example 3

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[2])
```

### Output

```text
KLM
```

---

## Negative Indexing

```text
Tuple

('ABC', 'XYZ', 'KLM')

 Index

  -3     -2     -1
```

---

## Example 4

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[-1])
```

### Output

```text
KLM
```

---

## Example 5

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[-2])
```

### Output

```text
XYZ
```

---

## Example 6

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[-3])
```

### Output

```text
ABC
```

---

## Production Example


```python
resolution = (4096, 2160)

print(resolution[0])
print(resolution[1])
```

### Output

```text
4096
2160
```

---

## Common Beginner Mistakes

### Mistake 1

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[3])
```

### Output

```text
IndexError: tuple index out of range
```

Reason:

The Tuple has only three items.

Valid indexes are:

```text
0
1
2
```

---

## Important  Points

- Indexing starts from `0`.
- Negative indexing starts from `-1`.
- Indexing returns a single item.
- Invalid index raises `IndexError`.

---

## Summary

- Use indexing to access a specific value.
- Positive indexing starts from the Left.
- Negative indexing start from the right.
- Index must be within the Tuple size.

---


# Topic 4 - Tuple Slicing

## Definition

Slicing is used to access multiple items from a Tuple.

Instead of accessing one item, slicing returns a new Tuple.

---

## Why Do We Need Slicing?

Sometimes we need only a part of the Tuple.

Example:

- Frist 5 frames
- Last 3 artists
- Selected shots
- First 2 resolutions

Instead of creating another Tuple manually, we use slicing.

---

## Syntax

```python
tuple_name[start:stop]
```

- `start` -> Starting index (included)
- `stop`  -> Ending index (excluded)


---

## Example Tuple

```python
shows = ("ABC", "XYZ", "KLM", "PQR", "DEF")
```

```text
Index

 0     1     2     3     4
ABC   XYZ   KLM   PQR   DEF
```

## Example 1

```python
shows = ("ABC", "XYZ", "KLM", "PQR", "DEF")

print(shows[1:4])
```

### Output

```text
('XYZ', 'KLM', 'PQR')
```

---

## Example 2

```python
shows = ("ABC", "XYZ", "KLM", "PQR", "DEF")

print(shows[:3])
```

### Output

```text
('ABC', 'XYZ', 'KLM')
```

---

## Example 3

```python
shows = ("ABC", "XYZ", "KLM", "PQR", "DEF")

print(shows[2:])
```

### Output

```text
('KLM', 'PQR', 'DEF')
```

---

## Example 4

```python
shows = ("ABC", "XYZ", "KLM", "PQR", "DEF")

print(shows[:])
```

### Output

```text
('ABC', 'XYZ', 'KLM', 'PQR', 'DEF')
```

---

## Negative Slicing

```python
shows = ("ABC", "XYZ", "KLM", "PQR", "DEF")

print(shows[-3:])
```

### Output

```text
('KLM', 'PQR', 'DEF')
```

---

## Production Example

```python
frames = (
    1001,
    1002,
    1003,
    1004,
    1005,
    1006
)

print(frames[:3])
```

### Output

```text
(1001, 1002, 1003)
```

---

## Common Beginner Mistakes

### Mistake 1

Thinking that the stop index is included.

```python
shows = ("ABC", "XYZ", "KLM", "PQR")

print(shows[1:3])
```

### Output

```text
('XYZ', 'KLM')
```

`PQR` is **not** included because the stop index is excluded.

---

##  Importnant Points

- Slicing returns a new Tuple.
- Start index is included.
- Stop index is excluded.
- Leaving `start` blank means from the beginning.
- Leaving `stop` blanks means till the end.

---

## Summary

- Use slicing to access multiple items.
- Syntax


# Topic 5 - Tuple vs List

## Definition

Both List and Tuple are used to store multiple values.

The main difference is:

- **List** -> Mutable (Can be modified)
- **Tuple** -> Immutable (Cannot be modified)

---


## Why Do We Need Both?

Choose the data structure based on your requirement.

Use a **List** when data changes frequently.

Use a **Tuple** when data should remain fixed.

---

## Syntax

### List 


```python
shows = ["ABC", "XYZ", "KLM"]
```

### Tuple

```python
shows = ("ABC", "XYZ", "KLM")
```

---

## Example 1

### List

```python
shows = ["ABC", "XYZ", "KLM"]

shows[1] = "DEF"

print(shows)
```

### Output

```text
['ABC', 'DEF', 'KLM']
```

The value was succefully modified.

---

## Example 2

### Tuple

```python
shows = ("ABC", "XYZ", "KLM")

shows[1] = "DEF"

print(shows)
```

### Output

```text
TypeError: 'Tuple' object does not support item assigment
```

The value cannot be modified because Tuples are immutable.

---

## Production Example

### List Example

```python
render_queue = [
    "Shot001",
    "Shot002",
    "Shot003"
]
```

New shots can be added or removed during production.

---

### Tuple Example

```python
resolution = (4096, 2160)
```

Image resolution is fixed, so a Tuple is a better choice.

---

## Comparison Table

| **Feature**      |**List** |**Tuple**|
|------------------|---------|---------|
| Brackets         | `[]`    | `()`    |
|------------------|---------|---------|
| Mutable          |  Yes    |  No     |
|------------------|---------|---------|
| Ordered          |  Yes    |  Yes    |
|------------------|---------|---------|
| Duplicate Values |  Yes    |  Yes    |
|------------------|---------|---------|
| Mixed Data Types |  Yes    |  Yes    |

---

## Common Beginner Mistakes

### Mistake 1

Trying to modify a Tuple.

```python
resolution = (1920, 1080)

resolution[0] = 1280
```

### Output

```text
TypeError
```

---

### Mistake 2

Using a List for fixed data.

```python
resolution = [1920, 1080]
```

A Tuple is a better choice because the resolution should not change.

---

## Important Points

- Lists use square brackets `[]`.
- Tuples use parentheses `()`.
- Lists are mutable.
- Tuples are immutable.
- Both maintain the insertion order.

---

## Summary

- Use **List** for dynamic data.
- Use **Tuple** for fixed data.
- Choose the correct data structure based on the requirement.

---

# Topic 6 - Packing and Unpacking

## Definition

### Packing

Packing means storing multiple values into a single Tuple.

### Unpacking

Unpacking means extracting Tuple values into separate variables.

---

## Why Do We Need It?

Instead of writting:

```python
width = 4096
height = 2160
```

We can write:

```python
resolution = (4096, 2160)
```

Later we can easily extract the values.

---

## Packing Syntax

```python
tuple_name = (value1, value2, value3)
```

Python also allows packing without parentheses.

```python
tuple_name = value1, value2, value3
```

Both create a Tuple.

---

## Example 1

```python
resolution = (4096, 2160)

print(resolution)
```

---

## Example 2

```python
resolution = 4096, 2160

print(resolution)
```

### Output

```text
(4096, 2160)
```

Both examples create the same Tuple.

---

## Unpacking Syntax

```python
variable1, variable2 = tuple_name
```

---

## Example 3

```python
reolution = (4096, 2160)

width, height = resolution

print(width)
print(height)
```

### Output

```text
4096
2160
```

---

## Example 4

```python
artist = ("Rajesh", "Compositing")

name, department = artist

print(name)
print(department)
```

### Output

```text
Rajesh
Compositing
```

---

## Production Examle

```python
plate_resolution = (1920, 1080)

width, height = plate_resolution

print(width)
print(height)
```

### Output

```text
1920
1080
```

A production tool can directly use `width` and `height` without accessing indexes.

---

## Common Beginner Mistakes

### Mistake 1

More variables than Tuple values.

```python
resolution = (4096, 2160)

width, height, fps = resolution
```

### Output

```text
ValueError: not enough values to unpack
```

---

### Mistake 2

Fewer variables than Tuple values.

```python
artist = ("Rajesh", "Comp", "Night")

name, department = artist
```

### Output

```text
ValueError: too many values to unpack
```

---

## Important Points

- Packing stores multiple values into one Tuple.
- Unpacking extracts Tuple into variables. 
- Number of variables and Tuple items must match.
- Parentheses are optional while packing.

---

## Summary

- Packing -> Multiple values -> One Tuple
- Unpacking -> One Tuple -> Multiple variables
- Variable count must match the number of Tuple items.

---


# Topic 7 - Tuple Methods

## Definition

Tuples have only two built-in methods:

- `count()`
- `index()`

Unlike lists, Tuples cannot be modified, so they have very few methods.

---

## Method 1 - Count()

### Definition

The `count()` method returns the number of times a value appears in a Tuple.

---

## Why Do We Nedd It?

It is used to find how many times a particular values exists.

---

## Syntax

```python
tuple_name.count(value)
```

---


## Example 1

```python
shows = ("ABC", "XYZ", "ABC", "KLM")

print(shows.count("ABC"))
```

### Output

```text
2
```

---

## Example 2

```python
numbers = (10, 20, 30, 20, 20)

print(numbers.count(20))
```

### Output

```text
3
```

---

## Production Example

```python
status = (
    "Completed",
    "Failed",
    "Completed",
    "Completed"
)

print(status.count("Completed"))
```

### Output

```text
3
```

---

## Method 2 - Index()

### Definition

The `index()` method returns the index of the first occurence of a value.

---

## Why Do We Need It?

It helps locate where a value exists in the Tuple.

---

## Syntax

```python
tuple_name.index(value)
```

---

## Example 1

```python
shows = ("ABC", "XYZ", "KLM")

print(shows.index("XYZ"))
```

### Output

```text
1
```

---

## Example 2

```python
numbers = (10, 20, 30, 20)

print(numbers.index(20))
```

### Output

```text
1
```

Only the first occurrence is returned.

---

## Production Example

```python
passes = (
    "Beauty",
    "Depth",
    "Shadow"
)

print(passes.index("Depth"))
```

### Output

```text
1
```

---

## Common Beginner Mistakes

### Mistake 1

Searching for a value that does not exist.

```python
shows = ("ABC", "XYZ")

print(shows.index("PQR"))
```

### Output

```text
ValueError: tuple.index(x): x not in tuple
```

---

## Important Points

- Tuples have only two methods.
- `count()` returns how many times a value appears.
- `index()` returns the first matching index.
- `index()` raises `ValueError` if value is not found.

---

## Summary

- `count()` -> Count occurrences.
- `index()` -> Find the first index of a value.
- These are the only two built-in Tuple methods.

---

# Topic 8 - Output Prediction

## Objective

Predict the output without running the code.

This Improves:

- Logical Thinking
- Code Reading
- Debugging Skills

---

## Question 1

```python
shows = ("ABC", "XYZ", "KLM")

print(shows[1])
```

### Output

```text
XYZ
```

---

## Question 2

```python
frames = (1001, 1002, 1003, 1004)

print(frames[-2])
```

### Output

```text
1003
```

---

## Question 3

```python
shows = ("ABC", "XYZ", "KLM", "PQR")

print(shows[1:3])
```

### Output

```text
('XYZ', 'KLM')
```

---

## Question 4

```python
resolution = (4096, 2160)

width, height = resolution

print(width)
print(height)
```

### Output

```text
4096
2160
```

## Question 5

```python
shows = ("ABC", "XYZ", "ABC", "KLM")

print(shows.count("ABC"))
```

### Output

```text
2
```

---

## Question 6

```python
shows = ("ABC", "XYZ", "KLM")

print(shows.index("KLM"))
```

### Output

```text
2
```

---


## Question 7

```python
shot = ("SH010")

print(shot)
```

### Output

```text
SH010
```

---

## Question 8

```python
shot = ("SH010",)

print(shot)
```

### Output

```text
('SH010',)
```

---

## Question 9

```python
data = ("Rajesh", 1001, True)

print(data[0])
```

### Output

```text
Rajesh
```

---

## Question 10

```python
shows = ("ABC", "XYZ")

print(shows.index("PQR"))
```

### Output

```text
ValueError
```

---

## Summary 

If you predict all the above outputs correctly, you have understand the Tuple fundamentals.


---


# Topic 9 - Mini Project

## VFX Shot Data Analyzer

### Objective

Create a simple production tool that stores fixed shot information inside a Tuple and extracts useful data.

The project will use:

- Tuple
- Indexing
- Slicing
- Packing
- Unpacking
- `count()`
- `index()`

---

## Production Data

```python
shot_data = (
    "ABC"
    "SH010",
    "Compositing",
    "Rajesh",
    1001,
    1100,
    "Completed"
)
```

The Tuple contains:

```text
Show
Shot
Department
Artist
Start Frame
Status
```

---

## Access Data USing Indexing

```python
shot_data = (
    "ABC",
    "SH010",
    "Compositing",
    "Rajesh",
    1001,
    1100,
    "Completed"
)

print(shot_data[0])
print(shot_data[1])
print(shot_data[-1])
```

### Output

```text
ABC
SH010
Completed
```

---

## Extract Data Using Slicing

```python
shot_data = (
    "ABC",
    "SH010",
    "Compositing",
    "Rajesh",
    1001,
    1100,
    "Completed"
)

print(shot_data[:4])
```

### Output

```text
('ABC', 'SH010', 'Compositing', 'Rajesh')
```

---

## Unpack Shot Data

```python
shot_data = (
    "ABC",
    "SH010",
    "Compositing",
    "Rajesh",
    1001,
    1100,
    "Completed"
)

show, shot, department, artist, start_frame, end_frame, status = shot_data

print(show)
print(shot)
print(department)
print(artist)
print(start_frame)
print(end_frame)
print(status)
```

### Output

```text
ABC
SH010
Compositing
Rajesh
1001
1100
Completed
```

---

## Tuple Method Example

```python
status_history = (
    "Pending",
    "Rendering",
    "Failed",
    "Rendering",
    "Completed"
)

print(status_history.count("Rendering"))
print(status_history.index("Failed"))
```

### Output

```text
2
2
```

---

## Important Points

- Tuple is useful for fixed production data.
- Indexing accesses one values.
- Slicing accesses multiple values.
- Unpacking stores Tuple items into separate variables.
- `count()` counts matching values.
- `index()` finds the first matching value.

---

## Summary

This project demonstrates how Tuple data can used to store and fixed VFX shot information.

