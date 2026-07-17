# ==========================================================
# Python for VFX
# Day 04 - Mini Projects
#
# Topics Covered:
# 1. Decision Making (if, else, elif)
# 2. Comparison Operators
# 3. Logical Operators
#
# Mini Projects:
# 1. Shot Validation Tool
# 2. VFX Render Quality Checker
# ==========================================================


# ==========================================================
# Mini Project 01
# Shot Validation Tool
# ==========================================================

print("=" * 50)
print("           Shot Validation Tool")
print("=" * 50)
print()

# -------------------------
# User Input
# -------------------------

project_name = input("Project Name : ")
sequence = input("Sequence     : ")
shot_name = input("Shot Name    : ")

width = int(input("Width        : "))
height = int(input("Height       : "))

print()
print("=" * 50)
print("Validation Result")
print("=" * 50)

print(f"Project  : {project_name}")
print(f"Sequence : {sequence}")
print(f"Shot     : {shot_name}")

# -------------------------
# Resolution Validation
# -------------------------

if width == 1920 and height == 1080:
    print("Status   : Shot Validation Passed")
else:
    print("Status   : Shot Validation Failed")

print()
print("=" * 50)
print("Pipeline Finished")
print("=" * 50)


print("\n\n")


# ==========================================================
# Mini Project 02
# VFX Render Quality Checker
# ==========================================================

print("=" * 50)
print("       VFX Render Quality Checker")
print("=" * 50)
print()

# -------------------------
# Render Settings
# -------------------------

resolution = 4
samples = 64
render_status = "Completed"

# -------------------------
# Resolution Check
# -------------------------

if resolution == 4:
    print("Resolution Approved")
else:
    print("Check Resolution")

# -------------------------
# Sample Check
# -------------------------

if samples >= 64:
    print("Samples Quality Approved")
else:
    print("Increase Samples")

# -------------------------
# Render Status Check
# -------------------------

if render_status == "Completed":
    print("Render Status : Completed")
else:
    print("Render Failed")

# -------------------------
# Final Validation
# -------------------------

if resolution == 4 and samples >= 64 and render_status == "Completed":
    print("Ready for Upload")
else:
    print("Fix Render Settings")

print()
print("=" * 50)
print("Render Validation Finished")
print("=" * 50)