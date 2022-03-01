from manim import *
import numpy as np
config.background_color = rgb_to_color(hex_to_rgb('#31343a'))

class Ouverture(Scene):
    def construct(self):

        self.wait(2)
        title1 = Text("Introduction", font_size=96).shift(UP)
        title2 = Text("à l'algèbre linéaire", font_size=96).next_to(title1, direction=DOWN)
        self.play(FadeIn(title1, title2))
        
        self.wait(2)
        self.play(*[FadeOut(objects) for objects in self.mobjects])
        self.clear()
        self.wait(2)

        return super().construct()


class Droites(Scene):
    def construct(self):

        self.wait(2)

        equation1 = MathTex(r"y = 2x + 1")
        self.play(Write(equation1))
        
        self.wait(2)
        
        
        self.play(equation1.animate.shift(2.75*UP))
        self.wait(2)

        axes1 = Axes(x_range=[-5,5], x_length=10, y_range=[-10,10], y_length=5, axis_config={"include_ticks": False},)
        graph1 = axes1.plot(lambda x : 2*x+1, x_range=[-5, 5], color=BLUE)
        graphique1 = VGroup(axes1, graph1)
        graphique1.next_to(equation1, direction = DOWN, buff=0.75)

        self.play(FadeIn(axes1))
        self.wait(2)
        self.play(Create(graph1))
        self.wait(2)

        coord_point1 = axes1.input_to_graph_point(3, graph = graph1)
        point1 = Dot(coord_point1, color=YELLOW)
        text_point1 = MathTex(r"(3, 7)", color = YELLOW).scale(0.75).next_to(point1, direction=0.15*LEFT+0.15*UP, buff=0.5)
        eq_point1 = MathTex(r"7 = 2(3) + 1", color = YELLOW).scale(0.75).next_to(point1, direction=RIGHT, buff=0.5)
        point1_group = VGroup(point1, text_point1, eq_point1)
        self.play(FadeIn(point1_group))
        self.wait(2)

        coord_point2 = axes1.input_to_graph_point(1, graph = graph1)
        point2 = Dot(coord_point2, color=YELLOW)
        text_point2 = MathTex(r"(1, 3)", color = YELLOW).scale(0.75).next_to(point2, direction=0.15*LEFT+0.15*UP, buff=0.5)
        eq_point2 = MathTex(r"3 = 2(1) + 1", color = YELLOW).scale(0.75).next_to(point2, direction=RIGHT, buff=0.5)
        point2_group = VGroup(point2, text_point2, eq_point2)
        self.play(FadeIn(point2_group))
        self.wait(2)

        coord_point3 = axes1.input_to_graph_point(-4, graph = graph1)
        point3 = Dot(coord_point3, color=YELLOW)
        text_point3 = MathTex(r"(-4, -7)", color = YELLOW).scale(0.75).next_to(point3, direction=0.15*LEFT+0.15*UP, buff=0.5)
        eq_point3 = MathTex(r"-7 = 2(-4) + 1", color = YELLOW).scale(0.75).next_to(point3, direction=RIGHT, buff=0.5)
        point3_group = VGroup(point3, text_point3, eq_point3)
        self.play(FadeIn(point3_group))
        self.wait(2)

        self.play(FadeOut(point1_group, point2_group, point3_group))
        self.wait(2)

        graphique1_et_equation1 = VGroup(graphique1, equation1)
        self.play(graphique1.animate.scale(0.5), equation1.animate.shift(DOWN))
        self.play(graphique1_et_equation1.animate.shift(4*LEFT))
        self.wait(2)

        equation2 = MathTex(r"y = -x - 2")
        equation2.shift(4*RIGHT+1.75*UP)
        self.play(Write(equation2))
        self.wait(2)

        axes2 = Axes(x_range=[-5,5], x_length=10, y_range=[-10,10], y_length=5, axis_config={"include_ticks": False},)
        graph2 = axes2.plot(lambda x : -x-2, x_range=[-5, 5], color=GREEN)
        graphique2 = VGroup(axes2, graph2)
        graphique2.next_to(equation2, direction = DOWN, buff=0.75).scale(0.5).align_to(graphique1, direction=DOWN)
        self.play(FadeIn(axes2))
        self.wait(2)
        self.play(Create(graph2))
        self.wait(2)

        self.play(graphique1.animate.shift(4*RIGHT), graphique2.animate.shift(4*LEFT))
        self.wait(2)

        coord_point_inter = axes1.input_to_graph_point(-1, graph = graph1)
        point_inter = Dot(coord_point_inter, color=YELLOW)
        self.play(FadeIn(point_inter))
        self.wait(2)

        arrow = Arrow(start=coord_point_inter + 0.1*DOWN, end=coord_point_inter + 2*DOWN, max_tip_length_to_length_ratio=0.1, max_stroke_width_to_length_ratio=3, color=YELLOW)
        solution = Text("Solution aux deux équations", font_size=24, color=YELLOW).next_to(arrow, direction=DOWN)
        self.play(Create(arrow))
        self.wait(2)
        self.play(Write(solution))

        self.wait(2)
        self.play(*[FadeOut(objects) for objects in self.mobjects])
        self.clear()
        self.wait(2)

        return super().construct()
    
class Solutions(Scene):
    def construct(self):

        self.wait(2)

        axes1 = Axes(x_range=[-5,5], x_length=7, y_range=[-10,10], y_length=5, axis_config={"include_ticks": False},)
        graph1_line1 = axes1.plot(lambda x : 2*x+3, x_range=[-5, 5], color=BLUE)
        graph1_line2 = axes1.plot(lambda x : -x-3, x_range=[-5, 5], color=GREEN)
        graphique1 = VGroup(axes1, graph1_line1, graph1_line2)
        graphique1.scale(0.5)

        axes2 = Axes(x_range=[-5,5], x_length=7, y_range=[-10,10], y_length=5, axis_config={"include_ticks": False},)
        graph2_line1 = axes2.plot(lambda x : 2*x+3, x_range=[-5, 5], color=BLUE)
        graph2_line2 = axes2.plot(lambda x : 2*x, x_range=[-5, 5], color=GREEN)
        graphique2 = VGroup(axes2, graph2_line1, graph2_line2)
        graphique2.scale(0.5)

        axes3 = Axes(x_range=[-5,5], x_length=7, y_range=[-10,10], y_length=5, axis_config={"include_ticks": False},)
        graph3_line1 = axes3.plot(lambda x : 2*x+3, x_range=[-5, 5], color=BLUE)
        graph3_line2 = axes3.plot(lambda x : 2*x+3, x_range=[-5, 5], color=GREEN)
        graph3_line2_dashed = DashedVMobject(graph3_line2)
        graphique3 = VGroup(axes3, graph3_line1, graph3_line2_dashed)
        graphique3.scale(0.5)

        graphiques = VGroup(graphique1, graphique2, graphique3).set_x(0).arrange(buff=1.0)
        graphiques.shift(0.5*UP)
        self.play(FadeIn(graphiques))
        self.wait(2)

        solution_unique = Text("Solution unique", font_size=32).next_to(graphique1, direction=DOWN, buff=1)
        aucune_solution = Text("Aucune solution", font_size=32).next_to(graphique2, direction=DOWN, buff=1)
        infinite_solution = Text("Infinité de solutions", font_size=32).next_to(graphique3, direction=DOWN, buff=1)

        self.play(Write(solution_unique))
        self.wait(2)
        self.play(Write(aucune_solution))
        self.wait(2)
        self.play(Write(infinite_solution))
        self.wait(2)

        self.play(*[FadeOut(objects) for objects in self.mobjects])
        self.clear()
        self.wait(2)

        return super().construct()

class Matrices(Scene):
    def construct(self):

        self.wait(2)

        equation1 = MathTex("y", "=", "2x", "+", "1")
        equation1.shift(3*LEFT+UP)
        self.play(Write(equation1))
        self.wait(2)

        equation2 = MathTex("y", "=", "-", "x", "-2")
        equation2.shift(3*RIGHT+UP)
        self.play(Write(equation2))
        self.wait(2)

        equation1_isol = MathTex("-", "2x", "+", "y", "=", "1")
        equation1_isol.next_to(equation1, direction=DOWN, buff=0.5)
        self.play(TransformMatchingTex(equation1.copy(), equation1_isol, path_arc=PI/2))
        self.wait(2)

        equation2_isol = MathTex("x", "+", "y", "=", "-2")
        equation2_isol.next_to(equation2, direction=DOWN, buff=0.5)
        self.play(TransformMatchingTex(equation2.copy(), equation2_isol, path_arc=PI/2))
        self.wait(2)

        equation1_color = MathTex("-2", "x", "+", "1", "y", "=", "1")
        equation1_color[0].set_color(RED)
        equation1_color[3].set_color(GREEN)
        equation1_color.next_to(equation1_isol, direction=DOWN, buff=0.5)
        self.play(TransformMatchingTex(equation1_isol.copy(), equation1_color, path_arc=PI/2))
        self.wait(2)

        equation2_color = MathTex("1", "x", "+", "1", "y", "=", "-2")
        equation2_color[0].set_color(BLUE)
        equation2_color[3].set_color(YELLOW)
        equation2_color.next_to(equation2_isol, direction=DOWN, buff=0.5)
        self.play(TransformMatchingTex(equation2_isol.copy(), equation2_color, path_arc=PI/2))
        self.wait(2)

        all_equations = VGroup(equation1, equation2, equation1_isol, equation2_isol, equation1_color, equation2_color)
        self.play(all_equations.animate.shift(1.5*UP))
        self.wait(2)

        coeff_matrix = Matrix([[-2, 1], [1, 1]])
        coeff_matrix.shift(1.5*DOWN)
        elements = coeff_matrix.get_entries()
        colors = [RED, GREEN, BLUE, YELLOW]
        for k in range(len(colors)):
            elements[k].set_color(colors[k])
            elements[k].set_opacity(0)
        self.play(Create(coeff_matrix))
        self.wait(2)

        self.play(equation1_color[0].copy().animate.move_to(elements[0].get_center()))
        self.wait(2)
        self.play(equation1_color[3].copy().animate.move_to(elements[1].get_center()))
        self.wait(2)
        self.play(equation2_color[0].copy().animate.move_to(elements[2].get_center()))
        self.wait(2)
        self.play(equation2_color[3].copy().animate.move_to(elements[3].get_center()))
        self.wait(2)

        br = Brace(coeff_matrix)
        br_text = Text("Matrice des coefficients", font_size=32).next_to(br, direction=DOWN)
        self.play(FadeIn(br))
        self.play(Write(br_text))
        self.wait(2)

        self.play(*[FadeOut(objects) for objects in self.mobjects])
        self.clear()
        self.wait(2)

        return super().construct()