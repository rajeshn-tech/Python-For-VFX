# =========================================================
# Project : Render Queue Simulator
# Day 05 - Mini Project
#
# Description:
# Simulates rendering multiple shots, where each shot
# contains a sequence of frames to be rendered.
# =========================================================

print("========== Render Queue Simulator ==========\n")

for shot in range(1, 4):
    print(f"Starting Shot {shot}")

    for frame in range(1001, 1006):
        print(f"    Rendering Frame {frame}")

    print(f"Shot {shot} Completed\n")

print("========== Render Queue Finished ==========")