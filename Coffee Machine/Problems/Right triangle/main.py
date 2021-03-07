class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.t_area = .5 * leg_1 * leg_2

    def print_info(self):
        print(self.t_area)


input_c, input_a, input_b = [int(x) for x in input().split()]

if not input_c * input_c == input_a * input_a + input_b * input_b:
    print("Not right")
else:
    triangle = RightTriangle(input_c, input_a, input_b)
    triangle.print_info()
