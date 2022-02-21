from typing import List


# def container_with_most_water(height: List[int]) -> int:
#     n = len(height)

#     max_area = 0
#     for i in range(n):
#         for j in range(i, n):
#             l = abs(j - i)
#             h = min(height[i], height[j])
#             area = l * h
#             if area > max_area:
#                 max_area = area

#     return max_area


def container_with_most_water(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    area = 0

    while l < r:
        # Calculating the max area
        area = max(area, min(height[l], height[r]) * (r - l))

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area


# print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(container_with_most_water([1, 1]))
print(container_with_most_water([2, 3, 10, 5, 7, 8, 9]))
print(container_with_most_water([1, 2, 3, 4, 5, 6, 7, 8, 9]))
