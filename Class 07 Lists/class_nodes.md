# Topic 1 - What is a List?

## Definition

A List is a collection of multiple values stored in a single variable.

List are enclosed inside square brackets `[]`.

---

## Why Do We Need a List?

without a List:

```python
show_1 = "ABC"
show_2 = "XYZ"
show_3 = "KLM"
```
If there are 500 shows, we need 500 variables.

Instead, we use one List.

Lists can store:

- Strings
- Numbers
- Boolean
- Mixed Data Types

---

## Syntax

```python
list_name = [item1, item2, item3]
```
---

## Example 1

```python
shows = ["ABC", "XYZ", "KLM"]
print(shows)
```

### Output

```text
['ABC', 'XYZ', 'KLM']
```

---

## Example 2

```python
frames = [1001, 1002, 1003]
print(frames)
```

### Output

```text
[1001, 1002, 1003]
```

```python
data = ["Rajesh", 1001, True]
print(data)
```

### Output

```text
['Rajesh', 1001, True]
```

---


## Example 3

```python
data = ["Rajesh", 1001, True]

print(data)
```

### Output

```text
['Rajesh', 1001, True]
```

## Production Example


```python
render_files = [
    "ABC_SH010_v001.exr",
    "ABC_SH020_v001.exr",
    "ABC_SH030_v001.exr"
]

print(render_files)
```

### Output

```text
['ABC_SH010_v001.exr',
 'ABC_SH020_v001.exr',
 'ABC_SH030_v001.exr']
```

--- 

## Important Points

- List stores multiple values.
- Uses square brackets`[]`.
- Items are separatedby commas.
- Lists are ordered.
- Lists are mutable.

---

## Summary

Use a List when you want to store multiple related values in a single variable.

---

# Topic 2 - Lists Indexing

## Definition

List Indexing is used to access a specific item from a List.

Index always starts from `0`.

---

## Syntax

```python
list_name[index]
```

---

## Example

```python
shows = ["ABC", "XYZ", "KLM"]

print(shows[0])
print(shows[1])
print(shows[2])
```

### Output

```text
ABC
XYZ
KLM
```

---

## Negative Indexing

```python
shows = shows = ["ABC", "XYZ", "KLM"]

print(shows[-1])
print(shows[-2])
```

### Output

```text
KLM
XYZ
```

## Production Example

```python
render_files = [
    "ABC_SH010_v001.exr",
    "ABC_SH020_v001.exr",
    "ABC_SH030_v001.exr" 
]

print(render_files[0])
print(render_files[-1])
```

### Output

```text
ABC_SH010_v001.exr
ABC_SH030_v001.exr
```

---

## Important Points

- Index Starts from `0`.
- Negative index starts from `-1`.
- Every item has its own index.
- Access one item at a time.

---

## Summary

Use indexing when you need a specific item from a List.

---

Memory Visualization

Index

  0      1     2
┌─────┬─────┬─────┐
│ ABC │ XYZ │ KLM │
└─────┴─────┴─────┘
 -3     -2     -1

---


# Topic 3 - List Slicing

## Definition

List Slicing is used to access multple items from a List.

---

## Syntax

```python
list_name[start : stop]
```

or

```python
list_name[start : stop : step]
```

---

## Example 

```python
shows = ["ABC", "XYZ", "KLM", "PQR", "DEF"]

print(shows[1:4])
```
### Output

```text
['XYZ', 'KLM', 'PQR']
```

---

## Example

```python
print(shows[2:])
```

### Output

```text
['KLM', 'PQR', 'DEF']
```

---

## Production Example

```python
render_files = [
    "ABC_SH010_v001.exr",
    "ABC_SH020_v001.exr",
    "ABC_SH030_v001.exr",
    "ABC_SH040_v001.exr",
    "ABC_SH050_v001.exr"
]

print(render_files[1:4])
```

### Output

```text
[
'ABC_SH020_v001.exr',
'ABC_SH030_v001.exr',
'ABC_SH040_v001.exr'
]
```

---

## Important Points

- Slicing returns multiple items.
- Start index is included.
- Stop index is excluded.
- Step is optional.

---

## Summary

USe slicing when you need a portion of a List.

---

# Topic 4 - Accessing & Modifying List Items

## Definition

List items can be accessed using an index.

Unlike Strings, List items can also be modified.

---

## Syntax
### Access Item

```python
list_name[index]
```

### Modify Item

```python
list_name[index] = new_value
```

---

## Example

```python
shows = ["ABC", "XYZ", "KLM"]

print(shows[1])

shows[1] = "PQR"

print(shows)
```

### Output

```text
XYZ
['ABC', 'PQR', 'KLM']
```

---

## Production Example

```python
render_files = [
    "ABC_SH010_v001.exr",
    "ABC_SH020_v001.exr",
    "ABC_SH030_v001.exr"
]

render_files[2] = "ABC_SH030_v002.exr"

print(render_files)
```

### Output

```text
[
    "ABC_SH010_v001.exr",
    "ABC_SH020_v001.exr",
    "ABC_SH030_v001.exr"
]
```

---

## Important Points

- Use indexing to access an item.
- Use indexing with `=` to modify an item.
- Lists are multiple.
- Strings are immutable.

---

## Summary

Lists allow both accessing and modifying items using indexes.


---

# Topic 5 append()


## Definition

The `append()` method is used to add a new item at the end of a List.

The existing items are not changed.

---

## Why do we need append()?

Without `append()`, we can only replace existing items.

```python
shows = ["ABC", "XYZ", "KLM"]

shows[1] = "BTT"
```

Output

```text
['ABC', 'BTT', 'KLM']
```

Here, `XYZ` is replaced by `BTT`.

Sometimes we don't want to replace an item.

We want to keep all existing items and add a new one.

for that, we use `append()`.

---

## Syntax

```python
list_name.append(item)
```

---

## Memory Visualization

Before

```text
Index

0      1      2
┌────┬────┬────┐
│ABC │XYZ │KLM │
└────┴────┴────┘
```

Code

```python
shows.append("BTT")
```

After

```text
Index

0      1      2      3
┌────┬────┬────┬────┐
│ABC │XYZ │KLM │OTT │
└────┴────┴────┴────┘
```

Notice:

Nothing is replaced.

A new item is added at the end.

---

## Example 1

```python
shows = ["ABC", "XYZ", "KLM"]

shows.append("BTT")
print(shows)
```

### Output

```text
['ABC', 'XYZ', 'KLM', 'BTT']
```

---

## Example 2

```python
frames = [1001, 1002]

frames.append(1003)

print(frames)
```

### Output

```text
[1001, 1002, 1003]
```

---

## Production Example

```python
render_files = []

render_files.append("ABC_SH010_v001.exr")
render_files.append("ABC_SH020_v001.exr")
render_files.append("ABC_SH030_v001.exr")

print(render_files)
```

### Output

```text
['ABC_SH010_v001.exr', 'ABC_SH020_v001.exr', 'ABC_SH030_v001.exr']
```

---

## append() vs Modify

Replace Item

```python
shows = ["ABC", "XYZ", "KLM"]

shows[1] = "BTT"
```

### Output

```text
['ABC', 'BTT', 'KLM']
```

Add New Item

```python
shows = ["ABC", "XYZ", "KLM"]

shows.append("BTT")
```

### Output

```text
['ABC', 'XYZ', 'KLM', 'BTT']
```

---

## Common Beginner Mistake

Forgetting brackets

```python
shows = ["ABC", "XYZ", "KLM"]
shows.append
```

Correct

```python
shows = ["ABC", "XYZ", "KLM"]
shows.append("BTT")
```

---

Using square brackets

```python
shows = ["ABC", "XYZ", "KLM"]
shows.append["BTT"]
```

Correct

```python
shows = ["ABC", "XYZ", "KLM"]
shows.append("BTT")
```

---

## Important Points

- `append()` always adds one item.
- The new item is added at the end.
- Existing items are not replaced.
- List size increases by one.
- append() always adds an item at the end of the List.

---

## Summary

Use `append()` when you want to add a new item to the end of a List.

---

# Topic 6 - `insert()`

## Definition

The `insert()` method is used to add a new item at a specific position (index) in a List.

The existing items are **not replaced**.

Instead, all items from that position move one step to the right.

---

## Why do we need `insert()`?

The `append()` method always adds a new item at the end of the List.

Sometimes we need to add a new item at the beginning or in the middle while keeping the existing order.

For that, we use `insert()`

---

## Syntax

```python
list_name.insert(index, item)
```

---

## Memory Visualization

### Before

```text

0      1      2
┌────┬────┬────┐
│ABC │XYZ │KLM │
└────┴────┴────┘
```

### Code

```python
shows.insert(1, "BTT")
```

### After

```text
Index

0      1      2      3
┌────┬────┬────┬────┐
│ABC │BTT │XYZ │KLM │
└────┴────┴────┴────┘
```

Notice:

- `ABC` remains at index 0.
- `BTT` is inserted at index 1.
- `XYZ` moves from index 1 to index 2.
- `KLM` moves from index 2 to index 3.
- Nothing is replaced.

---

## How `insert()` Works

Suppose we have:

```python
shows = ["ABC", "XYZ", "KLM"]
```

Memory:

```text
0 → ABC
1 → XYZ
2 → KLM
```

Now write:

```python
shows.insert(1, "BTT")
```

Python internally performs these steps:

### Step 1

Go to index **1**.

### Step 2

Create space at index **1**.

### Step 3

Move every item from index **1** one position to the right.

```text
0 → ABC
1 → ____
2 → XYZ
3 → KLM
```

### Step 4

Store the new value.

```text
0 → ABC
1 → BTT
2 → XYZ
3 → KLM
```

---

## Example 1

```python
shows = ["ABC", "XYZ", "KLM"]

shows.insert(1, "BTT")

print(shows)
```

### Output

```text
['ABC', 'BTT', 'XYZ', 'KLM']
```

---

## Example 2

```python
frames = [1001, 1003]

frames.insert(1, 1002)

print(frames)
```

### Output

```text
[1001, 1002, 1003]
```

---

## Production Example

```python
render_queue = [
    "SH010",
    "SH030",
    "SH040"
]

render_queue.insert(1, "SH020")

print(render_queue)
```

### Output

```text
['SH010', 'SH020', 'SH030', 'SH040']
```

---

## `append()` vs `insert()`

### append()

```python
shows = ["ABC", "XYZ", "KLM"]

shows.append("BTT")
```

### Output

```text
['ABC', 'XYZ', 'KLM', 'BTT']
```

`append()` always adds the new item at the end.

---

### insert()

```python
shows = ["ABC", "XYZ", "KLM"]

shows.insert(1, "BTT")
```

### Output

```text
['ABC', 'BTT', 'XYZ', 'KLM']
```

`insert()` adds the new item at the specified index.

---

## Common Beginner Mistakes

### Forgetting the index

```python
shows.insert("BTT")
```

Correct

```python
shows.insert(1, "BTT")
```

---

### Wrong parameter order

```python
shows.insert("BTT", 1)
```

Correct

```python
shows.insert(1, "BTT")
```

---

### Thinking `insert()` replaces an item

```python
shows = ["ABC", "XYZ", "KLM"]

shows.insert(1, "BTT")
```

Wrong expectation

```text
['ABC', 'BTT', 'KLM']
```

Correct Output

```text
['ABC', 'BTT', 'XYZ', 'KLM']
```

`XYZ` is not removed.

It is shifted one position to the right.

---


## Important Points

- `insert()` adds only one item at a time.
- You can insert an item at any valid index.
- Existing items are shifted to the right.
- No existing item is replaced.
- The List size increases by one.
- Use `insert()` when you want to maintain the order of the List.

---

## Summary

Use `insert()` when you want to add a new item at a specific position in a List.

- `append()` -> Adds an item at the end.
- `insert()` -> adds an item at a specific index.

---

# Topic 7 `remove()`

## Definition

The `remove()` method is used to remove a specific item from a List.

The item is removed by its **value**, not its index.

After removing the item, all remaining items shift one position to the left.

---

## Why do we need `remove()`?

Sometimes we know the value that we want to remove from a List.

For example, we want to remove the show `"XYZ"`.

Instead of remembering its index, we can directly remove it using its value.

For that, we use `remove()`.

---

## Syntax

```python
list_name.remove(item)
```

---

## Memory Visualization

## Before

```text
Index

0      1      2      3
┌────┬────┬────┬────┐
│ABC │XYZ │KLM │BTT │
└────┴────┴────┴────┘
```

### Code

```python
shows.remove("XYZ")
```

### After

```text
Index

0      1      2
┌────┬────┬────┐
│ABC │KLM │BTT │
└────┴────┴────┘
```

Notice:

- `XYZ` is removed.
- `KLM` shifts from index 2 to index 1.
- `BTT` shifts from index 3 to index 2.
- The List size decreases by one.

---

## How `remove()` Works

Suppose we have:


```python
shows = ["ABC", "XYZ", "KLM", "BTT"]
```

Memory

```text
0 → ABC
1 → XYZ
2 → KLM
3 → BTT
```

Now write:

```python
shows.remove("XYZ")
```

Python internally performs these steps:

### Step 1

Search for the value `"XYZ"`.

### Step 2

Find its position.

```text
0 → ABC
1 → XYZ
2 → KLM
3 → BTT
```

### Step 3

Delete `"XYZ"`.

```text
0 → ABC
1 → ____
2 → KLM
3 → BTT
```

### Step 4

Move all remaining items one position to the left.

```text
0 → ABC
1 → KLM
2 → BTT
```

---

## Example 1

```python
shows = ["ABC", "XYZ", "KLM"]

shows.remove("XYZ")

print(shows)
```

### Output

```text
['ABC', 'KLM']
```

---

## Example 2

```python
artists = ["Rajesh", "Amit", "Rahul"]

artists.remove("Amit")

print(artists)
```

### Output

```text
['Rajesh', 'Rahul']
```

---

## Production Example

```python
render_queue = [
    "SH010",
    "SH020",
    "SH030"
]

render_queue.remove("SH020")

print(render_queue)
```

### Output

```text
['SH010', 'SH030']
```

---

## `remove()` vs `insert()`

### insert()

```python
shows = ["ABC", "XYZ"]

shows.insert(1, "BTT")
```

### Output

```text
['ABC', 'BTT', 'XYZ']
```

A new item is added.

---

### remove()

```python
shows = ["ABC", "XYZ", "KLM"]

shows.remove("XYZ")
```

### Output

```text
['ABC', 'KLM']
```

An existing item is removed.

---

## Common Beginner Mistakes

### Using index instead of value

```python
shows.remove(1)
```

Many beginners think this removes index **1**.

Wrong.

It tries to remove the value **1**.

Correct

```python
shows.remove("XYZ")
```

---

### Removing an item that does not exist

```python
shows.remove("OTT")
```

Output

```text
ValueError: list.remove(x): x not in list
```

Always make sure the item exists before removing it.

---

## Important Points

- `remove()` removes an item by its value.
- It removes only the frist matching item.
- Remaining items shift one position to the left.
- List size decreases by one.
- IF the value does not exist, Python raises a `ValueError`.

---

## Summary

Use `remove()` when you know the value of the item that you want to delete from a List.

- `append()` -> Add at the end.
- `insert()` -> add at a specific index.
- `remove()` -> Remove by value.

