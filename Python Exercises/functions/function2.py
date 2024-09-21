# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(b,h):
    area=(1/2)*b*h
    return area
print(calculate_area(5,6))
print(calculate_area(7,8))