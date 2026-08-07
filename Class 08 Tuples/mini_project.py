"""
=========================================================
Class 08 - Tuples
Mini Project - VFX Shot Data Analyzer
=========================================================
"""

print("=========================================================")
print("VFX SHOT DATA ANALYZER")
print("=========================================================\n")


# =========================================================
# Shot Data
# =========================================================

shot_data = (
    "ABC",
    "SH010",
    "Compositing",
    "Rajesh",
    1001,
    1100,
    "Completed"
)

# =========================================================
# Unpack Shot Data
# =========================================================

show, shot, department, artist, start_frame, end_frame, status = shot_data  



# =========================================================
# Display Shot Information
# =========================================================


print("Show        :", show)
print("Shot        :", shot)
print("Department  :", department)
print("Artist      :", artist)
print("Start Frame :", start_frame)
print("End Frame   :", end_frame)
print("Status      :", status)


print("\n=========================================================")
print("SHOT DATA CHECK")
print("=========================================================\n")


# =========================================================
# Indexing
# =========================================================

print("First Value  :", shot_data[0])
print("Last Value   :", shot_data[-1])


# =========================================================
# Slicing
# =========================================================

print("Basic Info    :", shot_data[:4])



# =========================================================
# Status History
# =========================================================

status_history = (
    "Pending",
    "Rendering",
    "Failed",
    "Rendering",
    "Completed"
)



# =========================================================
# Tuple Methods
# =========================================================

print("Rendering Count :", status_history.count("Rendering"))
print("Failed Index    :", status_history.index("Failed"))

