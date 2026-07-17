# =========================================================
# Day 05 - Topic 19
# Homework
# =========================================================

print("========== Topic 19 ==========\n")

# =========================================================
# Question 1
# Print numbers from 25 to 50.
# =========================================================

for i in range(25, 51):
    print(i)

print()


# =========================================================
# Question 2
# Print numbers from 50 to 25 in reverse order.
# =========================================================

for i in range(50, 24, -1):
    print(i)

print()


# =========================================================
# Question 3
# Print all multiples of 5 from 5 to 50.
# =========================================================

for i in range(5, 51, 5):
    print(i)

print()


# =========================================================
# Question 4
# Print all multiples of 3 from 3 to 30.
# =========================================================

for i in range(3, 31, 3):
    print(i)

print()


# =========================================================
# Question 5
# Print:
#
# Render Layer 1
# Render Layer 2
# Render Layer 3
# Render Layer 4
# =========================================================

for layer in range(1, 5):
    print(f"Render Layer {layer}")

print()


# =========================================================
# Question 6
# Print:
#
# Camera 1
#     Frame 1001
#     Frame 1002
#
# Camera 2
#     Frame 1001
#     Frame 1002
# =========================================================

for camera in range(1, 3):
    print(f"Camera {camera}")

    for frame in range(1001, 1003):
        print(f"    Frame {frame}")

    print()


# =========================================================
# Question 7
# Create a list:
#
# ["Diffuse", "Specular", "Reflection", "Depth"]
#
# Print every layer using a loop.
# =========================================================

layers = ["Diffuse", "Specular", "Reflection", "Depth"]

for layer in layers:
    print(layer)

print()


# =========================================================
# Question 8
# Create two lists:
#
# Assets:
# Car
# Tree
#
# Versions:
# V001
# V002
#
# Output:
#
# Car -> V001
# Car -> V002
# Tree -> V001
# Tree -> V002
# =========================================================

assets = ["Car", "Tree"]
versions = ["V001", "V002"]

for asset in assets:
    for version in versions:
        print(f"{asset} -> {version}")

print()


# =========================================================
# Question 9
# Print:
#
# Project X
#     Sequence 1
#     Sequence 2
#
# Project Y
#     Sequence 1
#     Sequence 2
# =========================================================

projects = ["Project X", "Project Y"]

for project in projects:
    print(project)

    for sequence in range(1, 3):
        print(f"    Sequence {sequence}")

    print()


# =========================================================
# Question 10
# Create your own VFX example using Nested Loops.
# =========================================================

shots = ["Shot001", "Shot002"]

for shot in shots:
    print(shot)

    for frame in range(1001, 1004):
        print(f"    Rendering Frame {frame}")

    print()

print("========== Homework Completed ==========")