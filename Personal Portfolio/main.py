#Avery bowman, Personal Portfolio

from financial_calculator import 
from password_gen import 
from rock_paper_scissors import 
from  import 
from  import 

def menu():
    shapes = []

    while True:
        print("\n=== Geometry Calculator ===")
        print("1. Create Shape")
        print("2. Show All Shapes")
        print("3. Compare Two Shapes")
        print("4. Sort Shapes")
        print("0. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == '1':  # General Shape Creation Option
                print("\nSelect the type of shape to create:")
                print("a. Circle")
                print("b. Rectangle")
                print("c. Square")
                print("d. Triangle")
                shape_choice = input("Choose a shape (a/b/c/d): ").strip().lower()

                if shape_choice == 'a':
                    radius = float(input("Enter radius: "))
                    if radius <= 0:
                        print("Radius must be positive.")
                        continue
                    shapes.append(Circle(radius))
                    print("Circle created.")
                elif shape_choice == 'b':
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    if length <= 0 or width <= 0:
                        print("Length and width must be positive.")
                        continue
                    shapes.append(Rectangle(length, width))
                    print("Rectangle created.")
                elif shape_choice == 'c':
                    side = float(input("Enter side: "))
                    if side <= 0:
                        print("Side must be positive.")
                        continue
                    shapes.append(Square(side))
                    print("Square created.")
                elif shape_choice == 'd':
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    a = float(input("Enter side A: "))
                    b = float(input("Enter side B: "))
                    c = float(input("Enter side C: "))
                    if base <= 0 or height <= 0 or a <= 0 or b <= 0 or c <= 0:
                        print("All dimensions must be positive.")
                        continue
                    shapes.append(Triangle(base, height, a, b, c))
                    print("Triangle created.")
                else:
                    print("Invalid shape option.")

            elif choice == '2':  # Show All Shapes
                if not shapes:
                    print("No shapes created yet.")
                else:
                    print("\nAll Shapes:")
                    for i, shape in enumerate(shapes):
                        print(f"{i}: {shape.display_info()}")

            elif choice == '3':  # Compare Two Shapes
                if len(shapes) < 2:
                    print("You need at least two shapes to compare.")
                else:
                    try:
                        idx1 = int(input("First shape index: "))
                        idx2 = int(input("Second shape index: "))
                        if idx1 >= len(shapes) or idx2 >= len(shapes):
                            print("Invalid shape index.")
                        elif shapes[idx1].has_larger_area(shapes[idx2]):
                            print("First shape has a larger area.")
                        else:
                            print("Second shape has a larger area.")
                    except ValueError:
                        print("Please enter valid integer indexes.")

            elif choice == '4':  # Sort Shapes
                if not shapes:
                    print("No shapes to sort.")
                else:
                    sort_by = input("Sort by 'area' or 'perimeter': ").strip().lower()
                    if sort_by not in ['area', 'perimeter']:
                        print("Invalid sort option.")
                    else:
                        sorted_list = sort_shapes(shapes, sort_by)
                        print(f"\nShapes sorted by {sort_by}:")
                        for s in sorted_list:
                            print(s.display_info())

            elif choice == '0':  # Exit
                print("Exiting...")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input. Please enter numbers only where required.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    menu()