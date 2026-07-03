# Day 04 - Decision Making

## Topics

- if Statement
- else Statement
- elif Statement

---

## Revision

### Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

#### Operators

- +
- -
- *
- /
- //
- %
- **

---

### Comparison Operators

Comparison operators are used to compare two values.

They always return:

- True
- False

#### Operators

- ==
- !=
- >
- <
- >=
- <=

---

### Logical Operators

Logical operators are used to combine multiple conditions.

#### Operators

- and
- or
- not

---

### Boolean Values

Python uses only two Boolean values.

- True
- False

These values are the foundation of decision making.

---

# Topic 1 - if Statement

## What is if?

The `if` statement is used to execute code only when a condition is **True**.

## Syntax

```python
if condition:
    # code
```

## Example

```python
width = 1920

if width == 1920:
    print("Valid Resolution")
```

## VFX Example

Suppose a render should start only when the resolution is **1920** pixels wide.

```python
width = 1920

if width == 1920:
    print("Render Allowed")
```

## Production Note

The `if` statement is commonly used in VFX pipelines for:

- Checking resolution
- Validating shot names
- Verifying file existence
- Checking render status

---

# Topic 2 - else Statement

## What is else?

The `else` statement executes when the `if` condition is **False**.

## Why do we use else?

Sometimes we want Python to perform another action when the condition is not satisfied.

## Syntax

```python
if condition:
    # Runs if the condition is True

else:
    # Runs if the condition is False
```

## Example

```python
width = 2048

if width == 1920:
    print("Valid Resolution")
else:
    print("Invalid Resolution")
```

## VFX Example

If a shot has the correct resolution, allow rendering.

Otherwise, stop the render and notify the artist.

## Production Note

The `else` statement is commonly used for:

- Invalid file paths
- Missing EXR files
- Permission denied
- Failed validations
- Render errors

---

# Topic 3 - elif Statement

## What is elif?

The `elif` statement is short for **else if**.

It is used to check another condition when the previous `if` condition is **False**.

## Why do we use elif?

Sometimes we need to check multiple conditions.

Instead of writing multiple `if` statements, we use `elif`.

## Syntax

```python
if condition1:
    # code

elif condition2:
    # code

else:
    # code
```

## Example

```python
width = 2048

if width == 1920:
    print("Full HD")

elif width == 2048:
    print("2K")

else:
    print("Unknown Resolution")
```

## VFX Example

A render tool checks the shot resolution.

- 1920 → Full HD
- 2048 → 2K
- 3840 → 4K
- Any other value → Invalid Resolution

## Production Note

The `elif` statement is commonly used for:

- Resolution validation
- Render status checks
- Version checks
- Shot status checks
- File format validation

# Topic 4 - Indentation

## What is Indentation?

Indentation means giving spaces at the beginning of a line.
In Python, Indentation defines which block of code belongs to a statement.

## Why is Indentation Important?

Unlike many programming languages, Python uses Indentation to Indentity code blocks.
without proper Indentation, Python will generate an error.

## Syntax

```python
if condition:
    print("Hello")
```

The `print()` statement is indented using four spaces.

## Correct Example

```python
width = 1920

if width == 1920:
    print("Valid Resolution")
```

## Incorrect Example

```python
width = 1920

if width == 1920:
    print("Valid Resolution")
```

Output

```text
IndentationError: expected an Indented block
```

## VFX Example

A render should start only when the resolution is valid.

```python
width = 1920

if width == 1920
    print("Render Started")
```

## Production Note

- Easy to read
- Easy to maintain
- Less error-prone
- Professional

## Topic 5 - Nested if

## What is Nested if?

A Nested `if` means writing one `if` statement inside another `if statement.

## Why do we use Nested if?

Sometimes one condition should be checked only after another is True.
In such cases, we use a Nested `if`

## Syntax 

```python
if condition1:

    if condition2:
        #code
```

## Example

```python
width = 1920
height = 1080

if width == 1920:

    if height == 1080:
        print("Valid Resolution")
```

## VFX Example

Before starting a render:

- Check width
- Then Check Height

If both are correct, start the render.

## Production Note

Nested `if` statement are commonly used for:

- Resolution Validation
- Artist approval
- File validation
- Publish valiation


# Topic 6 - and Operator 

## What is and?

The `and` operator is used to combine two or more conditions.

It return **True** only when **all conditions are True**.

## Why do we use and?

Sometimes a single condition is not enough.
We need multiple conditions to be True before executing the code.
In such cases, we use the `and` operator.

## Syntax

```python
if condition1 and condition2:
    # code
```

## Example

```python
width = 1920
height = 1080

if with == 1920 and height == 1080
    print("Valid Resolution")
```

## VFX Example 

A render should start only when:

- width is 1920
- Height is 1080

If both condition are True, start the render.

```python
width = 1920
height = 1080

if width == 1920 and height == 1080
    print("Render Started")
```

## Production Note

The `and` operators is commonly used for:

- Resolution validation
- shot validations
- Artist permission checks
- Publish validation
- Render approval

# Topic 7 - or Operator

## What is or?

The `or` operator is used to combine two or more conditions.
It return **True** if **at least one condition is True**.

## Why do we use or?

Something there are multiple valid options.
If any one condition is True, Python executes the code.
In such cases, we use the `or` operator.

## Syntax

```python
if condition1 or condition2:
    # Code
```

## Example

```python
width = 1920
height = 720

if width == 1920 or height == 1080:
    print("Valid Resolution")
```

## VFX Example

A render is allowed if:

- width is 1920
- or Height is 1080

If either condition is True, allow the render.

```python
width = 1920
height = 720

if width == 1920 or height == 1080:
    print("Render Started")
```

## Production Note

The `or` operator is commonly used for:

- Multiple file format validation
- Render status checks
- Version validation
- Artist permission check
- Multiple project validation

# Topic 8 - not Operator

## What is not?

The `not` operator is used to reverse a Boolean Value.

- True becomes False
- False becomes True

## Why do we use not?

Sometimes we want to execute code only when a condition is **not True*.
In such cases, we use the `not` operator.

## Syntax

```python
if not condition:
    # Code
```

## Example 

```python
render_completed = False

if not render_completed:
    print("Render Pending")
```
## VFX Example

A publish process should start only if the render is **not completed**.

```python
render_completed = False

if not render_completed:
    print("Start Rendering")
```

## Production Note

The `not` operator is commonly used for:

- File existence check
- Render status validation
- Artist permission checks
- Pipeline automation

# Mini project - Shot Validation Tool

## Objective

Build a simple Shot validation Tool using Day 4 concepts.

## User Input 

- Project Name
- Sequence
- Shot Number
- Width
- Height

## Validation Rule

- Width should be 1920
- Height should be 1080

If both conditions are correct:

```text
Shot Validation Passed
```

Otherwise:

```text
Shot Validation Failed
```

## Concepts Used

- if
- else
- and
- User Input
- Comparison Operators

## Production Note

Before rendering or publishing a shot, the pipeline validates important information such as:

- Resolution
- Shot Name
- Project Name
- Frame Range
- File Format

If any validation fails, the render or publish process is stopped automatically.
