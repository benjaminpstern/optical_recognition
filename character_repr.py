from math import sin, cos, pi, sqrt
from preprocessing import preprocess
def is_dark(pic, x, y, threshold=180):
    r = pic.getPixelRed(x,y)
    g = pic.getPixelBlue(x,y)
    b = pic.getPixelGreen(x,y)
    return r + g + b < threshold


class Char_Repr:
    def __init__(self, pic, xstart=0, ystart=0, \
            xend=None, yend=None, stepsize=60, max_lines=2):
        if not xend:
            xend=pic.width
        if not yend:
            yend=pic.height
        self.pic = preprocess(pic)
        self.xstart = xstart
        self.ystart = ystart
        self.xend = xend
        self.yend = yend
        self.stepsize = stepsize
        self.max_lines = max_lines
        self.points = []
        self.gen_repr()

    def gen_repr(self):
        self.xcenter, self.ycenter = self.center_of_mass()
        self.pic.setPenColor(0, 0, 255)
        self.pic.drawCircleFill(self.xcenter, self.ycenter, 5)
        for angle in range(0, 360, self.stepsize):
            points_for_angle = self.find_points(angle)
            while len(points_for_angle) < 2 * self.max_lines:
                points_for_angle.append(-1)
            while len(points_for_angle) > 2 * self.max_lines:
                points_for_angle.pop(-1)
            self.points.extend(points_for_angle)
        self.normalize()

    def point_average(self):
        total = 0
        counts = 0
        for point in self.points:
            if point != -1:
                total += point
                counts += 1
        if counts:
            return total / counts
        else:
            return 1

    def normalize(self):
        avg = self.point_average()
        for i in range(len(self.points)):
            if self.points[i] != -1:
                self.points[i] = self.points[i] / avg

    def center_of_mass(self):
        xtotal = 0
        ytotal = 0
        pixel_count = 0
        for i in range(self.xstart, self.xend):
            for j in range(self.ystart, self.yend):
                if is_dark(self.pic, i, j):
                    xtotal += i
                    ytotal += j
                    pixel_count += 1
        return xtotal // pixel_count, ytotal // pixel_count

    def in_bounds(self, x, y):
        return self.xstart <= x < self.xend and self.ystart <= y < self.yend

    def distance(self, x, y):
        return sqrt((x - self.xcenter)**2 + (y - self.ycenter)**2)

    def find_points(self, angle):
        """
        returns a list of all lines encountered in start, stop, start, stop form
        distances are from self.center_of_mass along angle
        """
        angle_rads = angle * 1.0 / 360 * 2 * pi
        points = []
        self.pic.setPenColor(255, 0, 0)
        cur_pos_x = self.xcenter
        cur_pos_y = self.ycenter
        in_line = False
        while self.in_bounds(cur_pos_x, cur_pos_y):
            if in_line:
                if not is_dark(self.pic, cur_pos_x, cur_pos_y):
                    in_line = False
                    points.append(self.distance(cur_pos_x, cur_pos_y))
                    self.pic.drawCircleFill(cur_pos_x, cur_pos_y, 2)
            else:
                if is_dark(self.pic, cur_pos_x, cur_pos_y):
                    in_line = True
                    points.append(self.distance(cur_pos_x, cur_pos_y))
                    self.pic.drawCircleFill(cur_pos_x, cur_pos_y, 2)
            cur_pos_x += 3 * cos(angle_rads)
            cur_pos_y += 3 * sin(angle_rads)
        return points
