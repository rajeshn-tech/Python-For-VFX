"""
Mini Project : File Name Analyzer

Objective

Analyze a production file name and extract
important information using String Methods.

Author : Rajesh Navsagar
"""

# =========================================================
# Input
# =========================================================

file_name = "ABC_XYZ5120_Depth_v001.exr"

parts = file_name.split("_")

show = parts[0]
shot = parts[1]
department = parts[2]

version = parts[3].replace(".exr", "")

extension = file_name.split(".")[1]

is_exr = file_name.endswith(".exr")

is_depth = "Depth" in file_name

starts_with_abc = file_name.startswith("ABC")

underscore_count = file_name.count("_")


print("=" * 45)
print("FILE NAME ANALYZER")
print("="* 45)

print("File Name       :", file_name)
print("Show            :", show)
print("Shot            :", shot)
print("Department      :", department)
print("Version         :", version)
print("Extension       :", extension)


print()

print("Valid EXR        :", is_exr)
print("Depth Pass       :", is_depth)
print("Starts With ABC  :", starts_with_abc)
print("Total Underscore :", underscore_count)

print("=" * 45)