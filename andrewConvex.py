from ProgrammingTest import Point, cross, distance


def convex_hull(points):

    # Remove duplicate points
    points = sorted(set((p.x, p.y) for p in points))

    # Convert back to Point objects
    points = [Point(x, y) for x, y in points]

    n = len(points)

    # Special cases
    if n <= 1:
        return points

    lower = []

    # Build Lower Hull
    for p in points:

        while (len(lower) >= 2 and
               cross(lower[-2], lower[-1], p) <= 0):
            lower.pop()

        lower.append(p)

    upper = []

    
    # Build Upper Hull
    for p in reversed(points):

        while (len(upper) >= 2 and
               cross(upper[-2], upper[-1], p) <= 0):
            upper.pop()

        upper.append(p)

    # Remove duplicate endpoints
    lower.pop()
    upper.pop()

    # Combine hulls
    return lower + upper

# Compute Convex Hull Perimeter
def compute_perimeter(hull):

    n = len(hull)

    if n == 1:
        return 0.0

    perimeter = 0.0

    for i in range(n):
        perimeter += distance(
            hull[i],
            hull[(i + 1) % n]
        )

    return perimeter
