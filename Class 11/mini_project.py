"""
=========================================================
Class 10 - Sets
Mini Project - VFX Shot Status Analyzer
=========================================================
"""

print("=========================================================")
print("VFX SHOT STATUS ANALYZER")
print("=========================================================\n")


all_shots = {
    "SH010",
    "SH020",
    "SH030",
    "SH040",
    "SH050"
}

completed_shots = {
    "SH010",
    "SH030",
    "SH050"
}

high_priority_shots = {
    "SH020",
    "SH030",
    "SH040"
}


# Find Pending Shots

pending_shots = all_shots.difference(completed_shots)


# Find High-Priority Completed Shots

priority_completed = high_priority_shots.intersection(completed_shots)


# Combine Tracked Shots

tracked_shots = completed_shots.union(high_priority_shots)


# Display Report

print("Completed Shots:")

for shot in completed_shots:
    print(shot)


print("\nPending Shots:")

for shot in pending_shots:
    print(shot)


print("\nHigh-Priority Completed Shots:")

for shot in priority_completed:
    print(shot)


print("\nAll Tracked Shots:")

for shot in tracked_shots:
    print(shot)