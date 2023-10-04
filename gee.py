#calculating area of a rectangle
def calculate_Area(length, width):
    return length * width

#calculating perimeter of a rectancle
def calculate_Parameter(lenght,width):
    return 2 * (lenght + width)

#get users input for the lenght and width 
lenght = int(input("enther the lenght of the rectangle: "))
width = int(input("enter the width of the rectangle: "))

#calculating the area and perimeter
area = calculate_Area(lenght, width)
perimeter = calculate_Parameter(lenght, width)

#displaying result
print(f"the area of the rectangle is:{area}")
print(f"the perimeter of the rectangle is:{perimeter}")