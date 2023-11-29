"""
    name:  Muhammad Shike
    Project: Recursive Grid Tiling
    Purpose: Design and implement a recursive algorithm for computing L-tilings of square grids.
"""


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


def solver(size_exp, row, col):
    side_length = 1 << size_exp
    grid = [[-1] * side_length for _ in range(side_length)]
    solver_helper(grid, size_exp, 0, side_length, 0, side_length, row, col, 0)
    return grid


def display_answer(answer):
    strings_grid = [[str(num).zfill(2) for num in row] for row in answer]
    display_string = '\n'.join(' '.join(line) for line in strings_grid)
    print(display_string)


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    size = int(input())
    row_str, col_str = input().split()
    row, col = int(row_str), int(col_str)

    answer = solver(size, row, col)
    display_answer(answer)


if __name__ == "__main__":
    main()
    