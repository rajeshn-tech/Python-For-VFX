## Day 5 - Loops

Loops are used to execute the same block of code multiple times.
Instead of writing the same code repeatedly, we use loops to automate repetitive tasks.
Loops help us write clean, efficient, and maintainable programs.

--- 

## Topic 1 - Why Loops are Needed

## What is the Problem?

Sometimes we need to perform the same task many times.

For Example:

- Print frame numbers
- Rename hundreds of render frames
- process every node in a Nuke script

Writing the same code repeatedly is:

- Time-consuming
- Difficult to maintain
- More likely to contain mistakes

### Example Without Loops

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Imagine writing `print()` 10,000 times.
This is not practical.

---

## Solution

A **loop** repeats a block of code automatically.
Instead of writing the same code again and again, Python executes it repeatedly until the task is complete.

---

### Production Note

Loops are commonly used in VFX and animation pipeline for:

- Processing image sequences 
- Renaming files
- Validating assets
- Generating reports
- Checking render status

--- 

## Key Points

- A loop repeats code automatically.
- Loops reduce duplicate code.
- Loops make programs easier to maintain.
- Loops are essential in VFX pipeline automation.

# Topic 2 - Iteration

## What is Iteration?

An **Iteration** is one complete execution of a loop.
Each time the loop runs, it is called one Iteration.

---

## Example

```pyhton
for i in range(5):
    print(i)
```

Execution:

Iteration 1 → 0

Iteration 2 → 1

Iteration 3 → 2

Iteration 4 → 3

Iteration 5 → 4

Total Iterations = 5

---

## Real VFX Example

Suppose a render folder contains 5 image files.
During each iteration:

- Process one image
- Move to the next image
- Repeat until all images are processed

---

## Production Note

In VFX pipeline, one iteration usually process:

- one frame
- one image
- one file
- one node
- one shot

---

## Key Points

- One loop execution = one iterations.
- Total loop execution = Total iterations.
- Every loop is made up of one or more iterations.

# Topic 3 - For Loop

## What is a for loop?

A **for loop** is used to repeat a block of code for a fixed number of iterations.
It is commonly used when we know how many times the code should run.

---

## Syntax

```pyhton
for varriable in sequence:
    # code
```

---

## Real VFX Example

A render folder contains 100 frame.
A for loop can process every frame one by one automatically.

---

## Key Points

- Used for fixed iteration.
- Executes code repeatedly.
- Commonly used with `range()`.

# Topic 4 - range()

## What is range()?

`range()` is a built-in Python function that generates a sequence of numbers.
It is commonly used with a `for` loop

---

## Syntax

```python
range(stop)
```

The sequence starts from **0** and stops **before** the stop value.

---

## Example

```python
for i in range(5):
    print(i)
```

Output:
0
1
2
3
4

---

## Key Points 

- Starts from 0 by default.
- Stop value is not included.
- Commonly used with for loops.

# Topic 5 - range(start, stop)

## What is range(start, stop)

`range(start, stop)` is a built-in Python function that generates a sequence of numbers starting from the **start** value and stoping **before** the **stop** value.

Unlike `range(stop)`, we can choose where the sequence should begin.

--- 

## Syntax

```python
range(start, stop)
```
### Parameters

- **start** -> Starting value of sequence.
- **stop**  -> Ending value of the sequence (not included)

---

## Example

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

The value **6** is not included.

---

## How range(start, stop) Works

```text
range(1, 6)

Start = 1
Stop = 6

Sequence

1
2
3
4
5
```

## Real VFX Example

Suppose a shot contains frames from **1001** to **1010**.

```python
for frame in range(1001, 1011):
```

Output

```text
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
```

---

## Production Note

`range(start, stop)` is commonly used for:

- processing frame range
- Batch rendering
- Exporting image sequence
- Iterating theough shot number

---

## Key Points

- You choose the starting number.
- The stop value is not included.
- Mostly used with `for` loops.

# Topic 6 - range(start, stop, step)

## What is range(start, stop, step)?

`range(start, stop, step)` is a built-in Python function that generates a sequence of number with a specific step size.
Unlike `range(start, stop, step)`, we can control how much the value increases after each iteration.

---

## Syntax

```python
range(start, stop, step)
```

### Parameters

- **start** -> starting of the sequence.
- **stop**  -> Ending value of the sequence (not included).
- **step**  -> Amount by which the value increases after each iteration.

---

## Example

```python
for i in range(1, 10, 2):
    print(i)
```

### Output

```text
1
3
5
7
9
```
## How range(start, stop, step) works

```text
range(1, 10, 2)

start = 1
stop  = 10
step  = 2

Sequence

1
3
5
7
9
```

The value **10** is not included.

---

### Real VFX Example

Suppose you want to process every 2nd frame.

```python
for frame in range(1001, 1011, 2):
print(frame)

```

Output

```text
1001
1003
1005
1007
1009
```
## Production Note

`range(start, stop, step)` is commonly used for:

- Processing every 2nd frame
- Processing every 5th frame
- Creating preview renders
- Sampling image sequence

---

## Key Points

- You choose the starting value.
- The stop value is not included.
- The step value decides how much the number increases.
- Mostly used with `for` loops.

## Topic 7 - Loop Execution Flow

## What is Loop Execution Flow?

Loop Execution Flow means the order in which Python executes a loop.
Python follows a fixed sequence while running a loop.
Understanding the execution flow helps you predict the output and debug programs easily.

---

## Execution Flow of a for Loop

Example:

```python
for i in range(3):
    print(i)

print("Loop Finished")
```

### Step-by-Step Execution

### Step 1

Python exeution:

```python
range(3)
```

It creates the sequence:

```text
0
1
2
```

---

### Step 2

Python starts the loop.

First value:

```python
i = 0
```

Execute:

```python
print(i)
```

Output

```text
0
```

---

### Step 3

Next value:

```python
i = 1
```

```text
1
```

---

### Step 4

Next value:

```python
i = 2
```

Output

```text
2
```

---

### Step 5

No more values are available.
The loop ends.

Python executes the next statement.

```python
print("Loop Finished")
```

Output

```text
Loop Finished
```

---

## Execution Flow Diagram

```text
Start
   │
   ▼
range(3)
   │
   ▼
0 1 2
   │
   ▼
i = 0
print(0)
   │
   ▼
i = 1
print(1)
   │
   ▼
i = 2
print(2)
   │
   ▼
More values available?

Yes -> Continue

No -> Exit Loop
   │
   ▼
print("Loop Finished")
   │
   ▼
End
```
---

Start
   │
   ▼
Get the next value from the sequence
   │
   ▼
Assign the value to the loop variable
   │
   ▼
Execute the loop body
   │
   ▼
More values available?
   │            │
  Yes          No
   │            │
   ▼            ▼
Repeat      Exit the Loop
   │
   ▼
Execute the next statement after the loop


---

## Production Note

Understanding execution flow is important for:

- Debugging loops
- Reading production code
- Writing efficient pipeline tools
- Finding logical mistakes

---

## Key Points

- Python executes loops one iteration at a time.
- The loop ends when no values are left.
- After the loop finishes, Python executes the next statement.

### Remember

> **only the indented code inside the loop is repeated.**
>
> **Any statement written outside the loop executes only once after the loop finishes.**


# Topic 8 - Common Beginner Mistake

While learning loops, beginners often make some common mistake.
Understanding these mistake will help you write correct programs and debug errors quickly.

---

### Mistake 1 - Forgetting the Colon (:)

Incorrect

```python
for i in range(5)
    print(i)
```

Correct

```python
for i in range(5):
    print(i)
```
---

## Mistake 2 - Incorrect Indentation

```python
for i in range(5):
print(i)
```
Correct

```python
for i in range(5):
    print(i)
```

Python uses indentation to identify the code that belongs to the loop.

---

## Mistake 3 - Expecting the stop value to be Included

Example

```python
for i in range(1, 5):
    print(i)
```

Output

```text
1
2
3
4
```

The stop value (5) is **not included**.

---

## Mistake 4 - Using the wrong step value

Example

```python
for i in range(1, 10, 2):
    print(i)
```

Output

```text
1
3
5
7
9
```

The value increases by **2** after every iteration.

---

## Mistake 5 - Writing code Outside the Loop by Accident

Incorrect

```python
for i in range(3):
    print(i)

print("Done")
```

If you expected `"Done"` to print every iteration, this code is incorrect because it is outside the loop.


```python
for i in range(3):
    print(i)
    print("Done")
```

---

## PRoduction Tips

- Always check the indentation.
- Remember that the stop value is not included.
- Read the code line by line.
- Mentally execute the loop before running the program.

---

## Key Points

- Small mistakes can completely change the output.
- Proper indentation is very important.
- Practice predicting the output before executing the code.


# Topic 9 - While Loop

## What is a while Loop?

a `while` loop repeatedly executes a block of code **as long a condition is true**.

Unlike a `for` loop, a `while` loop does not know in advance how many times it will run.

The loop stops only when the condition becomes `False`.

---
# Syntax

```python
while condition:
    # code
```
---

### How a while Loop Works

1. Python checks the condition. 
2. If the condition is `True`, the code inside the loop is executed.
3. Python checks the condition again.
4. The loop continus until the condition become `False`.
5. After the loop ends, Python executes the next statement.

---

### Example

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

### Output
```text
1
2
3
4
5
```

---

## Real VFX Example

Suppose a render is running.
Keep checking until all frames are renderd.

```python
render_complete = False

while render_complete == False:
    print("Rendering...")
```

(In a real production script, `render_complete` will eventually `True`.)

---

## Production Note

A `while` loop is commonly used for:

- waiting for a render to finish
- Monitoring file generation
- Watching folders for new files
- Runnung background pipeline tool

---

## Key Points

- A `while` loop depents on a condition.
- It runs while the condition is `True`.
- It stop when the condition is `False`.
- Be careful to avoid infinite loops.

## Execution Flow

Start
   │
   ▼
count = 1
   │
   ▼
Condition True?
   │
 ┌─┴─────┐
 │ Yes   │
 ▼       │
Execute Loop Body
 │
 ▼
Update count
 │
 └──────────────► Check Condition Again
         │
         ▼
      False
         │
         ▼
     Exit Loop


# Topic 10 - Infinite Loop

## What is an Infinite Loop?

An Infinite Loop is a loop that never stops executing.
It keeps running because its condition always remains`True`.

---

## Why Does an Infinite Loop Happen?

An infinite loop usally happens when the loop condition never becomes `False`.

This often occurs the loop variable is not updated correctly.

---

# Example

```python
count = 1

while count <= 5:
    print(count)
```

### What Happens?

- `count` is always `1`.
- The condition `count <= 5` is always `True`.
- The loop never ends.

count = 1
      │
      ▼
Condition True?
      │
      ▼
Print 1
      │
      ▼
Variable Updated?

❌ No
      │
      ▼
Condition True Again
      │
      ▼
Print 1
      │
      ▼
Repeat Forever...

---

## Correct Example

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

count = 1
↓
Print 1
↓
count = 2
↓
Print 2
↓
count = 3
↓
Print 3
↓
count = 4
↓
Print 4
↓
count = 5
↓
Print 5
↓
count = 6
↓
Condition False
↓
Loop End


### Output

```text
1
2
3
4
5
```

The loop stops because the condition eventually becomes `False`.

---

### Real VFX Example

Suppose a pipeline tool keeps checking whether a render has finished.

```python
render_complete = False

while render_complete == False:
    print("Waiting for render")
```

If `render_complete` is never changed to `True`, the loop will run forever.

---

## Production Tips

- Always make sure the loop condition can become `False`.
- Update the loop variable correctlty.
- Test your loop with small values.
- Be careful when writing `while` loops.

---

## Key Points

- An infinite loop never ends.
- It usually happens becuase the condition never becomes `Fales`
- Always update the loop variable inside the loop.

## How to Identify an Infinite Loop

Ask yourself these two questions:

1. It the loop variable being updated?
2. Can the condition eventually become False?

If the answer is **Yes**, it is a normal loop.
If the answer is **No**, it may become an infinite loop.

# Topic 11 - break Statement

## What is break?

The `break` statement is used to stop a loop immediately.

When Python execute `brek`, it exits the loop without checking the remaining iterations.

---

## Why do we use break?

Sometimes we do not want the loop to run until the condition becomes `False`.

We may find what we are looking for before the loop finishes.

In such cases, we use `break`.

---

## Syntax

```python
for variable in sequence:
    if condition:
        break
```

or

```python
while condition:
    if condition:
    break
```

---

## Example

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

Execution Flow

Start
   │
   ▼
i = 1
   │
   ▼
i == 3 ?
   │
False
   │
Print 1
   │
   ▼
i = 2
   │
False
   │
Print 2
   │
   ▼
i = 3
   │
True
   │
break
   │
   ▼
Loop End


## Output

```text
1
2
```

---

# Real VFX Example

Suppose we are checking render frames.

If a corrupted frame is found, stop checking immediately.

```python
for frame in range(1001, 1011):

    if frame == 1005:
        break

    print(frame)
```

Output

```text
1001
1002
1003
```

---

## Production Note

The `brek` statement is commonly used for:

- Stop searching after finding a file.
- Stop checking render frames after an error.
- Exit a menu when the user choose Exit.
- Stop reading data after the required result is found.

---

## Key Points

- `break` immediately exit the loop.
- The remaining iterations are skipped.
- Python continues executing the code after the loop.

## Remember

**Printing and Iteration are different concepts.**

- An iteration starts when the loop variable gets a new value.
- Even if `break` stops the loop before `print()`, that iteration has already started.


# Topic 12 - Continue Statement

## What is continue?

The `continue` statement is used to skip the current iteration and move to the next iteration of the loop.

Unlike `break`, the `continue` statement does not stop the loop.

It only skip the remaining code of the current iteration.

---

## Why do we use continue?

Sometimes we want to ignore a particular value but continue processing the remaining values.

In such cases, we use `continue`.

---

## Syntax 

```python
for variable in sequence:
    if condition:
        continue

    # remaining code
```

## Example

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

### Output

```text
1
2
4
5
```

---

## Real VFX Example

Suppose frame **1005** is corrupted.

Skip it and continue rendering the remining frames.

```python
for frame in range(1001, 1006):
    
    if frame == 1003:
        continue

    print(frame)
```

### Output

```text
1001
1002
1003
1004
```
---

## Production Note

The `continue` statement is commonly used for:

- Skip corrupted files.
- Ignore missing frames
- Continue processing remaining files

---

## Key Points

- `continue` skip only the current iteration.
- The loop does not stop.
- The next iteration starts immediately.



## Topic 13 - pass Statement

## What is pass?

The `pass` statement is a placeholder.

It tells Python:

> "Do nothing for now."

Python does not produce an error and simply moves to the statement.

---

## Why do we use pass?

Sometimes we know that we will write code later, but we are not ready yet.

Instead of leaving the block empty, we use `pass`.

---

## Syntax

```python
if condition:
    pass
```

or

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

---

## Example

```python
for i in range(1, 6):

    if i == 3:
        pass
    print(i)
```

### Output

```text
1
2
3
4
5
```

Notice that `pass` does not stop or skip the loop.

---

## Difference


| Statement | Meaning                |
|-----------|------------------------|
| break     | Stop the Loop          |
| continue  | Skip current iteration |
| pass      | Do nothing             |
|-----------|------------------------|

---

## Real VFX Example

Suppose you are creating a pipeline tool.

You have not written the render validation code yet.

```python
if render_failed:
    pass
```

You can come back later and complete the logic.

---

## Production Note

The `pass` statement is commonly used for:

- Temporary code blocks
- Future feature
- Pipeline development
- Code planning

---

## Key Points

- `pass` does nothing.
- It prevents syntax errors.
- It is used as a placeholder.
- The program continue normally.


**pass**

-> Does nothing.
-> Acts as a placeholder.


**continue**

-> Skip the current iteration.
-> Moves to the next iteration.

---------------------------------------------------------------|
Statement | Loop Stop? | Current Iteration Skip | does Nothing |
----------|------------|------------------------|--------------|
break     |  Yes       |  No                    | No           |
----------|------------|------------------------|--------------|
continue  | No         |  Yes                   | No           |
----------|------------|------------------------|--------------|
pass      | No         |  No                    | Yes          |
---------------------------------------------------------------|


# Day 05 - Topic 14
# Nested Loops (Basic)

---

# What is a Nested Loop?

A loop written inside another loop is called a **Nested Loop**.

### Example

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

Here,

**Outer Loop**

```python
for i in range(2):
```

Inside it,

**Inner Loop**

```python
for j in range(3):
```

---

# Rule of Nested Loops

For every **ONE** iteration of the **Outer Loop**,

the **Inner Loop** runs completely.

Only after the **Inner Loop** finishes,

the **Outer Loop** moves to its next iteration.

---

# Execution Order

```text
Start
   ↓
Outer Loop Starts
   ↓
Inner Loop Starts
   ↓
Inner Loop Finishes
   ↓
Outer Loop Moves to Next Iteration
   ↓
Inner Loop Starts Again
   ↓
Repeat Until Outer Loop Ends
   ↓
Program Ends
```

---

# Memory

Python creates two variables.

- `i` stores the current value of the **Outer Loop**.
- `j` stores the current value of the **Inner Loop**.

### Example

```text
i = 0
j = 0
```

Later,

```text
i = 0
j = 1
```

Later,

```text
i = 0
j = 2
```

After the **Inner Loop** finishes,

```text
i = 1
```

Then the **Inner Loop** starts again from the beginning.

---

# Important Rule

- The **Outer Loop** changes slowly.
- The **Inner Loop** changes quickly.
- The **Inner Loop** always finishes before the **Outer Loop** moves to its next value.

> **Remember this rule forever.**

---

# Example 1

```python
for i in range(2):
    print(i)
```

## Output

```text
0
1
```

There is only **one loop** in this example.

---

# Example 2

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

## Output

```text
0 0
0 1
0 2
1 0
1 1
1 2
```

---

# Nested Loop Structure

```text
Outer Loop
    ↓
for i in range(2)

    ↓

Inner Loop
for j in range(3)
```

---

# Memory Visualization

### Step 1 - Python Creates Variables

```text
i = ?
j = ?
```

---

### Step 2 - Outer Loop Starts

```text
i = 0
```

---

### Step 3 - Inner Loop Starts

```text
i = 0
j = 0
```

Output

```text
0 0
```

---

### Step 4 - Next Iteration

```text
i = 0
j = 1
```

Output

```text
0 1
```

---

### Step 5 - Next Iteration

```text
i = 0
j = 2
```

Output

```text
0 2
```

---

### Step 6 - Inner Loop Finishes

Current Memory

```text
i = 0
```

The **Inner Loop** has completed,

but the **Outer Loop** still has another value.

So Python updates:

```text
i = 1
```

---

### Step 7 - Inner Loop Starts Again

```text
i = 1
j = 0
```

Output

```text
1 0
```

---

### Step 8 - Next Iteration

```text
i = 1
j = 1
```

Output

```text
1 1
```

---

### Step 9 - Final Iteration

```text
i = 1
j = 2
```

Output

```text
1 2
```

# Simple Example 

i = 0
    j = 0  → print(0,0)
    j = 1  → print(0,1)
    j = 2  → print(0,2)

i = 1
    j = 0  → print(1,0)
    j = 1  → print(1,1)
    j = 2  → print(1,2)


---

# Iteration Table

|-----------------------|
| Step | i | j | Output |
|------|---|---|--------|
| 1    | 0 | 0 | 0 0    |
|------|---|---|--------|
| 2    | 0 | 1 | 0 1    |
|------|---|---|--------|
| 3    | 0 | 2 | 0 2    |
|------|---|---|--------|
| 4    | 1 | 0 | 1 0    |
|------|---|---|--------|
| 5    | 1 | 1 | 1 1    |
|------|---|---|--------|
| 6    | 1 | 2 | 1 2    |
|-----------------------|

---

# Key Points

- A **Nested Loop** is a loop inside another loop.
- The **Outer Loop** runs first.
- The **Inner Loop** runs completely for every iteration of the **Outer Loop**.
- The **Outer Loop** changes slowly.
- The **Inner Loop** changes quickly.
- Python repeats the **Inner Loop** from the beginning every time the **Outer Loop** gets a new value.
- Understanding Nested Loops is essential for working with matrices, tables, grids, and VFX production tasks.


# Topic 15 Real VFX Production Examples

# Why are Loops Important in VFX?

Loop are one of the most important concepts in the VFX industry.

Instead of repeating the same task manually, a loop performs the task automatically.

This saves time, reduces manual work, and minimizes huamn errors.

---

# Example 1 Rendering Frames

Suppose a shot contains frame from **1001 to 1005**.

```python
for frame in range(1001, 1006):
    print(f"Rendering Frame {frame}")
```

## Output

```text
Rendering Frame 1001
Rendering Frame 1002
Rendering Frame 1003
Rendering Frame 1004
Rendering Frame 1005
```

### How Python Executes

```text
frame = 1001
↓
Rendering Frame 1001

↓

frame = 1002
↓
Rendering Frame 1002

↓

frame = 1003
↓
Rendering Frame 1003

↓

frame = 1004
↓
Rendering Frame 1004

↓

frame = 1005
↓
Rendering Frame 1005
```

## Production Example

A Render farm renders one frame at a time until all frames are completed.

---

# Example 2 - Publishing Shot

Suppose a project contains three shots.

```python
for shot in range(1, 4):
    print(f"Publishing Shot {shot}")
```

## Output

```text
Publishing Shot 1
Publishing Shot 2
Publishing Shot 3
```

### How Python Executes

```text
shot = 1
↓

Publishing Shot 1

↓

shot = 2
↓

Publishing Shot 2

↓

shot = 3
↓

Publishing Shot 3
```

### Production Example

A Pipeline Tool can automatically publish every approved shot one by one.

---

# Example 3  - Render Progress

```python
for progress in range(0, 101, 25):
    print(f"Progress : {progress}%")
```

## Output

```text
Progress : 0%
Progress : 25%
Progress : 50%
Progress : 75%
Progress : 100%
```

### How Python Executes

```text
progress = 0

↓

progress = 25

↓

progress = 50

↓

progress = 75

↓

progress = 100
```

### Production Example 

Most render software displays render progress while rendering frames.

---

# Where Are Loops used in VFX?

Loops are commonly used for:

- Rendering Frames
- Publishing Shots
- Processing Image Sequences
- Creating Cache Files
- Rendering Layers
- Reading Excel Files
- Processing CSV Files
- Renaming Files
- Batch Processing
- Folder Automation
- Maya Automation
- Blender Automation
- Houdini Automation
- Render Farm Pipelines

---

# Key Points

- Loops automate repetitive task.
- Loops save time.
- Loops reduce manual work.
- Loops reduce human errors.
- A Pipeline TD uses loops almost every day.
- The loop logic remains the same; only the data changes.

---

# Summary

In this topic, we did **not** learn a new Python concept.

Instead, we learned how the **for loop** is used in real vfx production.

The same loop that prints numbers can also:

- Render Frames
- Publish Shots
- SHow Render Progress
- Process Files
- Automate Production Tasks

Understanding loops is one of the first steps toward becoming a Pipelinr TD or VFX Tools Developer.

# Topic 16 - Practice Questions

---

# Objective

In this topic, we will practice all the concepts learned in **Day 05**.

This topic does **not** introduce any new Python concepts.

The goal is to improve:

- Logical Thinking
- Code Writing
- Code Reading
- Problem Solving
- Debugging Skills

---

# Concepts Used

The following concepts will be used throughout this topic:

- `for` Loop
- `while` Loop
- `range()`
- `range(start, stop)`
- `range(start, stop, step)`
- `break`
- `continue`
- `pass`
- Nested Loops

---

# Why is Practice Important?

Reading code helps you understand Python.

Writing code helps you remember Python.

Practicing code helps you solve real-world problems.

The more you practice, the more confident you become.

---

# Programming Rule

The best programmers are not the ones who know the most syntax.

The best programmers are the ones who solve problems.

Practice builds confidence.

Confidence builds experience.

Experience builds better programmers.

---

# Production Note

In VFX production, developers solve small problems every day.

For example:

- Rendering Frames
- Publishing Shots
- Processing Image Sequences
- Renaming Files
- Batch Processing
- Creating Reports

All these tasks use the same Python concepts that you learned in **Day 05**.

---

# Key Points

- Practice improves coding speed.
- Practice improves logical thinking.
- Practice helps in debugging.
- Practice builds confidence.
- Every good programmer practices regularly.

---

# Summary

This topic focuses only on practice.

No new concepts are introduced.

The objective is to become comfortable writing loops without looking at notes.


# Topic 17 - Output Prediction Exercise

---

# Objective

In this topic, we will improve our ability to predict the output of Python programs without running the code.

This topic does **not** introduce any new Python concepts.

The main goal is to strengthen logical thinking and understand how Python executes code internally.

---

# Why is Output Prediction Important?

Before running a program, a good programmer should be able to predict what the output will be.

Output prediction helps you understanding the execution flow of a program.

It also improves your debugging and problem-solving skills.

---

# Concepts Used

The following concepts wil be used throughout this topic:

- `for` Loop
- `while` Loop
- `range()`
- `range(start, stop)`
- `range(start, stop, step)`
- `break`
- `countinue`
- `pass`
- Nested Loops

---

# Output Prediction Strategy

Whenever you see a Python program, follow these steps:

1. Read the code carefully.
2. Understand the loop.
3. Track the variable values.
4. Predict the output.
5. Run the program.
6. Compare the actule output with your prediction.
7. Find and understand any mistakes.

---

# Programming Rule

Never guess the output.

Always execute the program mentally.

Follow the execution one line at a time.

---

# Production Note

Professional developers spend more time reading code than writing code.

Being able to understand existing code is an essential programming skill.

Output prediction improves code reading, debugging, and logical thinking.

---

# Key Points

- Read the code carefully.
- Think before running the program.
- Track variable values mentally.
- Follow the execution step by step.
- Practice regularly.

---

# Summary

This topic focuses on understanding how Python executes code internally.
The better you become at predicting output, the easier it becomes to debug and understand production code.


# Topic 18 - Mini Project

---

# Project Name

Render Queue Simulator

----
# Objective

The objective of this mini project is to simulate how a render farm process multiple shots and their frames.

The project combines all the loop concepts learned in Day 05.

---

# Concets Used

- `for` Loop
- Nested Loop
- `range()`
- `f-string`

---

# Project Flow

Start Render Queue

↓

Select Shot

↓

Render All Frames

↓

Move to Next Shot

↓

Render Complete

---

# Production Note

In a real VFX production pipeline, render farms process thousands of frames automatically.

Instead of manually rendering every frame, Python loops automate the entire process.

This mini project demonstrates the basic idea behind render automation.

---

# Key Points

- One shot contains multiple frames.
- The outer loop process shots.
- The inner loop process frames.
- Nested loops are commonly used in production pipelines.

---

# Summary

This project combines the concepts learned in Day 05 into a simple production-style example.


# Topic 19 - Homework

---

# Objective

The objective is this homework is to strengthen your understanding of loops through independent practice.

The questions are based only on the concepts learned in **Day 05**.

No new Python concepts are introduced.

---

# Concepts Used

The following concepts may be used:

- `for` Loop
- `while` Loop
- `range()`
- `range(start, stop)`
- `range(start, stop, step)`
- `break`
- `continue`
- `pass`
- Nested Loops

---

# Homework Rules

- Solve every question without looking at the notes.
- Think before writing the code.
- Predict the output before running the program.
- Fix your own errors before asking for help.
- Write clean and properly formatted code.

---

# Production Note

In real VFX production, developers solve similar problems every day.

The purpose of this homework is to improve your logical thinking and coding confidence.

---

# Key Points

- Write the code yourself.
- Read the error messages carefully.
- Practice regularly.
- Focus on understanding the logic.

---

# Summary

This homework is designed to help you become more confidence with loops and prepare you for the next topics in Python.

