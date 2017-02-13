import alsaaudio
import audioop
import pygame

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, 0)
inp.setchannels(1)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)


def get_volume():
    l, data = inp.read()
    if l:
        return audioop.rms(data, 2)


def shift_left(ls):
    for i in range(1, len(ls)):
        ls[i-1] = ls[i]
    return ls


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
        ratio = 1.0*(val - input_interval_start)
        ratio = ratio / (input_interval_end - input_interval_start)
        num = ratio * (output_interval_end - output_interval_start)
        num += output_interval_start
        return num
    else:
        return 0


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


filename = 'image'
images = []
brects = []
for i in range(100):
    str_num = '0' * (5 - len(str(i))) + str(i)
    path = filename + str_num + '.png'
    myimage = pygame.image.load(path)
    imagerect = myimage.get_rect()
    images.append(myimage)
    brects.append(imagerect)


"""
while True:
    l, data = inp.read()
    if l:
        print(audioop.rms(data, 2))
"""
# max volume level = 1369
# avg = 177

(width, height) = (350, 350)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
running = True
index = 0
running_avg = 0.0
run = []
run_len = 10
for i in range(run_len):
    run.append(get_volume())
running_avg = mean(run)
pygame.display.set_caption('Responds to Noise')


while running:
    run = shift_left(run)
    run[run_len-1] = get_volume()
    avg_vol = mean(run)
    index = int(remap_interval(avg_vol, 0, 3000, 0, 99))
    if index > 99:
        index = 99
    # screen.fill(black)
    screen.blit(images[index], brects[index])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
