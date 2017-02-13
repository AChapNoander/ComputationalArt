"""
 Project 2: Recursively Generated Art
 Alex Chapman
 1/30/17
 Made it through both extra extensions. Microphone response is seen in the
 python file microphone_implementation in the file microphone_response
 Movie is saved under the name Movie_3
"""
import random
import math
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    first_order = ['x', 'y']
    elementary_func = ['prod', 'avg', 'cos_pi', 'sin_pi', 'square', 'root']

    # Base Case. can say == instead of <= because min depth is only ever
    # decreased by 1
    if min_depth == 0:
        ls = []
        ls.append(first_order[random.randint(0, 1)])
        return ls
    else:
        rand = random.randint(0, len(elementary_func)-1)
        begin = elementary_func[rand]
        arguments = [begin]
        arguments.append(build_random_function(min_depth-1, max_depth-1))

        # Establishes a second argument for the functions which need two
        if rand < 2:
            arguments.append(build_random_function(min_depth-1, max_depth-1))
        return arguments


def build_random_function_3(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth with three parameters, x, y, and t. Allows for
        movie style representation.

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)

        ESSENTIALLY THE SAME AS build_random_function
    """
    first_order = ['x', 'y', 't']
    elementary_func = ['prod', 'avg', 'cos_pi', 'sin_pi', 'square', 'root']
    if min_depth == 0:
        ls = []
        ls.append(first_order[random.randint(0, 2)])
        return ls
    else:
        rand = random.randint(0, len(elementary_func)-1)
        begin = elementary_func[rand]
        arguments = [begin]
        arguments.append(build_random_function_3(min_depth-1, max_depth-1))
        if rand < 2:
            arguments.append(build_random_function_3(min_depth-1, max_depth-1))
        to_return = [begin]
        to_return.append(arguments)
        return arguments


def r_lambda_func(depth):
    """ Builds a random function of depth 'depth'
        Ultimately failed to fully implement lambda functions. :(

        depth: the minimum depth of the random function
        returns: the randomly generated lambda function

        if u have any ideas pls help
    """
    first_order = [lambda x, y: x, lambda x, y: y]
    elementary_func = ['prod', 'avg', 'cos_pi', 'sin_pi']
    if depth == 0:
        rand = random.randint(0, 1)
        if rand == 0:
            return lambda x, y: x
        else:
            return lambda x, y: y
    else:
        rand = random.randint(0, len(elementary_func))
        rand = 1
        if rand == 0:
            return lambda x, y: (r_lambda_func(depth-1)(x, y)) * (r_lambda_func(depth-1)(x, y))
        elif rand == 1:
            return lambda x, y: .5 * ((r_lambda_func(depth-1)(x, y) + r_lambda_func(depth-1)(x, y)))(x, y)
        elif rand == 2:
            return lambda x, y: math.cos(lambda x, y: math.pi(x, y) * r_lambda_func(depth-1)(x, y))(x, y)
        elif rand == 3:
            return lambda x, y: math.sin(lambda x, y: math.pi(x, y) * r_lambda_func(depth-1)(x, y))(x, y)


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    elementary_func = ['prod', 'avg', 'cos_pi', 'sin_pi', 'square', 'root']
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y

    # Kindof effort instensive way to do this, but it allows for a
    # changeable list of functions with less effort
    else:
        if f[0] == elementary_func[0]:
            first_argument = evaluate_random_function(f[1], x, y)
            second_argument = evaluate_random_function(f[2], x, y)
            return first_argument * second_argument
        elif f[0] == elementary_func[1]:
            first_argument = evaluate_random_function(f[1], x, y)
            second_argument = evaluate_random_function(f[2], x, y)
            return .5*(first_argument + second_argument)
        elif f[0] == elementary_func[2]:
            argument = evaluate_random_function(f[1], x, y)
            ans = math.cos(math.pi * argument)
            return ans
        elif f[0] == elementary_func[3]:
            argument = evaluate_random_function(f[1], x, y)
            ans = math.sin(math.pi * argument)
            return ans
        elif f[0] == elementary_func[4]:
            argument = evaluate_random_function(f[1], x, y)
            return argument**2
        elif f[0] == elementary_func[5]:
            argument = evaluate_random_function(f[1], x, y)
            return math.sqrt(math.fabs(argument))


def eval_r_func_3(f, x, y, t):
    """ Evaluate the random function f with inputs x,y,t
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    elementary_func = ['prod', 'avg', 'cos_pi', 'sin_pi']
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "t":
        return t
    else:
        if f[0] == elementary_func[0]:
            first_argument = eval_r_func_3(f[1], x, y, t)
            second_argument = eval_r_func_3(f[2], x, y, t)
            return first_argument * second_argument
        elif f[0] == elementary_func[1]:
            first_argument = eval_r_func_3(f[1], x, y, t)
            second_argument = eval_r_func_3(f[2], x, y, t)
            return .5*(first_argument + second_argument)
        elif f[0] == elementary_func[2]:
            argument = eval_r_func_3(f[1], x, y, t)
            ans = math.cos(math.pi * argument)
            return ans
        elif f[0] == elementary_func[3]:
            argument = eval_r_func_3(f[1], x, y, t)
            ans = math.sin(math.pi * argument)
            return ans


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
        >>> remap_interval(350, 0, 350, -1, 1)
        1.0
    """
    if val is not None:
        # make sure it stays as a float
        ratio = 1.0*(val - input_interval_start)
        ratio = ratio / (input_interval_end - input_interval_start)
        num = ratio * (output_interval_end - output_interval_start)
        num += output_interval_start
        return num
    else:
        return 0


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)

    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel
    im.save(filename)
    return 'saved'


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)

    """
    # Functions for red, green, and blue channels - where the magic happens!
    r_lb = random.randint(6, 10)
    g_lb = random.randint(6, 10)
    b_lb = random.randint(6, 10)
    red_function = build_random_function(r_lb, r_lb+1)
    green_function = build_random_function(g_lb, g_lb+1)
    blue_function = build_random_function(b_lb, b_lb+1)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )
    im.save(filename+'.png')
    return 'saved'


def generate_lambda_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        Attempted. Failed. :(

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)

    """
    # Functions for red, green, and blue channels - where the magic happens!
    r_lb = random.randint(1, 2)
    g_lb = random.randint(1, 2)
    b_lb = random.randint(1, 2)
    red_function = r_lambda_func(1)
    green_function = r_lambda_func(1)
    blue_function = r_lambda_func(1)
    print(red_function)
    print(red_function)
    print(red_function(0.0, 1.0))
    print(red_function(1.0, 0.05))
    print(red_function(1.0, 0.0))

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(red_function(x, y)),
                    color_map(green_function(x, y)),
                    color_map(blue_function(x, y))
                    )
    im.save(filename)
    return 'saved'


def generate_art_3(filename, x_size=350, y_size=350, t_size=30):
    """ Generate computational art and save as a series of image files.

        filename: string base filename for image (should NOT be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
        t_size: optional arg for setting num of frames, default 30
    """
    # Functions for red, green, and blue channels - where the magic happens!
    r_lb = random.randint(1, 5)
    g_lb = random.randint(1, 10)
    b_lb = random.randint(1, 5)
    red_function = build_random_function_3(r_lb, r_lb+1)
    green_function = build_random_function_3(g_lb, g_lb+1)
    blue_function = build_random_function_3(b_lb, b_lb+1)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for time in range(t_size):
        for i in range(x_size):
            for j in range(y_size):
                t = remap_interval(time, 0, t_size, -1, 1)
                x = remap_interval(i, 0, x_size, -1, 1)
                y = remap_interval(j, 0, y_size, -1, 1)
                pixels[i, j] = (
                        color_map(eval_r_func_3(red_function, x, y, t)),
                        color_map(eval_r_func_3(green_function, x, y, t)),
                        color_map(eval_r_func_3(blue_function, x, y, t))
                    )
        str_num = '0' * (5 - len(str(time))) + str(time)
        print(str_num)
        im.save(filename + str_num + '.png')
    return 'saved'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    generate_art('Background', 1920, 1080)
    """
    name = 'wallpaper_'
    for i in range(10):
        title = name + str(i) + '.png'
        generate_art(title, 1334, 750)
    """
