from manim import *
import numpy as np
config.background_color = rgb_to_color(hex_to_rgb('#31343a'))

class motivation(Scene):
    def construct(self):

        self.wait(2)
        title = Text("Calcul intégral", font_size=112)
        subtitle = Text("Introduction", font_size=60).next_to(title, direction=DOWN)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeIn(subtitle))
        self.wait(2)

        self.clear()
        self.wait(2)

        sq = Square().scale(2).move_to(LEFT).set_color(BLUE)
        sq_sidelabel = MathTex('c').next_to(sq, direction=DOWN).set_color(TEAL)
        sq_area = MathTex(r"A = c \times c").next_to(sq, direction=3*RIGHT)
        sq_group = VGroup(sq, sq_sidelabel)
        self.play(FadeIn(sq_group))
        self.play(FadeIn(sq_area))
        self.wait(2)
        self.remove(sq_area)

        tri = Polygon([-5, -1.5, 0], [-2, -1.5, 0], [-3.5, 1.5, 0]).shift(2.5*RIGHT).set_color(BLUE)
        tri_vertices = tri.get_vertices()
        tri_baselabel = MathTex('b').next_to(tri, direction=DOWN).set_color(TEAL)
        tri_middlepoint = (tri_vertices[0] + tri_vertices[1])/2
        tri_height = DashedLine(tri_vertices[2], tri_middlepoint).set_color(TEAL)
        tri_heightlabel = MathTex('h').next_to(tri_height, direction=0.75*LEFT).set_color(TEAL)
        tri_area = MathTex(r"A = \frac{b \times h}{2}").next_to(tri, direction=3*RIGHT)
        tri_group = VGroup(tri, tri_baselabel, tri_height, tri_heightlabel)
        self.play(ReplacementTransform(sq_group, tri_group))
        self.play(FadeIn(tri_area))
        self.wait(2)
        self.remove(tri_area)

        trap = Polygon(2*UP + 1*LEFT, 2*UP + 2*RIGHT, 2*DOWN + 3*RIGHT, 2*DOWN + 4*LEFT).shift(LEFT).set_color(BLUE)
        trap_scale = 0.75
        trap.scale(trap_scale)
        trap_vertices = trap.get_vertices()
        trap_bigbaselabel = MathTex('B').next_to(trap, direction=DOWN).set_color(TEAL)
        trap_smallbasemiddlepoint = (trap_vertices[0] + trap_vertices[1])/2
        trap_smallbaselabel = MathTex('b').next_to(trap_smallbasemiddlepoint, direction=UP).set_color(TEAL)
        trap_height = DashedLine(trap_vertices[0], trap_vertices[3]+trap_scale*3*RIGHT).set_color(TEAL)
        trap_heightlabel = MathTex('h').next_to(trap_height, direction=0.75*LEFT).set_color(TEAL)
        trap_group = VGroup(trap, trap_bigbaselabel, trap_smallbaselabel, trap_height,trap_heightlabel)
        trap_area = MathTex(r"A = \frac{\left(B + b\right) \times h}{2}").next_to(trap, direction=3*RIGHT)
        self.play(ReplacementTransform(tri_group, trap_group))
        self.play(FadeIn(trap_area))
        self.wait(2)
        self.remove(trap_area)

        octo = RegularPolygon(n=8, start_angle=45/2*DEGREES).shift(LEFT).set_color(BLUE)
        octo_scale = 1.75
        octo.scale(octo_scale)
        octo_vertices = octo.get_vertices()
        octo_middlepoint = np.mean(octo_vertices, axis=0)
        octo_apothem = DashedLine(octo_middlepoint, (octo_vertices[3] + octo_vertices[4])/2).set_color(TEAL)
        octo_apothemlabel = MathTex('a').next_to(octo_apothem, direction=UP).set_color(TEAL)
        octo_sidelabel = MathTex('c').next_to(octo, direction=UP).set_color(TEAL)
        octo_group = VGroup(octo, octo_apothem, octo_apothemlabel, octo_sidelabel)
        octo_area = MathTex(r"A = \frac{P \times a}{2}").next_to(trap, direction=3*RIGHT)
        self.play(ReplacementTransform(trap_group, octo_group))
        self.play(FadeIn(octo_area))
        self.wait(2)
        
        self.play(FadeOut(octo_group, octo_area))
        self.wait(2)

        poly = Polygon(3*UP, 2*UP + 2*LEFT, DOWN + LEFT, 3*DOWN + RIGHT, 2*DOWN + 5*RIGHT, UP + 4*RIGHT).set_color(BLUE)
        poly_scale = 0.8
        poly.scale(poly_scale)
        poly.shift(4*LEFT)
        poly_vertices = poly.get_vertices()
        poly_area = MathTex(r'A = ', r'A_1 + A_2 + A_3 + A_4').next_to(poly, direction=4*RIGHT)
        self.play(Create(poly, run_time = 2))
        self.wait(2)
        self.play(FadeIn(poly_area[0]))

        for x in range(2, len(poly_vertices)):
            poly_trianglelabel = MathTex(r"A_{", x-1, "}").move_to(np.mean([poly_vertices[0], poly_vertices[x-1], poly_vertices[x]], axis=0))
            if x < len(poly_vertices)-1:
                poly_innerline = DashedLine(poly_vertices[0], poly_vertices[x]).set_color(TEAL)
                self.play(Create(poly_innerline))
                poly_trianglelabel.shift(0.1*LEFT)
            else:
                poly_trianglelabel.shift(0.3*RIGHT)
                self.wait(0.5)
            self.add(poly_trianglelabel)
        self.wait()
        self.play(Write(poly_area[1]), run_time = 2)

        self.wait(2)
        self.play(*[FadeOut(objects) for objects in self.mobjects])
        self.clear()
        self.wait(2)

        dots = Tex('...', font_size=80).set_color(BLUE)
        dots2 = Tex('...', font_size=80).set_color(BLUE)

        tri_circle = Circle(radius=1.0, color = TEAL, fill_opacity = 0.5)
        sq_circle = Circle(radius=1.0, color = TEAL, fill_opacity = 0.5)
        pent_circle = Circle(radius=1.0, color = TEAL, fill_opacity = 0.5)
        dodec_circle = Circle(radius=1.0, color = TEAL, fill_opacity = 0.5)
        allcircles = VGroup(tri_circle, sq_circle, pent_circle, dots, dodec_circle, dots2).set_x(0).arrange(buff=0.75)
        tri_circle_center = tri_circle.get_center()
        sq_circle_center = sq_circle.get_center()
        pent_circle_center = pent_circle.get_center()
        dodec_circle_center = dodec_circle.get_center()

        tri_vertices = [tri_circle.point_at_angle(((k*360/3+90) % 360)*DEGREES) for k in range(3)]
        tri = Polygon(*tri_vertices).set_color(BLUE)
        sq_vertices = [sq_circle.point_at_angle(((k*360/4+45) % 360)*DEGREES) for k in range(4)]
        sq = Polygon(*sq_vertices).set_color(BLUE)
        pent_vertices = [pent_circle.point_at_angle(((k*360/5+90) % 360)*DEGREES) for k in range(5)]
        pent = Polygon(*pent_vertices).set_color(BLUE)
        dodec_vertices = [dodec_circle.point_at_angle((k*360/12)*DEGREES) for k in range(12)]
        dodec = Polygon(*dodec_vertices).set_color(BLUE)

        allpoly = VGroup(tri, sq, pent, dots, dodec, dots2)

        self.play(Create(allpoly), run_time = 4)

        self.wait(2)

        tri_label = MathTex(r"A_3").next_to(tri_circle, direction=DOWN, buff=0.5)
        sq_label = MathTex(r"A_4").next_to(sq_circle, direction=DOWN, buff=0.5)
        pent_label = MathTex(r"A_5").next_to(pent_circle, direction=DOWN, buff=0.5)
        dodec_label = MathTex(r"A_{12}").next_to(dodec_circle, direction=DOWN, buff=0.5)
        alllabels = VGroup(tri_label, sq_label, pent_label, dodec_label)
        self.play(Write(alllabels), run_time = 4, rate_func = linear)

        self.wait(2)

        tri_circle = Circle(color = TEAL, fill_opacity = 0.5, radius = 3)
        tri_area = MathTex(r"A").scale(3)
        tri_circlegroup = VGroup(tri_circle, tri_area)
        self.play(
            allpoly.animate.set_stroke(opacity = 0.1),
            alllabels.animate.set_fill(opacity = 0.1),
            dots.animate.set_fill(opacity = 0.1),
            dots2.animate.set_fill(opacity = 0.1),
            FadeIn(tri_circlegroup)
        )
        self.wait(2)

        self.play(tri_circlegroup.animate.move_to(tri_circle_center).scale(1/3), tri.animate.set_stroke(opacity = 1), tri_label.animate.set_fill(opacity = 1))
        self.wait(2)
        sq_circle_group = tri_circlegroup.copy()
        self.add(sq_circle_group)
        self.play(sq_circle_group.animate.move_to(sq_circle_center), sq.animate.set_stroke(opacity = 1), sq_label.animate.set_fill(opacity = 1))
        self.wait(2)
        pent_circle_group = sq_circle_group.copy()
        self.add(pent_circle_group)
        self.play(pent_circle_group.animate.move_to(pent_circle_center), pent.animate.set_stroke(opacity = 1), pent_label.animate.set_fill(opacity = 1))
        self.wait(2)
        dodec_circle_group = pent_circle_group.copy()
        self.play(dodec_circle_group.animate.move_to(dodec_circle_center), dodec.animate.set_stroke(opacity = 1), dodec_label.animate.set_fill(opacity = 1), dots.animate.set_fill(opacity = 1))
        self.play(dots2.animate.set_fill(opacity = 1))
        self.wait(2)

        self.play(*[objects.animate.shift(2*UP) for objects in self.mobjects])

        self.wait(2)

        circle_limit = MathTex(r"A = \lim_{n \to \infty} A_n").shift(2*DOWN).scale(2)
        self.play(FadeIn(circle_limit))

        self.wait(2)
        self.play(*[FadeOut(objects) for objects in self.mobjects])
        self.clear()
        self.wait(2)

        axes = Axes(x_range=[-1,8], x_length=10, y_range=[-10,80], y_length=6, y_axis_config={"include_ticks": False},)
        graph = axes.plot(lambda x : x**2 + 10, x_range=[-1,8], color=TEAL)
        area = axes.get_area(graph, [1, 6], color=GREY, opacity=0.5)
        self.add(axes, graph, area)

        dx_list = [1, 0.5, 0.25, 0.1, 0.05, 0.025, 0.01]
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph = graph,
                    x_range = [1, 6],
                    stroke_width = 0.1,
                    stroke_color = WHITE,
                    dx = dx
                )
                for dx in dx_list
            ]
        )

        first_rect = rectangles[0]
        for k in range(1, len(dx_list)):
            new_rect = rectangles[k]
            self.play(Transform(first_rect, new_rect), run_time = 3)
            self.wait(0.5)
        
        self.wait(2)

        return super().construct()