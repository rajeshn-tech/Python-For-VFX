# Day 01 Notes

## Topics

- print()
- Numbers
- Strings
- Variables
- Math Operators
- Resolution Example

---

## What is print()?

The `print()` function is used to display output on the screen.

### Example

```python
print("Hello World")
```

### Output

```
Hello World
```

---

## Numbers

Python can print numbers directly.

### Example

```python
print(10)
print(50)
print(100)
```

### Output

```
10
50
100
```

---

## Strings

Strings are text values.

Strings are written inside single quotes (' ') or double quotes (" ").

### Example

```python
print("Nuke")
print("Compositing")
print("SH001")
```

---

## Variables

A variable is used to store data.

### Syntax

```python
variable_name = value
```

### Example

```python
width = 1920

print(width)
```

### Output

```
1920
```

---

## Math Operators

Python supports basic mathematical operations.

| Operator | Description |
|----------|-------------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |

### Example

```python
print(10 + 5)
print(20 - 3)
print(5 * 6)
print(20 / 5)
```

---

## Resolution Example

In VFX, every shot has a resolution.

### Example

```python
width = 1920
height = 1080

print("Resolution :", width, "x", height)
```

### Output

```
Resolution : 1920 x 1080
```

---

## Production Note

Variables are heavily used in VFX pipelines to store:

- Project Name
- Sequence Name
- Shot Name
- Artist Name
- Width
- Height
- Version