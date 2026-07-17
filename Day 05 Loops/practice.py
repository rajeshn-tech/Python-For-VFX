"""
=========================================================
Python for VFX
Day 05 - Loops
Practice File (Part 1)

Topics Covered:
1. Why Loops are Needed
2. Iteration
3. for Loop
4. range()
5. range(start, stop)
6. range(start, stop, step)
7. Loop Execution Flow
8. Common Beginner Mistakes

Author : Rajesh Navsagar
=========================================================
"""

# =========================================================
# Topic 1 - Why Loops are Needed
# =========================================================

print("========== Topic 1 ==========")

print("Frame 1")
print("Frame 2")
print("Frame 3")
print("Frame 4")
print("Frame 5")

print()

print("Imagine writing 10,000 print() statements.")
print("Loops solve this problem.")

print("\n")


# =========================================================
# Topic 2 - Iteration
# =========================================================

print("========== Topic 2 ==========")

for i in range(5):
    print(i)

print("\n")


# =========================================================
# Topic 3 - for Loop
# =========================================================

print("========== Topic 3 ==========")

for i in range(3):
    print("Hello")

print("\n")


# =========================================================
# Topic 4 - range()
# =========================================================

print("========== Topic 4 ==========")

# Example 1
for i in range(5):
    print(i)

print()

# Example 2
for number in range(8):
    print(number)

print()

# Example 3
for value in range(3):
    print(value)

print("Loop Finished")

print("\n")


# =========================================================
# Topic 5 - range(start, stop)
# =========================================================

print("========== Topic 5 ==========")

for i in range(1, 6):
    print(i)

print("Loop Finished")

print("\n")


# =========================================================
# Topic 6 - range(start, stop, step)
# =========================================================

print("========== Topic 6 ==========")

for i in range(1, 10, 2):
    print(i)

print("Loop Finished")

print("\n")


# =========================================================
# Topic 7 - Loop Execution Flow
# =========================================================

print("========== Topic 7 ==========")

for i in range(3):
    print("Iteration Start")
    print(i)
    print("Iteration End")
    print()

print("Loop Finished")

print("\n")


# =========================================================
# Topic 8 - Common Beginner Mistakes
# =========================================================

print("========== Topic 8 ==========")

for i in range(3):
    print(i)
    print("Inside Loop")

print("Outside Loop")

print("\n")


# =========================================================
# Topic 9 - while Loop
# =========================================================

print("========== Topic 9 ==========")

count = 1

while count <= 3:
    print(count)
    count = count + 1

print("Loop Finished")

print()

count = 2

while count <= 4:
    print(count)
    count = count + 1

print("Done")

print("\n")


# =========================================================
# Topic 10 - Infinite Loop
# =========================================================

print("========== Topic 10 ==========")

# WARNING:
# Do NOT run this code.
# It creates an Infinite Loop because 'count'
# is never updated.

"""
count = 1

while count <= 2:
    print(count)
"""

print("Infinite Loop example is commented to avoid accidental execution.")

print("\n")


# =========================================================
# Topic 11 - break
# =========================================================

print("========== Topic 11 ==========")

# Example 1

for i in range(1, 6):

    if i == 4:
        break

    print(i)

print("Loop Finished")

print()

# Example 2

for i in range(1, 8):

    if i == 5:
        break

    print(i)

print("Done")

print("\n")


# =========================================================
# Topic 12 - continue
# =========================================================

print("========== Topic 12 ==========")

# Example 1

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

print("Loop Finished")

print()

# Example 2

for i in range(1, 7):

    if i == 4:
        continue

    print(i)

print("Done")

print("\n")


# =========================================================
# Topic 13 - pass
# =========================================================

print("========== Topic 13 ==========")

# Example 1

for i in range(1, 6):

    if i == 3:
        pass

    print(i)

print("Loop Finished")

print()

# Example 2

for i in range(1, 5):

    if i == 2:
        pass

    print(i)

print("Done")

print("\n")

# =========================================================
# Topic 14 - Nested Loops (Basic)
#
# Purpose:
# Learn how Nested Loops work internally.
#
# Topics Covered:
# 1. Basic Nested Loop
# 2. Understanding Outer & Inner Loop
# 3. Execution Order
# 4. Loop Variables
# 5. Indentation
# =========================================================

print("========== Topic 14 ==========")

# Example 1

for i in range(2):
    for j in range(3):
        print(i, j)

print()

# Example 2

for i in range(3):
    for j in range(2):
        print(i, j)

print()

# Example 3

for i in range(2):
    print(f"Outer Start : {i}")

    for j in range(3):
        print(f"    Inner : {j}")

    print(f"Outer End : {i}")

print()

# Example 4

for i in range(2):
    for j in range(2):
        print(i, j)

print()

# Example 5

for shot in range(1, 3):
    for frame in range(1001, 1004):
        print(f"Shot {shot} -> Frame {frame}")

print()

# Example 6

for sequence in range(1, 3):
    for shot in range(1, 4):
        print(f"Sequence {sequence} -> Shot {shot}")

print()

# Example 7

for shot in range(1, 3):
    for layer in ["Beauty", "Shadow", "AO"]:
        print(f"Shot {shot} -> {layer}")

print()

# Example 8

for asset in range(1, 4):
    for version in range(1, 3):
        print(f"Asset {asset} -> Cache V{version}")

print()

# Example 9

for project in ["Project_A", "Project_B"]:
    for shot in ["Shot001", "Shot002", "Shot003"]:
        print(project, shot)

print()

# Example 10

for department in ["Model", "Rig", "Animation"]:
    for artist in ["Raj", "Amit"]:
        print(f"{department} -> {artist}")

print("\n")


# =========================================================
# Topic 15 - Real VFX Production Examples
# =========================================================

print("========== Topic 15 ==========")

# Example 1 - Rendering Frames

for frame in range(1001, 1006):
    print(f"Rendering Frame {frame}")

print()

# Example 2 - Publishing Shots

for shot in range(1, 4):
    print(f"Publishing Shot {shot}")

print()

# Example 3 - Render Progress

for progress in range(0, 101, 25):
    print(f"Progress : {progress}%")

print()

print("Topic 15 Completed")

print("\n")

# =========================================================
# Topic 16 - Practice Questions (Solutions)
# =========================================================

print("========== Topic 16 ==========\n")

# =========================================================
# Question 1
# Print numbers from 1 to 10.
# =========================================================

for i in range(1, 11):
    print(i)

print()


# =========================================================
# Question 2
# Print numbers from 10 to 1 in reverse order.
# =========================================================

for i in range(10, 0, -1):
    print(i)

print()


# =========================================================
# Question 3
# Print only even numbers from 2 to 20.
# =========================================================

for i in range(2, 21, 2):
    print(i)

print()


# =========================================================
# Question 4
# Print only odd numbers from 1 to 19.
# =========================================================

for i in range(1, 20, 2):
    print(i)

print()


# =========================================================
# Question 5
# Print:
#
# Frame 1001
# Frame 1002
# Frame 1003
# Frame 1004
# Frame 1005
# =========================================================

for frame in range(1001, 1006):
    print(f"Frame {frame}")

print()


# =========================================================
# Question 6
# Print:
#
# Publishing Shot 1
# Publishing Shot 2
# Publishing Shot 3
# =========================================================

for shot in range(1, 4):
    print(f"Publishing Shot {shot}")

print()


# =========================================================
# Question 7
# Print:
#
# Progress : 0%
# Progress : 20%
# Progress : 40%
# Progress : 60%
# Progress : 80%
# Progress : 100%
# =========================================================

for progress in range(0, 101, 20):
    print(f"Progress : {progress}%")

print()


# =========================================================
# Question 8
# Print using Nested Loop:
#
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# =========================================================

for i in range(2):
    for j in range(3):
        print(i, j)

print()


# =========================================================
# Question 9
# Print:
#
# Sequence 1
#     Shot 1
#     Shot 2
#
# Sequence 2
#     Shot 1
#     Shot 2
# =========================================================

for sequence in range(1, 3):
    print(f"Sequence {sequence}")

    for shot in range(1, 3):
        print(f"    Shot {shot}")

print()


# =========================================================
# Question 10
# Print:
#
# Shot 1
#     Frame 1001
#     Frame 1002
#     Frame 1003
#
# Shot 2
#     Frame 1001
#     Frame 1002
#     Frame 1003
# =========================================================

for shot in range(1, 3):
    print(f"Shot {shot}")

    for frame in range(1001, 1004):
        print(f"    Frame {frame}")

print()


# =========================================================
# Question 11
# Print:
#
# Cache Version 1
# Cache Version 2
# Cache Version 3
# Cache Version 4
# Cache Version 5
# =========================================================

for version in range(1, 6):
    print(f"Cache Version {version}")

print()


# =========================================================
# Question 12
# Create a list:
#
# ["Beauty", "Shadow", "AO", "Depth"]
#
# Print every render layer using a loop.
# =========================================================

layers = ["Beauty", "Shadow", "AO", "Depth"]

for layer in layers:
    print(layer)

print()


# =========================================================
# Question 13
# Create two lists.
#
# Departments:
# Animation
# Lighting
#
# Artists:
# Raj
# Amit
#
# Output:
#
# Animation -> Raj
# Animation -> Amit
# Lighting -> Raj
# Lighting -> Amit
# =========================================================

departments = ["Animation", "Lighting"]
artists = ["Raj", "Amit"]

for department in departments:
    for artist in artists:
        print(f"{department} -> {artist}")

print()


# =========================================================
# Question 14
# Print numbers from 50 to 100
# with a gap of 10.
# =========================================================

for number in range(50, 101, 10):
    print(number)

print()


# =========================================================
# Question 15
# Print:
#
# Project_A
#     Shot001
#     Shot002
#
# Project_B
#     Shot001
#     Shot002
# =========================================================

projects = ["Project_A", "Project_B"]
shots = ["Shot001", "Shot002"]

for project in projects:
    print(project)

    for shot in shots:
        print(f"    {shot}")

    print()

print("========== Topic 16 Completed ==========")


# =========================================================
# Topic 17 - Output Prediction Exercises
# =========================================================

print("========== Topic 17 ==========\n")

# =========================================================
# Question 1
# Predict the output.
# =========================================================

for i in range(5):
    print(i)

print()


# =========================================================
# Question 2
# =========================================================

for i in range(1, 6):
    print(i)

print()


# =========================================================
# Question 3
# =========================================================

for i in range(2, 11, 2):
    print(i)

print()


# =========================================================
# Question 4
# =========================================================

for i in range(10, 2, -2):
    print(i)

print()


# =========================================================
# Question 5
# =========================================================

for i in range(3):
    print("Python")

print()


# =========================================================
# Question 6
# =========================================================

for i in range(2):
    print(i)
    print("Hello")

print()


# =========================================================
# Question 7
# =========================================================

for i in range(2):
    for j in range(2):
        print(i, j)

print()


# =========================================================
# Question 8
# =========================================================

for i in range(3):
    for j in range(2):
        print(i, j)

print()


# =========================================================
# Question 9
# =========================================================

for i in range(2):
    print("Outer Start", i)

    for j in range(2):
        print("    Inner", j)

    print("Outer End", i)

print()


# =========================================================
# Question 10
# =========================================================

for i in range(2):
    for j in range(3):
        print(i, j)

    print("----")

print()


# =========================================================
# Question 11
# =========================================================

for frame in range(1001, 1004):
    print(f"Frame {frame}")

print()


# =========================================================
# Question 12
# =========================================================

for shot in range(1, 3):
    for frame in range(1001, 1003):
        print(f"Shot {shot} -> Frame {frame}")

print()


# =========================================================
# Question 13
# =========================================================

for progress in range(0, 101, 25):
    print(f"Progress : {progress}%")

print()


# =========================================================
# Question 14
# =========================================================

layers = ["Beauty", "Shadow", "AO"]

for layer in layers:
    print(layer)

print()


# =========================================================
# Question 15
# =========================================================

departments = ["Animation", "Lighting"]
artists = ["Raj", "Amit"]

for department in departments:
    for artist in artists:
        print(f"{department} -> {artist}")

print()

print("========== Topic 17 Completed ==========")