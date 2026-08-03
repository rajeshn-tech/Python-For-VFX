# =========================================================
# Class 07 - Topic 1
# What is a List?
# =========================================================

# print("========== Topic 1 ==========\n")

# =========================================================
# Example 1 String
# =========================================================

# name = "Rajesh"
# print(name)

# print()

# =========================================================
# Example 2 List of Strings
# =========================================================

# names = ["Rajesh", "Amit", "Rahul"]
# print(names)

# print()

# =========================================================
# Example 3 List of Shows
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]
# print(shows)

# print()

# =========================================================
# Example 4 List of Numbers
# =========================================================

# frames = [1001, 1002, 1003]
# print(frames)

# print()

# =========================================================
# Example 5 Mixed Data Types
# =========================================================

# data = ["Rajesh", 1001, True]
# print(data)

# print()

# =========================================================
# Example 6 Production Example
# =========================================================

# render_files = [
#     "ABC_SH010_v001.exr",
#     "ABC_SH020_v001.exr",
#     "ABC_SH030_v001.exr"
# ]

# print(render_files)

# print()


# =========================================================
# Class 07 - Topic 2
# List Indexing
# =========================================================

# print("========== Topic 2 ==========\n")

# =========================================================
# Example 1 Positive Indexing
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# print(shows[0])
# print(shows[1])
# print(shows[2])

# print()


# =========================================================
# Example 2 Negative Indexing
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# print(shows[-1])
# print(shows[-2])
# print(shows[-3])

# print()

# =========================================================
# Example 3 Number List
# =========================================================

# frames = [1001, 1002, 1003]

# print(frames[0])
# print(frames[2])

# print()

# =========================================================
# Example 4 Production Example
# =========================================================

# render_files = [
#     "ABC_SH010_v001.exr",
#     "ABC_SH020_v001.exr",
#     "ABC_SH030_v001.exr"
# ]

# print(render_files[0])
# print(render_files[1])

# print()

# print(render_files[-1])

# =========================================================
# Topic 3 List Slicing
# =========================================================

# shows = ["ABC", "XYZ", "KLM", "PQR", "DEF"]

# # Basic Slicing

# print(shows[1:4])

# print()

# # From Beginning

# print(shows[:3])

# print()

# # Till End

# print(shows[2:])

# print()

# # Complete List

# print(shows[:])

# print()

# # Step

# print(shows[::2])

# print()

# # Production Example

# render_files = [
#     "ABC_SH010_v001.exr",
#     "ABC_SH020_v001.exr",
#     "ABC_SH030_v001.exr",
#     "ABC_SH040_v001.exr",
#     "ABC_SH050_v001.exr"
# ]

# print(render_files[1:4])


# =========================================================
# Class 07 - Topic 4
# Accessing & Modifying List Items
# =========================================================

# print("========== Topic 4 ==========\n")

# =========================================================
# Example 1 Access Item
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# print(shows[0])
# print(shows[2])

# print()


# =========================================================
# Example 2 Modify Item
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows[1] = "PQR"
# print(shows)

# print()


# =========================================================
# Example 3 Number List
# =========================================================

# frames = [1001, 1002, 1003]

# frames[2] = 1010

# print(frames)

# print()


# =========================================================
# Example 4 Production Example
# =========================================================

# render_files =[
#     "ABC_SH010_v001.exr",
#     "ABC_SH020_v001.exr",
#     "ABC_SH030_v001.exr"
# ]

# render_files[2] = "ABC_SH030_v002.exr"

# print(render_files)


# render_files = [
#     "ABC_SH010_v001.exr",
#     "ABC_SH020_v001.exr",
#     "ABC_SH030_v001.exr"
# ]

# print(render_files[1])

# render_files[1] = "ABC_SH020_v002.exr"

# print(render_files)


# =========================================================
# Class 07 - Topic 5
# append()
# =========================================================

# print("========== Topic 5 ==========\n")

# =========================================================
# Example 1
# Add a New Show
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.append("BTT")

# print(shows)

# print()

# =========================================================
# Example 2 Add a New Frame
# =========================================================

# frames = [1001, 1010]

# frames.append(1003)

# print(frames)

# print()

# =========================================================
# Example 3
# Add Artists
# =========================================================

# artists = []

# artists.append("Rajesh")
# artists.append("Amit")
# artists.append("Rahul")

# print(artists)

# print()

# =========================================================
# Example 4
# Production Example
# =========================================================

# render_files = []

# render_files.append("ABC_SH010_v001.exr")
# render_files.append("ABC_SH020_v001.exr")
# render_files.append("ABC_SH030_v001.exr")

# print(render_files)

# print()

# =========================================================
# Example 5
# Modify vs append()
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows[1] = "BTT"

# print(shows)

# shows.append("DTT")

# print(shows)


# =========================================================
# Class 07 - Topic 6
# insert()
# =========================================================


# print("========== Topic 6 ==========\n")

# =========================================================
# Example 1 Insert a Show
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.insert(1, "BTT")

# print(shows)

# print()

# =========================================================
# Example 2 Insert a Frame
# =========================================================

# frames = [1001, 1003]

# frames.insert(1, 1002)

# print(frames)

# print()

# =========================================================
# Example 3 Insert an Artist
# =========================================================

# artists = ["Rajesh", "Rahul"]

# artists.insert(1, "Amit")

# print(artists)

# print()

# =========================================================
# Example 4 production Example
# =========================================================

# render_queue = [
#     "SH010",
#     "SH030",
#     "SH040"
# ]

# render_queue.insert(1, "SH020")

# print(render_queue)

# print()

# =========================================================
# Example 5 append() vs insert()
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.append("MTT")
# print(shows)

# shows.insert(1, "BTT")
# print(shows)

# =========================================================
# Class 07 - Topic 7
# remove()
# =========================================================

# print("========== Topic 7 ==========\n")

# =========================================================
# Example 1 Remove a Show
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.remove("XYZ")

# print(shows)

# print()

# =========================================================
# Example 2 Remove an Artist
# =========================================================

# artists = ["Rajesh", "Amit", "Rahul"]

# artists.remove("Amit")

# print(artists)

# print()

# =========================================================
# Example 3 Remove a Frame
# =========================================================

# frames = [1001, 1002, 1003]

# frames.remove(1002)

# print(frames)

# print()

# =========================================================
# Example 4 Production Example
# =========================================================

# render_queue = [
#     "SH010",
#     "SH020",
#     "SH030",
#     "SH040"
# ]

# render_queue.remove("SH020")

# print(render_queue)

# print()

# =========================================================
# Example 5 insert() vs remove()
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.insert(1, "BTT")

# print(shows)

# shows.remove("BTT")

# print(shows)


# =========================================================
# Class 07 - Topic 8
# pop()
# =========================================================

# print("========== Topic 8 ==========\n")

# =========================================================
# Example 1 Remove a Show using Index
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.pop(1)

# print(shows)

# print()


# =========================================================
# Example 2 Remove a Frame using Index
# =========================================================

# frames = [1001, 1002, 1003]

# frames.pop(0)

# print(frames)

# print()


# =========================================================
# Example 3 Remove an Artist using Index
# =========================================================

# artists = ["Rajesh", "Amit", "Rahul"]

# artists.pop(2)

# print(artists)

# print()


# =========================================================
# Example 4 Production Example
# =========================================================

# render_queue = [
#     "SH010",
#     "SH020",
#     "SH030",
#     "SH040"
# ]

# render_queue.pop(1)

# print(render_queue)

# print()


# =========================================================
# Example 5 remove() vs pop()
# =========================================================

# shows = ["ABC", "XYZ", "KLM", "BTT"]

# shows.remove("XYZ")

# print(shows)

# shows.pop(1)

# print(shows)


# =========================================================
# Class 07 - Topic 9
# clear()
# =========================================================

# print("========== Topic 9 ==========\n")

# =========================================================
# Example 1 Clear a Show List
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]
# shows.clear()

# print(shows)

# print()

# =========================================================
# Example 2 Clear a Frame List
# =========================================================

# frames = [1001, 1002, 1003, 1004]

# frames.clear()

# print(frames)

# print()


# =========================================================
# Example 3 Clear an Artist List
# =========================================================

# artists = ["Rajesh", "Amit", "Rahul"]

# artists.clear()

# print(artists)

# print()

# =========================================================
# Example 4 Production Example
# =========================================================

# render_queue = [
#     "SH010",
#     "SH020",
#     "SH030",
#     "SH040"
# ]

# render_queue.clear()

# print(render_queue)

# print()

# =========================================================
# Example 5 pop() vs clear()
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.pop(1)

# print(shows)

# shows.clear()

# print(shows)


# =========================================================
# Day 07 - Topic 10
# sort()
# =========================================================

# print("========== Topic 10 ==========\n")

# =========================================================
# Example 1 Sort Numbers
# =========================================================

# frames = [1005, 1002, 1008, 1001]

# frames.sort()

# print(frames)

# print()


# =========================================================
# Example 2 Sort Show Names
# =========================================================

# shows = ["XYZ", "ABC", "KLM", "BTT"]

# shows.sort()

# print(shows)

# print()


# =========================================================
# Example 3 Sort Artist Names
# =========================================================

# artists = ["Rahul", "Amit", "Rajesh", "Deepak"]

# artists.sort()

# print(artists)

# print()


# =========================================================
# Example 4 Production Example
# =========================================================

# render_frames = [1050, 1001, 1015, 1030, 1020]

# render_frames.sort()

# print(render_frames)

# print()


# =========================================================
# Example 5 Before and After Sorting
# =========================================================

# frames = [1010, 1003, 1007, 1001]

# print("Before Sort :", frames)

# frames.sort()

# print("After Sort  :", frames)


# =========================================================
# Class 07 - Topic 10 sort(reverse=True)
# =========================================================


# =========================================================
# Example 1 Sort Numbers in Descending Order
# =========================================================

# frames = [1002, 1008, 1001, 1005]

# frames.sort(reverse=True)

# print(frames)

# print()

# =========================================================
# Example 2 Sort Show Names in Descending Order
# =========================================================

# shows = ["ABC", "XYZ", "KLM", "BTT"]

# shows.sort(reverse=True)

# print(shows)

# print()

# =========================================================
# Example 3 Sort Artist Names in Descending Order
# =========================================================

# artists = ["Rajesh", "Amit", "Deepak", "Rahul"]

# artists.sort(reverse=True)

# print(artists)

# print()

# =========================================================
# Example 4 Production Example
# =========================================================

# render_time = [25, 10, 18, 5, 30]

# render_time.sort(reverse=True)

# print(render_time)

# print()

# =========================================================
# Example 5 Ascending vs Descending
# =========================================================

# frames = [1002, 1008, 1001, 1005]

# frames.sort()

# print("Ascending  :", frames)

# frames.sort(reverse=True)

# print("Descending :", frames)


# =========================================================
# Day 07 - Topic 11
# reverse()
# =========================================================

# print("========== Topic 11 ==========\n")

# =========================================================
# Example 1 Reverse Show Names
# =========================================================

# shows = ["ABC", "XYZ", "KLM"]

# shows.reverse()

# print(shows)

# print()


# =========================================================
# Example 2 Reverse Frame Numbers
# =========================================================

# frames = [1001, 1002, 1003, 1004]

# frames.reverse()

# print(frames)

# print()


# =========================================================
# Example 3 Reverse Artist Names
# =========================================================

# artists = ["Rajesh", "Amit", "Rahul", "Deepak"]

# artists.reverse()

# print(artists)

# print()


# =========================================================
# Example 4 Production Example
# =========================================================

# render_queue = [
#     "SH010",
#     "SH020",
#     "SH030",
#     "SH040"
# ]

# render_queue.reverse()

# print(render_queue)

# print()


# =========================================================
# Example 5 sort(reverse=True) vs reverse()
# =========================================================

# frames = [1005, 1001, 1008]

# frames.sort(reverse=True)

# print("sort(reverse=True) :", frames)

# frames = [1005, 1001, 1008]

# frames.reverse()

# print("reverse()          :", frames)

