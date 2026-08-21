"""
=========================================================
Class 11 - Functions
Topic 01 - What is a Function?
Practice
=========================================================
"""

# print("========== Topic 01 - What is a Function? ==========\n")


# =========================================================
# Question 1
# =========================================================

# def show_report_header():
#     print("=========================================================")
#     print("VFX RENDER JOB REPORT")
#     print("=========================================================\n")

# show_report_header()


# =========================================================
# Question 2
# =========================================================

# def show_job_status():
#     print("Job: ABC_SH010")
#     print("Status: Rendering")

# show_job_status()

# print()



# =========================================================
# Question 3
# =========================================================

# def check_render():
#     print("Checking Render...")

# check_render()
# check_render()

# print()


# =========================================================
# Question 4
# =========================================================

# def show_artist():
#     print("Artist: John Doe")

# print()


# =========================================================
# Question 5
# =========================================================

# def show_final_status():
#     print("Status: Completed")

# print("Render Started")

# show_final_status()

# print("Report Finished")

# print()


# =========================================================
# Topic 02 - Creating & Calling Functions
# =========================================================

# print("========== Topic 02 - Creating & Calling Functions ==========\n")


# =========================================================
# Question 1
# =========================================================

# def show_artist():
#     print("Artist: Rajesh")

# print("Job Information")

# show_artist()

# print()

# =========================================================
# Question 2
# =========================================================

# def show_status():
#     print("Status: Completed")

# print("Render Report")

# print()


# =========================================================
# Question 3
# =========================================================


# def check_render():
#     print("Checking Render...")

# print("Start")

# check_render()
# check_render()

# print("End")

# print()


# =========================================================
# Question 4
# =========================================================

# def show_job_name():
#     print("Job Name: ABC_SH010_Comp_v001")

# show_job_name()
# show_job_name()
# show_job_name()

# print()

# =========================================================
# Question 5
# =========================================================


# def show_render_status():
#     print("Status: Rendering")

# print("===================================")
# print("VFX RENDER JOB REPORT")
# print("===================================")

# show_render_status()

# print("Report Complete")


# =========================================================
# Topic 03 - Parameters & Arguments
# =========================================================

# print("========== Topic 03 - Parameters & Arguments ==========\n")


# =========================================================
# Question 1
# =========================================================

# def show_department(department):
#     print("Department:", department)

# show_department("Compositing")
# show_department("Lighting")

# print()


# =========================================================
# Question 2
# =========================================================

# def show_priority(priority):
#     print("Priority:", priority)

# show_priority(80)
# show_priority(50)

# print()


# =========================================================
# Question 3
# =========================================================

# def show_frame(frame):
#     print("Frame:", frame)

# print("Render Started")

# show_frame(1001)
# show_frame(1002)
# show_frame(1003)

# print("Render Completed")

# print()


# =========================================================
# Question 4
# =========================================================

# def show_artist(artist):
#     print("Artist:", artist)

# print("Job Started")

# show_artist("Rajesh")

# print("Processing...")

# show_artist("Amit")

# print("Job Finished")

# print()


# =========================================================
# Question 5 - Production Example
# =========================================================

# def show_job(job_name):
#     print("Processing:", job_name)

# print("VFX RENDER JOB REPORT")

# show_job("ABC_SH010")
# show_job("XYZ_SH020")
# show_job("KLM_SH030")

# print("Report Complete")

# =========================================================
# Topic 04 - Multiple Parameters
# =========================================================

# print("========== Topic 04 - Multiple Parameters ==========\n")


# =========================================================
# Question 1
# =========================================================

# def show_frame(shot, frame):
#     print("Shot:", shot)
#     print("Frame:", frame)

# show_frame("SH010", 1001)

# print()


# =========================================================
# Question 2
# =========================================================

# def show_artist_job(job_name, artist):
#     print("Job:", job_name)
#     print("Artist:", artist)

# show_artist_job("ABC_SH020", "Rajesh")

# print()


# =========================================================
# Question 3
# =========================================================

# def show_render_job(job_name, artist, status):
#     print("Job:", job_name)
#     print("Artist:", artist)
#     print("Status:", status)

# show_render_job("XYZ_SH030", "Amit", "Rendering")

# print()


# =========================================================
# Question 4 - Multiple Function Calls
# =========================================================

# def show_priority_job(job_name, priority):
#     print("Job:", job_name)
#     print("Priority:", priority)

# show_priority_job("SH010", 80)
# show_priority_job("SH020", 50)

# print()


# =========================================================
# Question 5 - Argument Order
# =========================================================

# def show_job_info(job_name, artist, priority):
#     print("Job:", job_name)
#     print("Artist:", artist)
#     print("Priority:", priority)

# show_job_info("Rajesh", 90, "SH040")

# print()


# =========================================================
# Question 6 - Production Example
# =========================================================

# def show_render_report(job_name, artist, status, priority):
#     print("Job Name:", job_name)
#     print("Artist:", artist)
#     print("Status:", status)
#     print("Priority:", priority)

# print("=========================================================")
# print("VFX RENDER JOB REPORT")
# print("=========================================================")

# show_render_report(
#     "ABC_SH050_Comp_v002",
#     "Rajesh",
#     "Rendering",
#     80
# )

# print("=========================================================")
# print("REPORT COMPLETE")
# print("=========================================================")

# =========================================================
# Topic 05 - Default Parameters
# =========================================================

# print("========== Topic 05 - Default Parameters ==========\n")


# =========================================================
# Question 1
# =========================================================

# def show_status(status="Rendering"):
#     print("Status:", status)

# show_status()

# print()


# =========================================================
# Question 2
# =========================================================

# def show_department(department="Compositing"):
#     print("Department:", department)

# show_department()
# show_department("Lighting")

# print()


# =========================================================
# Question 3
# =========================================================

# def show_priority(priority=50):
#     print("Priority:", priority)

# show_priority()
# show_priority(80)
# show_priority(100)

# print()


# =========================================================
# Question 4
# =========================================================

# def show_blade(blade, status="Online"):
#     print("Blade:", blade)
#     print("Status:", status)

# show_blade("Blade01")
# show_blade("Blade02", "Offline")

# print()


# =========================================================
# Question 5
# =========================================================

# def show_job(job_name, priority=50):
#     print("Job:", job_name)
#     print("Priority:", priority)

# show_job("SH010")
# show_job("SH020", 90)

# print()


# =========================================================
# Question 6 - Production Example
# =========================================================

# def show_render(job_name, status="Pending"):
#     print("Job:", job_name)
#     print("Status:", status)

# show_render("ABC_SH010")
# show_render("XYZ_SH020", "Completed")

# print()


# =========================================================
# Topic 06 - return Statement
# =========================================================

# print("========== Topic 06 - return Statement ==========\n")


# =========================================================
# Question 1
# =========================================================

# def get_priority():
#     return 80

# priority = get_priority()

# print("Priority:", priority)

# print()


# =========================================================
# Question 2
# =========================================================

# def get_status():
#     return "Completed"

# status = get_status()

# print("Status:", status)

# print()


# =========================================================
# Question 3
# =========================================================

# def get_frame():
#     return 1001

# frame = get_frame()

# print("Current Frame:", frame)

# print()


# =========================================================
# Question 4
# =========================================================

# def calculate_frames(start_frame, end_frame):
#     total_frames = end_frame - start_frame + 1
#     return total_frames

# frames = calculate_frames(1001, 1010)

# print("Total Frames:", frames)

# print()


# =========================================================
# Question 5
# =========================================================

# def calculate_time(frames, time_per_frame):
#     total_time = frames * time_per_frame
#     return total_time

# render_time = calculate_time(10, 5)

# print("Render Time:", render_time)

# print()


# =========================================================
# Question 6 - return Stops the Function
# =========================================================

# def get_job_status():
#     print("Checking Job...")
#     return "Rendering"
#     print("Checking Complete")

# job_status = get_job_status()

# print("Job Status:", job_status)

# print()


# =========================================================
# Question 7 - Production Example
# =========================================================

# def calculate_render_time(frames, time_per_frame):
#     total_time = frames * time_per_frame
#     return total_time

# total_render_time = calculate_render_time(20, 3)

# print("Total Render Time:", total_render_time)


def check_blade(render_time):
    if render_time > 60:
        return "Slow"
    else:
        return "Normal"


blade_status = check_blade(75)

print("Blade Status:", blade_status)