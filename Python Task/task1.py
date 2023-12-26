def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(area)
