from ProgrammingTest import Point
from andrewConvex import compute_perimeter, convex_hull


def main():

    N = int(input())

    points = []

    # Read rectangles
    for _ in range(N):

        x1, y1, x2, y2 = map(float, input().split())

        # Add all 4 corners
        points.append(Point(x1, y1))
        points.append(Point(x1, y2))
        points.append(Point(x2, y1))
        points.append(Point(x2, y2))

    # Compute convex hull
    hull = convex_hull(points)

    # Compute perimeter
    answer = compute_perimeter(hull)

    # Output with precision
    print(f"{answer:.6f}")


if __name__ == "__main__":
    main()