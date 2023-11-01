#Duplicate code example
def calculate(length, width, height):
    area = length * width
    perimeter = 2 * (length + width)
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    return area, perimeter, volume, surface_area

# Duplicate code: calculate_area and calculate_perimeter functions have similar calculations.
def calculate_area_perimeter(length, width):
    area, perimeter = calculate(length, width, 0)
    return area, perimeter
