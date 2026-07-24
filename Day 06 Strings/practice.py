"""
=========================================================
Day 06 - Strings
Topic 01 - What is String?
=========================================================

Objective:
Understand what a String is.

A String is a sequence of characters written
inside quotes.

Production Example:
ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk
"""

# print("========== Topic 01 ==========\n")

# # --------------------------------------------------------
# # Basic Strings
# # --------------------------------------------------------

# project = "ABC"
# sequence = "XYZ5120"
# shot = "SH010"
# artist = "Rajesh"

# print("Project   :", project)
# print("Sequence  :", sequence)
# print("Shot      :", shot)
# print("Artist    :", artist)


# # --------------------------------------------------------
# # Production File Name
# # --------------------------------------------------------

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# print("\nProduction File:")
# print(file_name)


"""
=========================================================
Topic 02 - Creating Strings
=========================================================

Objective:
Learn how to create Strings and store them in variables.
"""

# print("========== Topic 02 ==========\n")

# # --------------------------------------------------------
# # Creating Strings
# # --------------------------------------------------------

# project = "ABC"
# artist = "Rajesh"
# software = "Nuke"
# department = "COMP"

# print("Project   :", project)
# print("Artist    :", artist)
# print("Software  :", software)
# print("Department:", department)

# # --------------------------------------------------------
# # Production Example
# # --------------------------------------------------------

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# print("\nProduction File:")
# print(file_name)


"""
=========================================================
Topic 03 - Single Quotes
=========================================================

Objective:
Learn how to create Strings using single quotes.
"""

# print("========== Topic 03 ==========\n")

# # --------------------------------------------------------
# # Creating Strings using Single Quotes
# # --------------------------------------------------------

# project = 'ABC'
# artist = 'Rajesh'
# software = 'Nuke'
# department = 'COMP'

# print("Project   :", project)
# print("Artist    :", artist)
# print("Software  :", software)
# print("Department:", department)

# # --------------------------------------------------------
# # Production Example
# # --------------------------------------------------------

# file_name = 'ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk'

# print("\nProduction File:")
# print(file_name)


"""
=========================================================
Topic 04 - Double Quotes
=========================================================

Objective:
Learn how to create Strings using double quotes.
"""

# print("========== Topic 04 ==========\n")

# # --------------------------------------------------------
# # Creating Strings using Double Quotes
# # --------------------------------------------------------

# project = "ABC"
# artist = "Rajesh"
# software = "Nuke"
# department = "COMP"

# print("Project   :", project)
# print("Artist    :", artist)
# print("Software  :", software)
# print("Department:", department)

# # --------------------------------------------------------
# # Production Example
# # --------------------------------------------------------

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# print("\nProduction File:")
# print(file_name)

# # --------------------------------------------------------
# # Single vs Double Quotes
# # --------------------------------------------------------

# single_quote = 'Python'
# double_quote = "Python"

# print("\nSingle Quote :", single_quote)
# print("Double Quote :", double_quote)

"""
=========================================================
Topic 05 - Triple Quotes
=========================================================

Objective:
Learn how to create multi-line Strings using triple quotes.
"""

# print("========== Topic 05 ==========\n")

# # --------------------------------------------------------
# # Multi-line String
# # --------------------------------------------------------

# message = """
# Welcome
# to
# Python
# for VFX
# """

# print(message)

# # --------------------------------------------------------
# # Production Example
# # --------------------------------------------------------

# render_report = """
# Project    : ABC
# Sequence   : XYZ5120
# Shot       : SH010
# Department : COMP
# Artist     : Rajesh
# Version    : v002
# Status     : Completed
# """

# print("Render Report:")
# print(render_report)



# =========================================================
# Topic 06 - String Indexing
# =========================================================

"""
Objective:
Learn how to access individual characters
from a String using indexing.
"""

# print("========== Topic 06 - String Indexing ==========\n")


# =========================================================
# Example 1
# =========================================================

# artist = "Rajesh"

# print("Artist Name :", artist)
# print("\nCharacter Indexing")

# print("artist[0] :", artist[0])
# print("artist[1] :", artist[1])
# print("artist[2] :", artist[2])
# print("artist[3] :", artist[3])
# print("artist[4] :", artist[4])
# print("artist[5] :", artist[5])


# =========================================================
# Example 2
# =========================================================

# project = "ABC"

# print("\nProject Name :", project)
# print("\nCharacter Indexing")

# print("project[0] :", project[0])
# print("project[1] :", project[1])
# print("project[2] :", project[2])


# =========================================================
# Production Example
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# print("\nProduction File Name:")
# print(file_name)

# print("\nFirst Character  :", file_name[0])
# print("Second Character :", file_name[1])
# print("Third Character  :", file_name[2])
# print("Fourth Character :", file_name[3])
# print("Fifth Character  :", file_name[4])


# =========================================================
# Topic 07 - Negative Indexing
# =========================================================

"""
Objective:
Learn how to access characters from the end
of a String using negative indexing.
"""

# print("========== Topic 07 - Negative Indexing ==========\n")


# =========================================================
# Basic Example
# =========================================================

# artist = "Rajesh"

# print("Artist Name :", artist)
# print("\nNegative Indexing")

# print("artist[-1] :", artist[-1])
# print("artist[-2] :", artist[-2])
# print("artist[-3] :", artist[-3])


# =========================================================
# Production Example
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# print("\nProduction File Name:")
# print(file_name)

# print("\nLast Character        :", file_name[-1])
# print("Second Last Character :", file_name[-2])
# print("Third Last Character  :", file_name[-3])


# =========================================================
# Topic 08 - String Slicing
# =========================================================

"""
Objective:
Learn how to extract multiple characters
from a String using different forms of slicing.
"""

# print("========== Topic 08 - String Slicing ==========\n")


# =========================================================
# Example 1 - Basic Slicing
# =========================================================

# artist = "Rajesh"

# print("Artist Name :", artist)
# print("\nBasic Slicing")

# print("artist[0:3] :", artist[0:3])
# print("artist[3:6] :", artist[3:6])


# =========================================================
# Example 2 - Start and Stop Slicing
# =========================================================

# letters = "ABCDEFG"

# print("\nLetters :", letters)
# print("\nStart and Stop Slicing")

# print("letters[0:3] :", letters[0:3])
# print("letters[1:5] :", letters[1:5])
# print("letters[2:6] :", letters[2:6])


# =========================================================
# Example 3 - Different Forms of Slicing
# =========================================================

# letters = "ABCDEFG"

# print("\nLetters :", letters)
# print("\nDifferent Forms of Slicing")

# print("letters[:4] :", letters[:4])
# print("letters[2:] :", letters[2:])
# print("letters[:]  :", letters[:])


# =========================================================
# Example 4 - Step Slicing
# =========================================================

# letters = "ABCDEFG"

# print("\nLetters :", letters)
# print("\nStep Slicing")

# print("letters[0:7:2] :", letters[0:7:2])
# print("letters[1:7:2] :", letters[1:7:2])
# print("letters[0:6:3] :", letters[0:6:3])


# =========================================================
# Production Example
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# print("\nProduction File Name:")
# print(file_name)

# print("\nProject Code :", file_name[0:3])
# print("Sequence     :", file_name[4:11])
# print("Department   :", file_name[12:15])


# =========================================================
# Topic 09 - String Methods
# =========================================================

"""
Objective:
Learn how to use built-in String methods to process,
modify, search, split, and clean text efficiently.

Methods Covered:
- upper()
- lower()
- title()
- replace()
- split()
- strip()
- find()
- count()

Production Use:
String methods are widely used in VFX pipelines for
file naming, versioning, path handling, text processing,
report generation, and automation tools.
"""

# print("========== Topic 09 - String Methods ==========\n")


# =========================================================
# split()
# =========================================================

# print("========== split() ==========\n")


# =========================================================
# Example 1 - Split Using Comma
# =========================================================

# text = "Apple,Banana,Mango"

# fruits = text.split(",")

# print("Original String :", text)
# print("Split Result    :", fruits)


# =========================================================
# Example 2 - Split Using Space
# =========================================================

# artist = "Rajesh Navsagar"

# name_parts = artist.split(" ")

# print("\nArtist Name  :", artist)
# print("Split Result :", name_parts)


# =========================================================
# Production Example
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# parts = file_name.split("_")

# print("\nProduction File Name:")
# print(file_name)

# print("\nComplete Split Result:")
# print(parts)

# project = parts[0]
# sequence = parts[1]
# department = parts[2]
# element = parts[3]
# artist = parts[6]
# version_and_extension = parts[7]

# print("\nExtracted Information")

# print("Project               :", project)
# print("Sequence              :", sequence)
# print("Department            :", department)
# print("Element               :", element)
# print("Artist                :", artist)
# print("Version and Extension :", version_and_extension)


# =========================================================
# upper()
# =========================================================

# print("\n========== upper() ==========\n")


# =========================================================
# Example 1 - Convert Artist Name to Uppercase
# =========================================================

# artist = "Rajesh"

# uppercase_artist = artist.upper()

# print("Original Artist Name :", artist)
# print("Uppercase Artist Name:", uppercase_artist)


# =========================================================
# Production Example - Standardize Department Name
# =========================================================

# department = "comp"

# clean_department = department.upper()

# print("\nOriginal Department :", department)
# print("Clean Department    :", clean_department)


# =========================================================
# lower()
# =========================================================

# print("\n========== lower() ==========\n")


# =========================================================
# Example 1 - Convert Artist Name to Lowercase
# =========================================================

# artist = "RAJESH"

# lowercase_artist = artist.lower()

# print("Original Artist Name :", artist)
# print("Lowercase Artist Name:", lowercase_artist)


# =========================================================
# Production Example - Standardize File Extension
# =========================================================

# file_extension = ".EXR"

# clean_extension = file_extension.lower()

# print("\nOriginal Extension :", file_extension)
# print("Clean Extension    :", clean_extension)


# =========================================================
# title()
# =========================================================

# print("\n========== title() ==========\n")


# =========================================================
# Example 1 - Format Artist Name
# =========================================================

# artist = "rajesh navsagar"

# formatted_artist = artist.title()

# print("Original Artist Name  :", artist)
# print("Formatted Artist Name :", formatted_artist)


# =========================================================
# Production Example - Format Department Name
# =========================================================

# department = "compositing department"

# formatted_department = department.title()

# print("\nOriginal Department  :", department)
# print("Formatted Department :", formatted_department)


# =========================================================
# replace()
# =========================================================

# print("\n========== replace() ==========\n")


# =========================================================
# Example 1 - Replace Text
# =========================================================

# text = "Python is difficult"

# new_text = text.replace("difficult", "easy")

# print("Original Text :", text)
# print("Updated Text  :", new_text)


# =========================================================
# Production Example 1 - Update Version
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_v001.nk"

# new_file_name = file_name.replace("v001", "v002")

# print("\nOriginal File Name :", file_name)
# print("Updated File Name  :", new_file_name)


# =========================================================
# Production Example 2 - Replace Department
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_v001.nk"

# comp_file_name = file_name.replace("Depth", "Comp")

# print("\nOriginal File Name :", file_name)
# print("Updated File Name  :", comp_file_name)


# =========================================================
# Production Example 3 - Replace Path Separator
# =========================================================

# file_path = "C:/Project/Shot/Render"

# windows_path = file_path.replace("/", "\\")

# print("\nOriginal Path :", file_path)
# print("Windows Path  :", windows_path)


# =========================================================
# strip()
# =========================================================

# print("\n========== strip() ==========\n")


# =========================================================
# Example 1 - Remove Extra Spaces
# =========================================================

# artist = "   Rajesh   "

# clean_artist = artist.strip()

# print("Original Artist :", artist)
# print("Clean Artist    :", clean_artist)


# =========================================================
# Example 2 - Remove Specific Characters
# =========================================================

# text = "---Python---"

# clean_text = text.strip("-")

# print("\nOriginal Text :", text)
# print("Clean Text    :", clean_text)


# =========================================================
# Production Example - Clean Job Status
# =========================================================

# status = "   Completed   "

# clean_status = status.strip()

# print("\nOriginal Status :", status)
# print("Clean Status    :", clean_status)


# =========================================================
# lstrip()
# =========================================================

# text = "   Python   "

# left_clean_text = text.lstrip()

# print("\nOriginal Text    :", text)
# print("Left Clean Text  :", left_clean_text)


# =========================================================
# rstrip()
# =========================================================

# text = "   Python   "

# right_clean_text = text.rstrip()

# print("\nOriginal Text    :", text)
# print("Right Clean Text :", right_clean_text)


# =========================================================
# find()
# =========================================================

# print("\n========== find() ==========\n")


# =========================================================
# Example 1 - Find Character Position
# =========================================================

# artist = "Rajesh"

# position = artist.find("j")

# print("Artist Name       :", artist)
# print("Position of 'j'   :", position)


# =========================================================
# Example 2 - Value Not Found
# =========================================================

# artist = "Rajesh"

# position = artist.find("z")

# print("\nArtist Name       :", artist)
# print("Position of 'z'   :", position)


# =========================================================
# Production Example - Search Element Name
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# depth_position = file_name.find("Depth")

# print("\nProduction File Name:")
# print(file_name)

# print("\nPosition of 'Depth' :", depth_position)


# =========================================================
# Find Using if Statement
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# if file_name.find("Depth") != -1:
#     print("\nDepth Element Found")
# else:
#     print("\nDepth Element Not Found")


# =========================================================
# count()
# =========================================================

# print("\n========== count() ==========\n")


# =========================================================
# Example 1 - Count Character
# =========================================================

# text = "banana"

# total_a = text.count("a")

# print("Original Text :", text)
# print("Total 'a'     :", total_a)


# =========================================================
# Example 2 - Count Character in Artist Name
# =========================================================

# artist = "Rajesh Navsagar"

# total_a = artist.count("a")

# print("\nArtist Name :", artist)
# print("Total 'a'  :", total_a)


# =========================================================
# Production Example - Count Underscores
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# underscore_count = file_name.count("_")

# print("\nProduction File Name:")
# print(file_name)

# print("\nTotal Underscores :", underscore_count)


# =========================================================
# Filename Validation
# =========================================================

# file_name = "ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.nk"

# underscore_count = file_name.count("_")

# if underscore_count == 7:
#     print("\nFilename Structure Looks Valid")
# else:
#     print("\nInvalid Filename Structure")


# =========================================================
# Method Chaining
# =========================================================

# print("\n========== Method Chaining ==========\n")


# =========================================================
# Example 1 - Clean and Convert Status
# =========================================================

# status = "   COMPLETED   "

# clean_status = status.strip().lower()

# print("Original Status :", status)
# print("Clean Status    :", clean_status)


# =========================================================
# Production Example - Clean and Update File Name
# =========================================================

# file_name = "   ABC_XYZ_V001.NK   "

# clean_file_name = (
#     file_name
#     .strip()
#     .lower()
#     .replace("v001", "v002")
# )

# print("\nOriginal File Name :", file_name)
# print("Clean File Name    :", clean_file_name)


# =========================================================
# Final Production Example
# =========================================================

# print("\n========== Final Production Example ==========\n")

# file_name = "   ABC_XYZ5120_DPT_Depth_element_01_Rajesh_v002.NK   "

# clean_file_name = file_name.strip()

# lowercase_file_name = clean_file_name.lower()

# parts = clean_file_name.split("_")

# project = parts[0]
# sequence = parts[1]
# department = parts[2]
# element = parts[3]
# artist = parts[6]
# version_and_extension = parts[7]

# depth_position = clean_file_name.find("Depth")

# underscore_count = clean_file_name.count("_")

# new_version = clean_file_name.replace("v002", "v003")

# print("Clean File Name       :", clean_file_name)
# print("Lowercase File Name   :", lowercase_file_name)
# print("Project               :", project)
# print("Sequence              :", sequence)
# print("Department            :", department)
# print("Element               :", element)
# print("Artist                :", artist)
# print("Version and Extension :", version_and_extension)
# print("Depth Position        :", depth_position)
# print("Total Underscores     :", underscore_count)
# print("Updated Version       :", new_version)


# =========================================================
# Topic 10 - String Operators
# =========================================================

"""
Objective

Practice String Operators.

Operators Covered

1. +
2. *

Production Use

- File Naming
- Folder Paths
- Console Reports
- Log Messages
"""


# =========================================================
# Concatenation (+)
# =========================================================

# Example 1


# first_name = "Rajesh"
# last_name = "Navsagar"

# full_name = first_name + last_name

# print(full_name)


# =========================================================
# Example 2
# =========================================================

# first_name = "Rajesh"
# last_name = "Navsagar"

# full_name = first_name + " " + last_name

# print(full_name)


# =========================================================
# Example 3
# =========================================================

# department = "Compositing"
# software = "Nuke"

# text = department + " - " + software

# print(text)

# =========================================================
# Production Example 1
# =========================================================

# show = "TBO"
# shot = "SFE5120"

# file_name = show + "_" + shot + ".nk"

# print(file_name)

# =========================================================
# Production Example 2
# =========================================================

# project = "Project01"
# sequence = "Seq010"
# shot = "Shot020"

# path = "D:/Projects/" + project + "/" + sequence + "/" + shot

# print(path)


# =========================================================
# Integer Cannot Be Joined Directly
# =========================================================

# version = 2

# print("Version : " + str(version))


# =========================================================
# Repetition (*)
# =========================================================

# Example 1

# print("Python " * 3)


# =========================================================
# Example 2
# =========================================================

# print("-" * 40)


# =========================================================
# Example 3
# =========================================================

# print("*" * 20)

# =========================================================
# Production Example 1
# =========================================================

# print("=" * 60)
# print("Render Report")
# print("=" * 60)


# =========================================================
# Production Example 2
# =========================================================

# title = "Deadline Report"

# print("*" * 50)
# print(title)
# print("*" * 50)

# =========================================================
# Combined Example
# =========================================================

# show = "ABC"
# shot = "XYZ5120"

# file_name = show + "_" + shot + ".exr"

# print("=" * 40)
# print("Output File")
# print(file_name)
# print("=" * 40)