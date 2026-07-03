# ==========================================
# Day 04 - Decision Making
# ==========================================

print("=" * 50)
print("      Day 04 - Decision Making")
print("=" * 50)

# ==========================================
# Practice 1 - if Statement
# ==========================================

print()
print("-" * 50)
print("Practice 1 - if Statement")
print("-" * 50)

width = 1920

if width == 1920:
    print("Valid Resolution")

width = 2048

if width == 1920:
    print("Render Started")

# ==========================================
# Practice 2 - else Statement
# ==========================================

print()
print("-" * 50)
print("Practice 2 - else Statement")
print("-" * 50)

width = 2048

if width == 1920:
    print("Render Started")
else:
    print("Render Stopped")

print("Program Finished")

# ==========================================
# Practice 3 - else Statement
# ==========================================

print()
print("-" * 50)
print("Practice 3 - else Statement")
print("-" * 50)

width = 2048

if width == 1920:
    print("Valid Resolution")
else:
    print("Invalid Resolution")

render_status = False

if render_status:
    print("Rendering Started")
else:
    print("Rendering Failed")

print("Pipeline Finished")

# ==========================================
# Practice 4 - elif Statement
# ==========================================

print()
print("-" * 50)
print("Practice 4 - elif Statement")
print("-" * 50)

width = 2048

if width == 1920:
    print("Full HD")

elif width == 2048:
    print("2K")

else:
    print("Unknown Resolution")

file_extension = ".exr"

if file_extension == ".exr":
    print("EXR File")

elif file_extension == ".jpg":
    print("JPEG File")

elif file_extension == ".png":
    print("PNG File")

else:
    print("Unsupported File")

# ==========================================
# Practice 5 - Multiple elif
# ==========================================

print()
print("-" * 50)
print("Practice 5 - Multiple elif")
print("-" * 50)

width = 3840

if width == 1920:
    print("Full HD")

elif width == 2048:
    print("2K")

elif width == 3840:
    print("4K")

else:
    print("Invalid Resolution")

# ==========================================
# Practice 6 - Indentation
# ==========================================

print()
print("-" * 50)
print("Practice 6 - Indentation")
print("-" * 50)

width = 1920

if width == 1920:
    print("Valid Resolution")

print("Program Finished")

if True:
    print("Line 1")
    print("Line 2")

print("Program Finished")

# ==========================================
# Practice 7 - Nested if
# ==========================================

print()
print("-" * 50)
print("Practice 7 - Nested if")
print("-" * 50)

width = 1920
height = 1080

if width == 1920:

    if height == 1080:
        print("Valid Resolution")

print("Pipeline Finished")

# ==========================================
# Practice 8 - and Operator
# ==========================================

print()
print("-" * 50)
print("Practice 8 - and Operator")
print("-" * 50)

width = 1920
height = 1080

if width == 1920 and height == 1080:
    print("Valid Resolution")

print("Pipeline Finished")

# ==========================================
# Practice 9 - and Operator (False Condition)
# ==========================================

print()
print("-" * 50)
print("Practice 9 - and Operator (False Condition)")
print("-" * 50)

width = 1920
height = 720

if width == 1920 and height == 1080:
    print("Valid Resolution")

print("Pipeline Finished")

# ==========================================
# Practice 10 - or Operator
# ==========================================

print()
print("-" * 50)
print("Practice 10 - or Operator")
print("-" * 50)

width = 1920
height = 720

if width == 1920 or height == 1080:
    print("Valid Resolution")

print("Pipeline Finished")

# ==========================================
# Practice 11 - or Operator (False Condition)
# ==========================================

print()
print("-" * 50)
print("Practice 11 - or Operator (False Condition)")
print("-" * 50)

width = 1280
height = 720

if width == 1920 or height == 1080:
    print("Valid Resolution")

print("Pipeline Finished")

# ==========================================
# Practice 12 - not Operator
# ==========================================

print()
print("-" * 50)
print("Practice 12 - not Operator")
print("-" * 50)

render_completed = False

if not render_completed:
    print("Render Pending")

print("Pipeline Finished")