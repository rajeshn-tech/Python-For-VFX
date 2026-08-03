"""
=========================================================
Class 07 - Lists
Mini Project - Render Queue Organizer
=========================================================

Objective:
Create a simple tool to manage a VFX render queue.

Features:
- Display Render Queue
- Add a New Shot
- Add a Priority Shot
- Remove a Shot
- Remove a Shot by Index
- Sort Render Queue
- Reverse Render Queue
- Clear Render Queue
- Exit Tool

Author:
Rajesh Navsagar
=========================================================
"""

# =========================================================
# Initial Render Queue
# =========================================================

render_queue = [
    "ABC_SH030",
    "ABC_SH010",
    "ABC_SH020",
]

# =========================================================
# Main Program
# =========================================================

while True:

    print("\n" + "=" * 50)
    print("RENDER QUEUE ORGANIZER")
    print("=" * 50)

    print("1. Display Render Queue")
    print("2. Add New Shot")
    print("3. Add Priority Shot")
    print("4. Remove Shot by Name")
    print("5. Remove Shot by Index")
    print("6. Sort Render Queue")
    print("7. Reverse Render Queue")
    print("8. Clear Render Queue")
    print("9. Exit")

    print("=" * 50)

    choice = input("Enter your choice: ").strip()

    # =====================================================
    # Option 1 - Display Render Queue
    # =====================================================

    if choice == "1":

        print("\nCurrent Render Queue")
        print("-" * 50)

        if len(render_queue) == 0:
            print("Render queue is empty.")

        else:
            for index in range(len(render_queue)):
                print(index, "-", render_queue[index])

    # =====================================================
    # Option 2 - Add New Shot
    # =====================================================

    elif choice == "2":

        shot_name = input("Enter shot name: ").strip().upper()

        if shot_name == "":
            print("Shot name cannot be empty.")

        elif shot_name in render_queue:
            print("Shot already exists in the render queue.")

        else:
            render_queue.append(shot_name)

            print("Shot added successfully.")
            print(render_queue)

    # =====================================================
    # Option 3 - Add Priority Shot
    # =====================================================

    elif choice == "3":

        shot_name = input("Enter priority shot name: ").strip().upper()

        if shot_name == "":
            print("Shot name cannot be empty.")

        elif shot_name in render_queue:
            print("Shot already exists in the render queue.")

        else:
            render_queue.insert(0, shot_name)

            print("Priority shot added successfully.")
            print(render_queue)

    # =====================================================
    # Option 4 - Remove Shot by Name
    # =====================================================

    elif choice == "4":

        shot_name = input("Enter shot name to remove: ").strip().upper()

        if shot_name in render_queue:
            render_queue.remove(shot_name)

            print("Shot removed successfully.")
            print(render_queue)

        else:
            print("Shot not found in the render queue.")

    # =====================================================
    # Option 5 - Remove Shot by Index
    # =====================================================

    elif choice == "5":

        if len(render_queue) == 0:
            print("Render queue is empty.")

        else:
            print("\nCurrent Render Queue")

            for index in range(len(render_queue)):
                print(index, "-", render_queue[index])

            index_text = input("Enter shot index to remove: ").strip()

            if index_text.isdigit():

                shot_index = int(index_text)

                if shot_index < len(render_queue):
                    render_queue.pop(shot_index)

                    print("Shot removed successfully.")
                    print(render_queue)

                else:
                    print("Invalid shot index.")

            else:
                print("Index must contain digits only.")

    # =====================================================
    # Option 6 - Sort Render Queue
    # =====================================================

    elif choice == "6":

        render_queue.sort()

        print("Render queue sorted successfully.")
        print(render_queue)

    # =====================================================
    # Option 7 - Reverse Render Queue
    # =====================================================

    elif choice == "7":

        render_queue.reverse()

        print("Render queue reversed successfully.")
        print(render_queue)

    # =====================================================
    # Option 8 - Clear Render Queue
    # =====================================================

    elif choice == "8":

        render_queue.clear()

        print("Render queue cleared successfully.")
        print(render_queue)

    # =====================================================
    # Option 9 - Exit Tool
    # =====================================================

    elif choice == "9":

        print("\nRender Queue Organizer closed.")
        break

    # =====================================================
    # Invalid Choice
    # =====================================================

    else:
        print("Invalid choice. Enter a number from 1 to 9.")