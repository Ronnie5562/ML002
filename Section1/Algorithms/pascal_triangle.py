def pascal_triangle(n):
    if n <= 0:
        return []
    pascal_triangle = [[1]]

    while len(pascal_triangle) < n:
        new_row = [1]
        base = pascal_triangle[-1]
        
        for i in range(len(base) - 1):
            new_row.append(base[i] + base[i + 1])
        new_row.append(1)
        pascal_triangle.append(new_row)
    return pascal_triangle

print(pascal_triangle(6))