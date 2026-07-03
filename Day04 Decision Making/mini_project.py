# ==========================================
# Day 04 - Mini Project
# Shot Validation Tool
# ==========================================

print("=" * 50)
print("      Day 04 - Mini Project")
print("=" * 50)

print()
print("Shot Validation Tool")
print()

# ==========================================
# User Input
# ==========================================

project_name = input("Project Name : ")
sequence = input("Sequence     : ")
shot_name = input("Shot Name    : ")

width = int(input("Width        : "))
height = int(input("Height       : "))

# ==========================================
# Validation Result
# ==========================================

print()
print("=" * 50)
print("Validation Result")
print("=" * 50)

print("Project  :", project_name)
print("Sequence :", sequence)
print("Shot     :", shot_name)

if width == 1920 and height == 1080:
    print("Status   : Shot Validation Passed")
else:
    print("Status   : Shot Validation Failed")

print()
print("=" * 50)
print("Pipeline Finished")
print("=" * 50)