# ==========================================
# Day 04 - Homework
# Topic: Decision Making (if, elif, else)
# ==========================================

print("=" * 50)
print("          Day 04 - Homework")
print("=" * 50)

print()
print("Topic : Decision Making (if, elif, else)")
print()

# ==========================================
# Homework 1 - Age Eligibility Tool
# ==========================================

print("=" * 50)
print("      Age Eligibility Tool")
print("=" * 50)

print()

age = int(input("Enter Your Age : "))

print()

if age >= 18:
    print("Status : Eligible")
else:
    print("Status : Not Eligible")

# ==========================================
# Homework 2 - Password Checker
# ==========================================

print()
print("=" * 50)
print("       Password Checker")
print("=" * 50)

print()

password = input("Enter Password : ")

print()

if password == "python123":
    print("Status : Login Successful")
else:
    print("Status : Invalid Password")

# ==========================================
# Homework 3 - Shot Status Checker
# ==========================================

print()
print("=" * 50)
print("      Shot Status Checker")
print("=" * 50)

print()

shot_status = input("Enter Shot Status : ")

print()

if shot_status == "Approved":
    print("Status : Ready For Render")

elif shot_status == "Pending":
    print("Status : Waiting For Approval")

elif shot_status == "Rejected":
    print("Status : Fix Issues")

else:
    print("Status : Invalid Shot Status")

print()
print("=" * 50)
print("Homework Completed")
print("=" * 50)

status = "Pending"

if status == "Approved":
    print("Render")

elif status == "Pending":
    print("Wait")

else:
    print("Invalid")