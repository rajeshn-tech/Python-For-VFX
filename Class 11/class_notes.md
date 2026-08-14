# Class 10 - Sets

# Topic 1 - What is a Set?

## Definition

A Set is a collection of unique values stored in a single variable.

Sets are enclosed inside curly braces `{}`.

---

## Why Do We Need a Set?

A Set is useful when we want to store unique values and remove duplicate data.

For example, suppose a render report contains repeated artist names:

```python
artists = {"Rajesh", "Amit", "Rajesh", "Pankaj", "Amit"}

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Amit', 'Pankaj'}
```

Duplicate values are automatically removed.

> Note: The order of Set items may be different when you run the code.

---

## Syntax

```python
set_name = {item1, item2, item3}
```

---

## Example 1

```python
shows = {"ABC", "XYZ", "KLM"}

print(shows)
```

### Possible Output

```text
{'ABC', 'XYZ', 'KLM'}
```

---

## Example 2

```python
frames = {1001, 1002, 1003}

print(frames)
```

### Possible Output

```text
{1001, 1002, 1003}
```

---

## Example 3 - Duplicate Values

```python
artists = {"Rajesh", "Amit", "Rajesh", "Pankaj", "Amit"}

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Amit', 'Pankaj'}
```

The duplicate `"Rajesh"` and `"Amit"` values are automatically removed.

---

## Production Example

Suppose a Deadline report contains jobs from multiple departments.

Some department names appear many times.

```python
departments = {
    "Compositing",
    "Lighting",
    "Compositing",
    "FX",
    "Lighting"
}

print(departments)
```

### Possible Output

```text
{'Compositing', 'Lighting', 'FX'}
```

A Set keeps only the unique department names.

---

## Important Points

- A Set stores multiple values.
- Sets use curly braces `{}`.
- Set items are unique.
- Duplicate values are automatically removed.
- Sets are unordered.
- Set items do not have fixed index positions.
- Set output order may change.

---

## Summary

Use a Set when you want to store unique values and automatically remove duplicates.

---

# Topic 2 - Creating Sets

## Definition

A Set can be created using curly braces `{}` or the `set()` function.

A Set can store different types of values.

---

## Why Do We Need It?

We create Sets when we need a collection of unique values.

Examples:

- Unique Artists
- Unique Departments
- Unique Shows
- Unique Status Values
- Unique Frame Numbers

---

## Syntax

```python
set_name = {item1, item2, item3}
```

---

## Example 1 - String Values

```python
shows = {"ABC", "XYZ", "KLM"}

print(shows)
```

### Possible Output

```text
{'ABC', 'XYZ', 'KLM'}
```

---

## Example 2 - Number Values

```python
frames = {1001, 1002, 1003}

print(frames)
```

### Possible Output

```text
{1001, 1002, 1003}
```

---

## Example 3 - Mixed Values

```python
data = {"Rajesh", 1001, True}

print(data)
```

### Possible Output

```text
{'Rajesh', 1001, True}
```

The order may be different because Sets are unordered.

---

## Creating an Empty Set

An empty Set is created using `set()`.

```python
artists = set()

print(artists)
```

### Output

```text
set()
```

---

## Important - Empty Curly Braces

This does **NOT** create an empty Set:

```python
artists = {}

print(type(artists))
```

### Output

```text
<class 'dict'>
```

Empty curly braces `{}` create an empty Dictionary.

To create an empty Set:

```python
artists = set()

print(type(artists))
```

### Output

```text
<class 'set'>
```

---

## Production Example

```python
departments = {
    "Compositing",
    "Lighting",
    "FX",
    "Rendering"
}

print(departments)
```

### Possible Output

```text
{'Compositing', 'Lighting', 'FX', 'Rendering'}
```

---

## Important Points

- Sets are created using curly braces `{}`.
- Items are separated by commas.
- Sets can store different data types.
- Duplicate values are automatically removed.
- Sets are unordered.
- Use `set()` to create an empty Set.
- `{}` creates an empty Dictionary, not an empty Set.

---

## Summary

```python
shows = {"ABC", "XYZ", "KLM"}
```

Creates a Set with values.

```python
shows = set()
```

Creates an empty Set.

```python
shows = {}
```

Creates an empty Dictionary.

---

# Topic 3 - Adding Items

## Definition

The `add()` method is used to add a single item to a Set.

---

## Why Do We Need It?

Use `add()` when you want to add a new value to an existing Set.

For example:

- Add a new Artist
- Add a new Department
- Add a new Show
- Add a new Status

---

## Syntax

```python
set_name.add(value)
```

---

## Example 1

```python
artists = {"Rajesh", "Amit"}

artists.add("Suresh")

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Amit', 'Suresh'}
```

---

## Example 2 - Add a Number

```python
frames = {1001, 1002, 1003}

frames.add(1004)

print(frames)
```

### Possible Output

```text
{1001, 1002, 1003, 1004}
```

---

## Example 3 - Add a Duplicate Item

```python
artists = {"Rajesh", "Amit"}

artists.add("Rajesh")

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Amit'}
```

`"Rajesh"` is not added again because Sets do not allow duplicate values.

---

## Production Example

```python
departments = {"Compositing", "Lighting", "FX"}

departments.add("Rendering")

print(departments)
```

### Possible Output

```text
{'Compositing', 'Lighting', 'FX', 'Rendering'}
```

---

## Important Points

- `add()` adds one item to a Set.
- Use `set_name.add(value)` to add an item.
- Duplicate values are not added.
- Set items remain unique.
- Set output order may change.

---

## Summary

Use `add()` when you want to add a single item to an existing Set.

```python
set_name.add(value)
```

---

# Topic 4 - Removing Items

## Definition

Set items can be removed using the `remove()` and `discard()` methods.

---

## Why Do We Need It?

Use these methods when an item is no longer required in a Set.

Examples:

- Remove an Artist
- Remove a Department
- Remove a Show
- Remove a Status

---

# Method 1 - remove()

## Definition

The `remove()` method removes a specified item from a Set.

---

## Syntax

```python
set_name.remove(value)
```

---

## Example

```python
artists = {"Rajesh", "Amit", "Suresh"}

artists.remove("Amit")

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Suresh'}
```

---

## Important - Missing Item

If the item does not exist, `remove()` raises a `KeyError`.

```python
artists = {"Rajesh", "Amit"}

artists.remove("Suresh")
```

### Output

```text
KeyError: 'Suresh'
```

---

# Method 2 - discard()

## Definition

The `discard()` method also removes a specified item from a Set.

The main difference is that it does not raise an error if the item does not exist.

---

## Syntax

```python
set_name.discard(value)
```

---

## Example

```python
artists = {"Rajesh", "Amit", "Suresh"}

artists.discard("Amit")

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Suresh'}
```

---

## Missing Item with discard()

```python
artists = {"Rajesh", "Amit"}

artists.discard("Suresh")

print(artists)
```

### Possible Output

```text
{'Rajesh', 'Amit'}
```

No error occurs.

---

## Production Example

```python
failed_blades = {"Blade01", "Blade02", "Blade03"}

failed_blades.discard("Blade02")

print(failed_blades)
```

### Possible Output

```text
{'Blade01', 'Blade03'}
```

---

## remove() vs discard()

| Method | Item Exists | Item Does Not Exist |
|--------|-------------|---------------------|
| `remove()` | Removes item | `KeyError` |
| `discard()` | Removes item | No error |

---

## Important Points

- `remove()` removes a specified item.
- `discard()` also removes a specified item.
- `remove()` raises `KeyError` if the item does not exist.
- `discard()` does not raise an error if the item does not exist.
- Set output order may change.

---

## Summary

```python
set_name.remove(value)
```

Removes an item, but can raise `KeyError`.

```python
set_name.discard(value)
```

Removes an item without raising an error for a missing value.

---

# Topic 5 - Set Operations

## Definition

Set operations are used to compare and combine Sets.

The main Set operations are:

- `union()`
- `intersection()`
- `difference()`

---

# Method 1 - union()

## Definition

The `union()` method combines two Sets and returns all unique values.

---

## Why Do We Need It?

Use `union()` when you want to combine data from two Sets.

Duplicate values are automatically removed.

---

## Syntax

```python
set_a.union(set_b)
```

---

## Example

```python
set_a = {"ABC", "XYZ", "KLM"}
set_b = {"KLM", "PQR", "DEF"}

result = set_a.union(set_b)

print(result)
```

### Possible Output

```text
{'ABC', 'XYZ', 'KLM', 'PQR', 'DEF'}
```

---

## Production Example

```python
rendering_shots = {"SH010", "SH020", "SH030"}
completed_shots = {"SH020", "SH040"}

all_shots = rendering_shots.union(completed_shots)

print(all_shots)
```

### Possible Output

```text
{'SH010', 'SH020', 'SH030', 'SH040'}
```

---

# Method 2 - intersection()

## Definition

The `intersection()` method returns values that are common in both Sets.

---

## Why Do We Need It?

Use `intersection()` when you want to find matching values between two Sets.

---

## Syntax

```python
set_a.intersection(set_b)
```

---

## Example

```python
set_a = {"ABC", "XYZ", "KLM"}
set_b = {"KLM", "XYZ", "PQR"}

result = set_a.intersection(set_b)

print(result)
```

### Possible Output

```text
{'XYZ', 'KLM'}
```

---

## Production Example

```python
rendering_shots = {"SH010", "SH020", "SH030", "SH040"}
high_priority = {"SH020", "SH040", "SH050"}

result = rendering_shots.intersection(high_priority)

print(result)
```

### Possible Output

```text
{'SH020', 'SH040'}
```

---

# Method 3 - difference()

## Definition

The `difference()` method returns values that exist in the left Set but do not exist in the right Set.

---

## Why Do We Need It?

Use `difference()` when you want to find what remains after removing matching values.

---

## Syntax

```python
set_a.difference(set_b)
```

---

## Example

```python
set_a = {10, 20, 30, 40}
set_b = {20, 40}

result = set_a.difference(set_b)

print(result)
```

### Possible Output

```text
{10, 30}
```

---

## How difference() Works

```text
set_a = MAIN SET
set_b = CHECK / REMOVE SET

set_a.difference(set_b)

20 -> Found in set_b -> Remove
40 -> Found in set_b -> Remove

Remaining:

10
30
```

---

## Direction is Important

```python
set_a = {10, 20, 30, 40}
set_b = {20, 50}

print(set_a.difference(set_b))
```

### Possible Output

```text
{10, 30, 40}
```

But:

```python
print(set_b.difference(set_a))
```

### Possible Output

```text
{50}
```

The Set on the left side is the main Set.

---

## Production Example

```python
all_shots = {"SH010", "SH020", "SH030", "SH040"}
completed_shots = {"SH010", "SH030"}

pending_shots = all_shots.difference(completed_shots)

print(pending_shots)
```

### Possible Output

```text
{'SH020', 'SH040'}
```

---

## Important Points

- `union()` -> Combines both Sets.
- `intersection()` -> Returns common values.
- `difference()` -> Returns values from the left Set that are not in the right Set.
- Set output order may change.
- Duplicate values are automatically removed.

---

## Summary

```text
union()        -> Combine both Sets
intersection() -> Common values
difference()   -> Left Set - Matching Right Set values
```

---

# Topic 6 - Set Methods

## Definition

Sets provide built-in methods to perform different operations on Set data.

We have already learned:

- `add()`
- `remove()`
- `discard()`
- `union()`
- `intersection()`
- `difference()`

In this topic, we will learn:

- `clear()`
- `copy()`

---

# Method 1 - clear()

## Definition

The `clear()` method removes all items from a Set.

The Set still exists, but it becomes empty.

---

## Why Do We Need It?

Use `clear()` when you want to remove all existing values from a Set.

---

## Syntax

```python
set_name.clear()
```

---

## Example

```python
artists = {"Rajesh", "Amit", "Suresh"}

artists.clear()

print(artists)
```

### Output

```text
set()
```

---

## Production Example

```python
failed_blades = {"Blade01", "Blade02", "Blade03"}

failed_blades.clear()

print(failed_blades)
```

### Output

```text
set()
```

All items are removed from the Set.

---

# Method 2 - copy()

## Definition

The `copy()` method creates a copy of an existing Set.

---

## Why Do We Need It?

Use `copy()` when you want to keep a separate copy of Set data before modifying the original Set.

---

## Syntax

```python
new_set = original_set.copy()
```

---

## Example

```python
departments = {"Compositing", "Lighting", "FX"}

backup = departments.copy()

print(backup)
```

### Possible Output

```text
{'Compositing', 'Lighting', 'FX'}
```

---

## Production Example

```python
failed_blades = {"Blade01", "Blade02", "Blade03"}

backup = failed_blades.copy()

failed_blades.clear()

print(failed_blades)
print(backup)
```

### Possible Output

```text
set()
{'Blade01', 'Blade02', 'Blade03'}
```

`failed_blades` becomes empty, but the copied data remains available in `backup`.

---

## Important Points

- `clear()` removes all items from a Set.
- `clear()` does not delete the Set itself.
- An empty Set is displayed as `set()`.
- `copy()` creates a separate copy of a Set.
- Changes to the original Set do not affect the copied Set.
- Set output order may change.

---

## Summary

```text
clear() -> Remove all items
copy()  -> Create a copy of the Set
```

---


# Topic 7 - Looping Through Sets

## Definition

A `for` loop is used to access Set items one by one.

---

## Why Do We Need It?

Use a `for` loop when you want to process or display every item stored in a Set.

Example:

- Display unique Artists
- Display unique Departments
- Display failed Blades
- Display unique Shots

---

## Syntax

```python
for item in set_name:
        print(item)
```

---

## Example 1

```python
shows = {"ABC", "XYZ", "KLM"}

for show in shows:
        print(show)
```

### Possible Output

```text
ABC
XYZ
KLM
```

The Output order may be different because Sets are unordered.

---

## Example 2

```python
frames = {1001, 1002, 1003}

for frame in frames:
        print("Frame:", frame)
```

### Possible Output

```text
Frame: 1001
Frame: 1002
Frame: 1003
```

---

## Production Example

```python
failed_blades = {"Blade01", "Blade02", "Blade03"}

for blade in failed_blades:
        print("Failed Blade:", blade)
```

### Possible Output

```text
Failed Blade: Blade01
Failed Blade: Blade02
Failed Blade: Blade03
```

---

## Printing a Set vs Looping Through a Set

Printing the Set Directly:

```python
shots = {"SH010", "SH020", "SH030"}

print(shots)
```

### Possible Output

```text
{'SH010', 'SH020', 'SH030'}
```

The complete Set is printed at once.

Using a `for` loop:

```python
shots = {"SH010", "SH020", "SH030"}

for shot in shots:
        print(shot)
```

### Possible Output

```text
SH010
SH020
SH030
```

Each item is printed separately.

---

## Important Points

- A `for` loop accesses Set items one by one.
- Each loop interation processes one item.
- Set items do not have fixed positions.
- Set output order may change.
- `print(set_name)` prints the complete Set.
- A `for` loop can print each Set item separately.

---

## Summary

```python
for item in set_name:
        print(item)
```

Use a `for` loop when you want to access every item in a Set one bye one.

---

