print("=" * 50)
print("         Day 3 - Practice")
print("=" * 50)
print()

# ==========================================
# Arithmetic Operators
# ==========================================

print("=" * 50)
print("      Arithmetic Operators")
print("=" * 50)

print("Addition        :", 10 + 5)
print("Subtraction     :", 10 - 5)
print("Multiplication  :", 10 * 5)
print("Division        :", 10 / 5)
print("Floor Division  :", 10 // 5)
print("Modulus         :", 10 % 5)
print("Power           :", 10 ** 5)

print()

print("20 // 6 =", 20 // 6)
print("20 % 6  =", 20 % 6)
print("3 ** 4  =", 3 ** 4)

# ==========================================
# Operators with Variables
# ==========================================

print()
print("=" * 50)
print("      Operators With Variables")
print("=" * 50)

a = 10
b = 5

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)

print()

width = 1920
height = 1080

print("Width          :", width)
print("Height         :", height)

pixels = width * height

print("Total Pixels   :", pixels)

print()

width = 3840
height = 2160

pixels = width * height

print("Resolution     :", width, "x", height)
print("Total Pixels   :", pixels)

print()

width = 1280
height = 720

pixels = width * height

print("Resolution     :", width, "x", height)
print("Total Pixels   :", pixels)

# ==========================================
# User Input + Operators
# ==========================================

print()
print("=" * 50)
print("      Calculator")
print("=" * 50)

first_number = int(input("Enter First Number  : "))
second_number = int(input("Enter Second Number : "))

print()

print("Addition       :", first_number + second_number)
print("Subtraction    :", first_number - second_number)
print("Multiplication :", first_number * second_number)
print("Division       :", first_number / second_number)
print("Floor Division :", first_number // second_number)
print("Modulus        :", first_number % second_number)
print("Power          :", first_number ** second_number)

# ==========================================
# Comparison Operators
# ==========================================

print()
print("=" * 50)
print("      Comparison Operators")
print("=" * 50)

print("10 == 10 :", 10 == 10)
print("10 != 20 :", 10 != 20)
print("10 > 5   :", 10 > 5)
print("10 < 5   :", 10 < 5)
print("10 >= 10 :", 10 >= 10)
print("10 <= 5  :", 10 <= 5)

# ==========================================
# Comparison with Variables
# ==========================================

print()
print("=" * 50)
print("   Comparison with Variables")
print("=" * 50)

a = 25
b = 10

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# ==========================================
# User Input Comparison
# ==========================================

print()
print("=" * 50)
print("      User Input Comparison")
print("=" * 50)

a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number : "))

print()

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# ==========================================
# Assignment Operators
# ==========================================

print()
print("=" * 50)
print("      Assignment Operators")
print("=" * 50)

value = 10

print("Initial Value :", value)

value += 5
print("After +=      :", value)

value -= 3
print("After -=      :", value)

value *= 2
print("After *=      :", value)

value /= 4
print("After /=      :", value)

# ==========================================
# Logical Operators
# ==========================================

print()
print("=" * 50)
print("      Logical Operators")
print("=" * 50)

print(True and True)
print(True and False)

print(True or False)
print(False or False)

print(not True)
print(not False)