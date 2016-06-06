from picture import Picture
class char_feed:
    def __init__(self, pic):
        self.pic = pic
    def next_char_coords(self):
        pass


def get_neighbors(x, y, xmax, ymax):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < xmax and 0 <= y + j < ymax:
                yield i + x, j + y

def vec_sum(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def avg_color(pic, x, y):
    cur_sum = [0, 0, 0]
    pixel_count = 0
    for neighbor_x, neighbor_y in get_neighbors(x, y, pic.width, pic.height):
        cur_sum = vec_sum(cur_sum, pic.getPixelColor(neighbor_x, neighbor_y))
        pixel_count += 1
    return [cur_sum[i] / pixel_count for i in range(3)]
    
def blur(pic):
    new_pic = Picture(pic.width, pic.height)
    for i in range(pic.width):
        for j in range(pic.height):
            new_pic.setPixelColor(i, j, *avg_color(pic, i, j))
    return new_pic
