# Topic 1 - What is a Dictionary?

## Definition

A Dictionary is a collection of data stored in **Key : Value** pairs.

Dictionaries are enclosed inside curly braces `{}`.

---

## Why Do We Need Dictionary?

Without a Dictionary:

```python
artist_name = "Rajesh"
department = "Compositing"
experience = 3
shift = "Night"
```

If we have information for hundreds of artists, we need hundreds of variables.

Instead, we use one Dictionary.

A Dictionary stores related information together.

---

## Syntax

```python
dictionary_name = {
    "key": Value
}
```

---

## Example 1

```pyhthon
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Department': 'Compositing', 'Experience': 3}
```

---

## Example 2


## Example 2

```python
shot = {
    "Show": "ABC",
    "Shot": "SH010",
    "Status": "Completed"
}

print(shot)
```

### Output

```text
{'Show': 'ABC', 'Shot': 'SH010', 'Status': 'Completed'}
```

---

## Example 3

```python
blade = {
    "Blade": "Blade-01",
    "CPU": "95%",
    "RAM": "64 GB"
}

print(blade)
```

### Output

```text
{'Blade': 'Blade-01', 'CPU': '95%', 'RAM': '64 GB'}
```

---

## Production Example

```python
deadline_job = {
    "Job Name": "ABC_SH010_Comp_v001",
    "Artist": "Rajesh",
    "Department": "Compositing",
    "Status": "Completed",
    "Frames": "1001-1100"
}

print(deadline_job)
```

### Output

{'Job Name': 'ABC_SH010_Comp_v001', 'Artist': 'Rajesh', 'Department': 'Compositing', 'Status': 'Completed', 'Frames': '1001-1100'}

---


## Important Points

- Dictionary stores data in **Key : Value** pairs.
- Uses curly braces `{}`.
- Each key is separated by a colon `:`.
- Each pair is separated by a comma `,`.
- Keys should be unique.
- Values can be duplicated.

---

## Summary

Use a Dictionary when you want to store related information using meaningful names instead of numeric indexes.

---


# Topic 2 Creating Dictionaries

## Definition

A Dictionary is created using curly braces `{}`.

Each item is stored as a **Key : Value** pair.

---

## Why Do We Need Different Ways to Create Dictionaries?

Different types of data can be stored together inside a Dictionary.

Examples:

- Artist Information
- Shot Information
- Render Job Information
- Blade Information

---

## Syntax

```python
dictionary_name = {
    "Key1": Value1,
    "Key2": Value2
}
```

---

## Creating an Empty Dictionary

```python
artist = {}
print(artist)
```

### Output

```text
{}
```

--- 

## Creating a Dictionary with String Values

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Shift": "Night"
}

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Department': 'Compositing', 'Shift': 'Night'}
```

---

## Creating a Dictionary with Mixed Data Types

```python
artist = {
    "Name": "Rajesh",
    "Experience": "3",
    "Available": "True"
}

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Experience': 3, 'Available': True}
```

---


## Creating a Production Dictionary

```python
deadline_job = {
    "Job Name": "ABC_SH010_Comp_v001",
    "Artist": "Rajesh",
    "Department": "Compositing",
    "Frames": "1001-1100",
    "Status": "Completed"
}

print(deadline_job)
```

### Output

```text
{'Job Name': 'ABC_SH010_Comp_v001', 'Artist': 'Rajesh', 'Department': 'Compositing', 'Frames': '1001-1100', 'Status': 'Completed'}
```

---

## Important Points

- Dictionary uses curly braces `{}`.
- Data is stored as **Key : Value** pairs.
- Keys are separated from values using a colon `:`.
- Each pair is separated by a comma `,`.
- Keys should be unique.
- Values can be duplicated.

---

## Summary

- Create Dictionaries using `{}`.
- Store data using **Key : Value** pairs.
- Dictionaries can store different data types.

---


# Topic 3 - Accessing Dictionary Values

## Definition

Dictionary values are accessed using their **Keys**.

Unlike Lists and Tuples, Dictionaries do **not** use numeric indexes.

---

## Why Do We Need It?

Instead of remembering index numbers, we can directly access data using meaningful keys.

Example:

- Artist Name
- Department
- Status
- Frames

This makes the code easier to read.

---

## Syntax

```python
dictionary_name["Key"]
```

---

## Example 1

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist["Name"])
```

### Output

```text
Rajesh
```

---

## Example 2

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist["Department"])
```

### Output

```text
Compositing
```

---

## Example 3

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist["Experience"])
```

### Output

```text
3
```

---

## Production Example

```python
deadline_job = {
    "Job Name": "ABC_SH010_Comp_v001",
    "Artist": "Rajesh",
    "Department": "Compositing",
    "Status": "Completed",
    "Frames": "1001-1100"
}

print(deadline_job["Status"])
print(deadline_job["Frames"])
```

### Output

```text
Completed
1001-1100
```

---


## Common Beginner Mistakes

### Mistake 1

Using an index.

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

print(artist[0])
```

### Output

```text
KeyError: 0
```

Reason:

Dictionaries use **Keys**, not indexes.

---

## Mistake 2

Using a key that does not exist.

```python
artist = {
    "Name": "Rajesh"
}

print(artist["Age"])
```

### Output

```text
KeyError: 'Age'
```

---

## Important Points

- Dictionaries are accessed using keys.
- Index numbers are not used.
- The key must exist.
- Keys are case-sensitive.

---

## Summary

- Use `dictionaries["Key"]` to access values.
- Dictionaries use keys instead of indexes.
- Invalid keys raise `KeyError`.

---


# Topic 4 - Adding & Updating Dictionary Data

## Definition

A new **Key : Value** pair can be added to a Dictionary.

An existing value can also be updated.

---

## Why Do We Need It?

Production data changes frequently.

Examples:

- Artist changes
- Shot status changes
- Frame range updates
- Department updates

Instead of creating a new Dictionary, we update the existing one.

---

## Syntax

### Add a New Key

```python
dictionary_name["New Key"] = New Value
```

### Update an Existing Key

```python
dictionary_name["Existing Key"] = New Value
```

---

## Example 1 - Add New Data

```python
artist = {
    "Name": "Rajesh"
}

artist["Department"] = "Compositing"

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Department': 'Compositing'}
```

---

## Example 2 - Add Another Key

```python
artist = {
    "Name": "Rajesh"
}

artist["Experience"] = 3

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Experience': 3}
```

---

## Example 3 - Update Existing Value

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

artist["Department"] = "Lighting"

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Department': 'Lighting'}
```

---

## Production Example

```python
deadline_job = {
    "Job Name": "ABC_SH010",
    "Status": "Rendering"
}

deadline_job["Status"] = "Completed"

print(deadline_job)
```

### Output

```text
{'Job Name': 'ABC_SH010', 'Status': 'Completed'}
```

---

## Common Beginner Mistakes

### Mistake 1

Thinking that this always updates data.

```python
artist = {
    "Name": "Rajesh"
}

artist["Department"] = "Comp"
```

It **adds** a new key because `"Department"` does not exist.

---

### Mistake 2

Thinking that this adds a duplicate key.

```python
artist = {
    "Department": "Comp"
}

artist["Department"] = "Lighting"
```

### Output

```text
{'Department': 'Lighting'}
```

The old value is replaced.

No duplicate key is created.

---

## Understanding Keys and Values

In a Dictionary:

- The left side is called the **Key**.
- The right side is called the **Value**.

```python
artist = {
    "Name": "Rajesh"
}
```

```text
Key        Value
------------------------
"Name"  -> "Rajesh"
```

In this example:

- `"Name"` is a **String Key**.
- `"Rajesh"` is a **String Value**.

Both are Strings, but they have different purposes.

---

## Do Keys Always Need Quotes?

If the key is a **String**, quotes are required.

```python
artist = {
    "Department": "Compositing"
}

print(artist)
```

### Output

```text
{'Department': 'Compositing'}
```

---

If the key is a **Number**, quotes are not required.

```python
marks = {
    1: "Rajesh",
    2: "Amit"
}

print(marks)
```

### Output

```text
{1: 'Rajesh', 2: 'Amit'}
```

---

## Do Values Always Need Quotes?

Only String values need quotes.

```python
artist = {
    "Name": "Rajesh",
    "Experience": 3,
    "Available": True
}

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Experience': 3, 'Available': True}
```

Here:

- `"Rajesh"` → String → Quotes required.
- `3` → Integer → No quotes.
- `True` → Boolean → No quotes.

---

## Important Points

- String Keys → Quotes required.
- String Values → Quotes required.
- Numbers → No quotes.
- Boolean → No quotes.
- Tuples → No quotes.
- Lists → No quotes.
- If the key does not exist → A new key is added.
- If the key already exists → The value is updated.
- Keys remain unique.

---

## Summary

- Use `dictionary["Key"] = Value`
- New key → Add
- Existing key → Update

---


# Topic 5 - Removing Dictionary Data

## Definition

Dictionary data can be removed using the `del` keyword.

---

## Why Do We Need It?

Sometimes data is no longer required.

Example:

- Artist leaves the project.
- Shot is removed.
- Completed jobs are deleted.
- Old information is removed.

---

## Syntax

```python
del dictionary_name["key"]
```

---

## Example 1

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

del artist["Department"]
print(artist)
```

### Output

```text
{'Name': 'Rajesh'}
```

---

## Example 2

```python
artist  = {
    "Name": "Rajesh",
    "Experience": 3,
    "Available": True
}

del artist["Available"]
print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Experience':3}
```

---

## Example 3

```python
deadline_job = {
    "Job Name": "ABC_SH010",
    "Status": "Completed",
    "Frames": "1001-1100"
}

del deadline_job["Frames"]
print(deadline_job)
```

### Output

```text
{'Job Name': 'ABC_SH010', 'Status': 'Completed'}
```

---

## Production Example

```python
blade = {
    "Blade": "Blade-01",
    "CPU": "95%",
    "RAM": "64 GB"
}

del blade["RAM"]
print(blade)
```

### Output

```text
{'Blade': 'Blade-01', 'CPU': '95%'}
```

---

## Common Beginner Mistakes

### Mistake 1

Trying to delete a key that does not exist.

```python
artist = {
    "Name": "Rajesh"
}

del artist["Age"]
```

### Output

```text
KeyError: 'Age'
```

---

## Important Points

- Use `del` to remove data.
- `del` removes the complete key : Value pair.
- The key must exist.
- If the key does not exist, Python raises `KeyError`.

---

## Summary

- Use `del dictionary["Key"]`
- The complete key : Value pair is removed.
- Invalid keys raise `KeyError`.

---

# Topic 6 - Dictionary Methods

## Definition

Dictionaries provide built-in methods to access and retrieve data.

The most commonly used methods are:

- `keys()`
- `values()`
- `items()`
- `get()`

---

## Method 1 - keys()

## Definition

The `keys()` method returns all the keys in a Dictionary.

## Why Do We Need It?

Use this method when you want to see all the available keys in a Dictionary.

It is useful for checking what information is stored.

---

## Syntax

```python
dictionary_name.keys()
```

---

## Example

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist.keys())
```

### Output

```text
dict_keys(['Name', 'Department', 'Experience'])
```

---

## Method 2 - values()

## Definition

The `values()` method returns all the values in a Dictionary.

## Why Do We Need It?

Use this method when you want to access only the values without the keys.

It is useful for displaying or processing stored data.

---

## Syntax

```python
dictionary_name.values()
```

---

## Example

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist.values())
```

### Output

```text
dict_values(['Rajesh', 'Compositing', 3])
```

---

## Method 3 - items()

## Definition

The `items()` method returns all the Key : Value pairs in a Dictionary.

## Why Do We Need It?

Use this method when you need both the key and its value together.

It is commonly used while looping through a Dictionary.

---

## Syntax

```python
dictionary_name.items()
```

---

## Example

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist.items())
```

### Output

```text
dict_items([
    ('Name', 'Rajesh'),
    ('Department', 'Compositing'),
    ('Experience', 3)
])
```

---

## Method 4 - get()

## Definition

The `get()` method returns the value of a specified key.

## Why Do We Need It?

Unlike square brackets, `get()` does not raise a `KeyError` if the key is not found.

Instead, it returns `None`, making the code safer.

---

## Syntax

```python
dictionary_name.get("Key")
```

---

## Example 1

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

print(artist.get("Department"))
```

### Output

```text
Compositing
```

---

## Example 2

```python
artist = {
    "Name": "Rajesh"
}

print(artist.get("Age"))
```

### Output

```text
None
```

---

## Production Example

```python
deadline_job = {
    "Job Name": "ABC_SH010",
    "Artist": "Rajesh",
    "Status": "Completed"
}

print(deadline_job.get("Status"))
```

### Output

```text
Completed
```

---

## Important Points

- `keys()` → Returns all keys.
- `values()` → Returns all values.
- `items()` → Returns all Key : Value pairs.
- `get()` → Returns the value of a specified key.
- `get()` returns `None` if the key is not found.
- `get()` does not raise a `KeyError` for missing keys.

---

## Summary

| Method     | Purpose                              |
|------------|--------------------------------------|
| `keys()`   | Returns all keys                     |
| `values()` | Returns all values                   |
| `items()`  | Returns all Key : Value pairs        |
| `get()`    | Returns the value of a specified key |

---


# Topic 7 - Looping Through Dictionary

## Definition

Looping is used to access Dictionary data one item at a time.

You can loop through:

- Keys
- Values
- Key : Value pairs

--- 

## Why Do We Need It?

Instead of accessing each dictionary item manually, we use a loop.

This is useful when a Dictionary contains many entries.

---


## Method 1 - Loop Through Keys

## Definition

This loop returns all the keys in a Dictionary.

--- 

## Syntax

```python
for key in dictionary_name:
    print(key)
```

---

## Example

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

for key in artist:
    print(key)
```

### Output

```text
Name
Department
Experience
```

---

## Method 2 - Loop Through Values

## Definition

This loop returns all the values in Dictionary.

---

## Syntax

```python
for value in dictionary_name.value():
    print(value)
```

---

## Example

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

for value in artist.value():
    print(value)
```

## Output

```text
Rajesh
Compositing
3
```

---

## Method 3 - Loop Through Keys and Values

## Definition

This loop returns both the key and its value together.

---

## Syntax

```python
for key, value in dictionary_name.items():
    print(key, value)
```

---

## Example

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

for key, value in artist.items():
    print(key, ":", value)
```

### Output

```text
Name : Rajesh
Department : Compositing
Experience : 3
```

---

## Production Example

```python
deadline_job = {
    "Job Name": "ABC_SH010",
    "Artist": "Rajesh",
    "Status": "Completed"
}

for key, value in deadline_job.items():
    print(key, ":", value)
```

### Output

```text
Job Name : ABC_SH010
Artist : Rajesh
Status : Completed
```

---

## Important Points

- `for key in dictionary` -> Returns all keys.
- `dictionary.values()` -> Returns all values.
- `dictionary.items()` -> Returns both keys and values.
- `items()` is the most commonly used method while looping.

---

## Summary


|               Loop                     | Returns         |
|----------------------------------------|-----------------|
| `for key in dictionary`                | Keys            |
| `for value in dictionary.values()`     | Values          |
| `for key, value in dictionary.items()` | Keys and Values |

---

# Topic 8 - Mini Project

## Deadline Job Information Tool

### Objective

Create a simple production tool to display and update Deadline job information using a Dictionary.

This project uses:

- Dictionary
- Accessing Values
- Adding Data
- Updating Data
- Removing Data
- Dictionary Methods
- Looping

---

## Production Data

```python
job = {
    "Job Name": "ABC_SH010_Comp_v001",
    "Artist": "Rajesh",
    "Department": "Compositing",
    "Frames": "1001-1100",
    "Status": "Rendering"
}
```

---

## Display Job Information

```python
print(job["Job Name"])
print(job["Artist"])
print(job["Status"])
```

### Output

```text
ABC_SH010_Comp_v001
Rajesh
Rendering
```

---

## Update Job Status

```python
job["Status"] = "Completed"

print(job["Status"])
```

### Output

```text
Completed
```

---

## Add Priority

```python
job["Priority"] = 80

print(job)
```

### Output

```text
{'Job Name': 'ABC_SH010_Comp_v001', 'Artist': 'Rajesh', 'Department': 'Compositing', 'Frames': '1001-1100', 'Status': 'Completed', 'Priority': 80}
```

---

## Remove Frames

```python
del job["Frames"]

print(job)
```

### Output

```text
{'Job Name': 'ABC_SH010_Comp_v001', 'Artist': 'Rajesh', 'Department': 'Compositing', 'Status': 'Completed', 'Priority': 80}
```

---

## Display Complete Report

```python
for key, value in job.items():
    print(key, ":", value)
```

### Output

```text
Job Name : ABC_SH010_Comp_v001
Artist : Rajesh
Department : Compositing
Status : Completed
Priority : 80
```

---

## Important Points

- A Dictionary stores production data using Key : Value pairs.
- Existing values can be updated.
- New data can be added.
- Unwanted data can be removed.
- `items()` is useful for displaying complete reports.

---

## Summary

This project demonstrates how Dictionaries are used to manage production information in a VFX pipeline.

---

# Topic 9 - Output Prediction

## Objective

Predict the output without running the code.

This improves:

- Logical Thinking
- Code Reading
- Debugging Skills

---

## Question 1

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

print(artist["Name"])
```

### Output

```text
Rajesh
```

---

## Question 2

```python
artist = {
    "Name": "Rajesh"
}

artist["Department"] = "Lighting"

print(artist)
```

### Output

```text
{'Name': 'Rajesh', 'Department': 'Lighting'}
```

---

## Question 3

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

del artist["Department"]

print(artist)
```

### Output

```text
{'Name': 'Rajesh'}
```

---

## Question 4

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist.keys())
```

### Output

```text
dict_keys(['Name', 'Department', 'Experience'])
```

---

## Question 5

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing",
    "Experience": 3
}

print(artist.values())
```

### Output

```text
dict_values(['Rajesh', 'Compositing', 3])
```

---

## Question 6

```python
artist = {
    "Name": "Rajesh"
}

print(artist.get("Age"))
```

### Output

```text
None
```

---

## Question 7

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

for key in artist:
    print(key)
```

### Output

```text
Name
Department
```

---

## Question 8

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

for value in artist.values():
    print(value)
```

### Output

```text
Rajesh
Compositing
```

---

## Question 9

```python
artist = {
    "Name": "Rajesh",
    "Department": "Compositing"
}

for key, value in artist.items():
    print(key, ":", value)
```

### Output

```text
Name : Rajesh
Department : Compositing
```

---

## Question 10

```python
artist = {
    "Name": "Rajesh"
}

print(artist["Age"])
```

### Output

```text
KeyError: 'Age'
```

---

## Summary

If you can predict all the above outputs correctly, you have understood the fundamentals of Dictionaries.

---