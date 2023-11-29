# Recursive Grid Tiling

## Project Overview
This Python project addresses the challenging problem of recursively tiling a 2^n x 2^n square grid with L-shaped tiles, with one square removed. It stands at the intersection of computational geometry and algorithmic problem solving, demonstrating the application of recursive algorithms to solve spatial and mathematical challenges.

## Preview
![Recording-2023-11-28-232127](https://github.com/MuhammadK8/Recursive-Grid-Tiling/assets/144934871/4d638143-d08b-4215-89f6-95b87ae2da3e)

## Features

### Recursive Tiling Algorithm
- The core of the project is a recursive function that splits the grid and strategically places L-tiles to cover the entire area, excluding the removed square.

### Dynamic Grid Size
- Users can input any grid size as a power of 2, along with the coordinates of the removed square, making the algorithm versatile and adaptable to various scenarios.

### Tiling Visualization
- The output of the program is a grid representation showing the placement of L-tiles, each uniquely numbered to illustrate the tiling pattern.
---
### Mathematical Induction and Its Application
The project is grounded in the mathematical principle of induction. The core theorem states that a grid of size 2^n x 2^n, minus one square, can be tiled with L-shaped tiles for any integer n. This forms the theoretical foundation for the recursive algorithm, adding complexity and requiring a deep understanding of geometric patterns and recursive structures.

## Programming Skills Showcased
- **Advanced Recursion**: Demonstrates a profound understanding of recursion, crucial for problems with naturally recursive structures, like spatial tiling.
- **Mathematical Problem Solving**: Translates a complex mathematical theorem, grounded in induction, into a practical algorithm, highlighting the ability to apply abstract concepts in real-world applications.
- **Algorithmic Efficiency**: Optimizes the recursive process for large grids, showcasing skill in managing computational resources and algorithm optimization.
- **Data Structure Utilization**: Uses multidimensional arrays effectively to represent and manipulate grid data, showcasing proficiency in data structure manipulation.
- **Problem Decomposition**: Skillfully breaks down the problem into smaller parts, a key aspect of algorithmic thinking.

## Code Snippets and Examples

### Complete Recursive Function for Tiling
```python
def solver_helper(arr, size_exp, left, right, top, bottom, row, col, tile__offset):
    if size_exp == 0:
        return

    tiles_per_quad = ((1 << (2 * size_exp - 2)) - 1) // 3
    
    mid_c = (left + right) // 2
    mid_r = (top + bottom) // 2
    missing_in_right = col >= mid_c
    missing_in_bottom = row >= mid_r

    num = arr[mid_r - 1 + missing_in_bottom][mid_c - 1 + missing_in_right]
    arr[mid_r - 1][mid_c - 1] = tile__offset
    arr[mid_r - 1][mid_c] = tile__offset
    arr[mid_r][mid_c - 1] = tile__offset
    arr[mid_r][mid_c] = tile__offset
    arr[mid_r - 1 + missing_in_bottom][mid_c - 1 + missing_in_right] = num

    for r in [False, True]:
        for b in [False, True]:       
            missing_r, missing_c = (row, col) \
            if r == missing_in_right and b == missing_in_bottom else (mid_r - 1 + b, mid_c - 1 + r)
            quad_left, quad_right = (mid_c, right) if r else (left, mid_c)
            quad_top, quad_bottom = (mid_r, bottom) if b else (top, mid_r)

            solver_helper(arr, size_exp-1, quad_left, quad_right, quad_top,
                          quad_bottom, missing_r, missing_c,           
                               tile__offset + 1 + (r + 2 * b) * tiles_per_quad)
```
### Main Solver Function
```python
def solver(size_exp, row, col):
    side_length = 1 << size_exp
    grid = [[-1] * side_length for _ in range(side_length)]
    solver_helper(grid, size_exp, 0, side_length, 0, side_length, row, col, 0)
    return grid
```

### Main Method
```python
def main():
    size = int(input())
    row_str, col_str = input().split()
    row, col = int(row_str), int(col_str)
    answer = solver(size, row, col)
    display_answer(answer)
```

## Challenges and Learning

### Mathematical Complexity
The mathematical challenge in this project revolved around an intricate theorem in computational geometry: any 2^n x 2^n square grid, with one square removed, can be completely tiled with L-shaped tiles. Each tile covers three squares, forming an L-shape. This theorem necessitates a deep understanding of geometric patterns and recursive structures, as it involves visualizing and implementing a process to methodically cover a large, evolving grid area with a specific tiling pattern.

### Recursive Problem Decomposition
The most significant challenge was decomposing this complex mathematical problem into a recursive algorithm. Recursion, in this context, involves dividing the grid into smaller quadrants in each iteration, with the process repeating until the smallest possible grid (a single square) is reached. This required careful planning to ensure that each recursive step correctly placed the L-tiles, respecting the position of the removed square in each smaller grid.

### Mathematical Operations and Optimization
Implementing the algorithm required a thorough understanding of mathematical operations and their optimization in code. For example, the calculation of the number of tiles per quadrant (`tiles_per_quad = ((1 << (2 * size_exp - 2)) - 1) // 3`) is a compact and efficient way to handle the geometric progression of the grid sizes and the corresponding number of tiles. Such optimizations were crucial for handling larger grid sizes and reducing computational complexity.

### Handling Edge Cases
Another aspect was handling edge cases, such as when the removed square is on the boundaries or corners of the grid. This required additional logic to ensure the algorithm correctly identified the quadrant of the removed square and adjusted the tiling pattern accordingly.

### Learning Outcomes
Working through these challenges enhanced my skills in several areas:
- **Algorithmic Thinking**: Gained a deeper understanding of how to translate complex mathematical concepts into efficient algorithms.
- **Spatial Reasoning**: Improved my ability to visualize and solve spatial problems, a skill that is crucial in fields like computational geometry and computer graphics.
- **Code Optimization**: Learned advanced techniques for optimizing code, especially in the context of recursive functions and large data sets.
- **Problem-Solving**: Enhanced my problem-solving skills, particularly in tackling problems that require abstract thinking and innovative approaches.

### Conclusion
The use of mathematical induction in this project not only adds to its complexity but also serves as a powerful demonstration of the ability to bridge the gap between theoretical mathematics and practical programming. It showcases a high level of proficiency in mathematical reasoning, problem-solving, and algorithmic design.
