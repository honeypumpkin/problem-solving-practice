def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + '#'
    
    return line_str

#now use for next problem

def square(n):
    square_str = ''
    for i in range(n):
        square_str += line(n) + '\n'

    return square_str

def rectangle(width, height):
    rectangle_str = ''
    for i in range(height):
        rectangle_str += (line(width) + '\n')

    return rectangle_str




if __name__ == '__main__':
    print(rectangle(12, 3))