from picture import Picture
class char_feed:
    def __init__(self, pic):
        self.pic = pic
    def next_char_coords(self):
        pass

def apply_threshold(pic, threshold=-1):
    if threshold == -1:
        center = [pic.width/2, pic.height/2]
        threshold = sum(avg_color(pic, *center, distance=center[0]))

    new_pic = Picture(pic.width, pic.height)
    for i in range(pic.width):
        for j in range(pic.height):
            if sum(pic.getPixelColor(i, j)) > threshold:
                new_pic.setPixelColor(i, j, 255, 255, 255)
            else:
                new_pic.setPixelColor(i, j, 0, 0, 0)
    return new_pic

def preprocess(pic):
    return blur(apply_threshold(pic))

def get_neighbors(x, y, xmax, ymax, distance=1):
    for i in range(-distance, distance + 1):
        for j in range(-distance, distance + 1):
            if 0 <= x + i < xmax and 0 <= y + j < ymax:
                yield i + x, j + y

def vec_sum(a, b):
    return [a[i] + b[i] for i in range(len(a))]

def avg_color(pic, x, y, distance=1):
    height = pic.height
    width = pic.width
    cur_sum = [0, 0, 0]
    pixel_count = 0
    for neighbor_x, neighbor_y in get_neighbors(x, y, width, height, distance):
        cur_sum = vec_sum(cur_sum, pic.getPixelColor(neighbor_x, neighbor_y))
        pixel_count += 1
    return [cur_sum[i] / pixel_count for i in range(3)]
    
def blur(pic):
    new_pic = Picture(pic.width, pic.height)
    for i in range(pic.width):
        for j in range(pic.height):
            new_pic.setPixelColor(i, j, *avg_color(pic, i, j))
    return new_pic
