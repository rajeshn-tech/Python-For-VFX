"""
=========================================================
Class 09 - Dictionaries
Topic 01 - What is a Dictionary?
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist)

# print()

# =========================================================
# Question 2
# =========================================================

# shot = {
#     "Show": "ABC",
#     "Shot": "SH010",
#     "Status": "Completed"
# }

# print(shot)

# print()

# =========================================================
# Question 3
# =========================================================

# blade = {
#     "Blade": "Blade-01",
#     "CPU": "95%",
#     "RAM": "64 GB"
# }

# print(blade)

# print()

# =========================================================
# Question 4
# =========================================================

# deadline_job = {
#     "Job Name": "ABC_SH010_Comp_v001",
#     "Artist": "Rajesh",
#     "Department": "Compositing",
#     "Status": "Completed"
# }

# print(deadline_job)


"""
=========================================================
Class 09 - Dictionaries
Topic 02 - Creating Dictionaries
Practice
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {}

# print(artist)

# print()


# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Shift": "Night"
# }

# print(artist)

# print()


# =========================================================
# Question 3
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Experience": 3,
#     "Available": True
# }

# print(artist)

# print()


# =========================================================
# Question 4
# =========================================================

# deadline_job = {
#     "Job Name": "ABC_SH010_Comp_v001",
#     "Artist": "Rajesh",
#     "Department": "Compositing",
#     "Frames": "1001-1100",
#     "Status": "Completed"
# }

# print(deadline_job)


"""
=========================================================
Class 09 - Dictionaries
Topic 03 - Accessing Values
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist["Name"])

# print()

# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist["Department"])

# print()

# =========================================================
# Question 3
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist["Experience"])

# print()

# =========================================================
# Question 4
# =========================================================

# deadline_job = {
#     "Job Name": "ABC_SH010_Comp_v001",
#     "Artist": "Rajesh",
#     "Status": "Completed",
#     "Frames": "1001-1100"
# }

# print(deadline_job["Status"])

# print()

# =========================================================
# Question 5
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# print(artist["Age"])

"""
=========================================================
Class 09 - Dictionaries
Topic 04 - Adding & Updating Data
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# artist["Department"] = "Compositing"

# print(artist)

# print()


# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# artist["Experience"] = 3

# print(artist)

# print()


# =========================================================
# Question 3
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# artist["Department"] = "Lighting"

# print(artist)

# print()


# =========================================================
# Question 4
# =========================================================

# job = {
#     "Status": "Queued"
# }

# job["Status"] = "Rendering"

# print(job)

# print()


# =========================================================
# Question 5
# =========================================================

# job = {
#     "Status": "Rendering"
# }

# job["Artist"] = "Rajesh"

# print(job)

"""
=========================================================
Class 09 - Dictionaries
Topic 05 - Removing Data
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# del artist["Department"]

# print(artist)

# print()

# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Experience": 3,
#     "Available": True
# }

# del artist["Available"]

# print(artist)

# print()

# =========================================================
# Question 3
# =========================================================

# job = {
#     "Job Name": "ABC_SH010",
#     "Status": "Completed",
#     "Frames": "1001-1100"
# }

# del job["Frames"]

# print(job)

# print()

# =========================================================
# Question 4
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# del artist["Age"]


"""
=========================================================
Class 09 - Dictionaries
Topic 06 - Dictionary Methods
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist.keys())

# print()

# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist.values())

# print()

# =========================================================
# Question 3
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist.items())

# print()

# =========================================================
# Question 4
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# print(artist.get("Department"))

# print()

# =========================================================
# Question 5
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# print(artist.get("Age"))

"""
=========================================================
Class 09 - Dictionaries
Topic 07 - Looping Through Dictionary
=========================================================
"""

# print("========== Practice ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# for key in artist:
#     print(key)

# print()


# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# for value in artist.values():
#     print(value)

# print()


# =========================================================
# Question 3
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# for key, value in artist.items():
#     print(key, ":", value)

# print()


# =========================================================
# Question 4
# =========================================================

# job = {
#     "Job Name": "ABC_SH010",
#     "Status": "Completed"
# }

# for key, value in job.items():
#     print(key, ":", value)


"""
=========================================================
Class 09 - Dictionaries
Topic 09 - Output Prediction
=========================================================
"""

# print("========== Output Prediction ==========\n")

# =========================================================
# Question 1
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# print(artist["Name"])

# print()

# =========================================================
# Question 2
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# artist["Department"] = "Lighting"

# print(artist)

# print()

# =========================================================
# Question 3
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# del artist["Department"]

# print(artist)

# print()

# =========================================================
# Question 4
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist.keys())

# print()

# =========================================================
# Question 5
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing",
#     "Experience": 3
# }

# print(artist.values())

# print()

# =========================================================
# Question 6
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# print(artist.get("Age"))

# print()

# =========================================================
# Question 7
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# for key in artist:
#     print(key)

# print()

# =========================================================
# Question 8
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# for value in artist.values():
#     print(value)

# print()

# =========================================================
# Question 9
# =========================================================

# artist = {
#     "Name": "Rajesh",
#     "Department": "Compositing"
# }

# for key, value in artist.items():
#     print(key, ":", value)

# print()

# =========================================================
# Question 10
# =========================================================

# artist = {
#     "Name": "Rajesh"
# }

# print(artist["Age"])