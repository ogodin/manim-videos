from manim import *
from manim.utils import tex_templates
import numpy as np

class Test(Scene):
    def construct(self):
        myTexTemplate = TexTemplate()
        myTexTemplate.add_to_preamble(r'\usepackage{esvect}')
        self.camera.background_color = WHITE

        h = np.array([3, 0, 0])
        v = np.array([-0.5, -1.5, 0])
        p = np.array([1, 1, 0])
        A = np.array([-4, 1, 0])
        B = np.array([3, 1, 0])
        C = np.array([3, -3, 0])
        D = np.array([-4, -3, 0])
        E = A+p
        F = B+p
        G = C+p
        H = D+p
        dotA = Dot(A, color=LIGHT_BROWN)
        dotB = Dot(B, color=LIGHT_BROWN)
        dotC = Dot(C, color=LIGHT_BROWN)
        dotD = Dot(D, color=LIGHT_BROWN)
        dotE = Dot(E, color=LIGHT_BROWN)
        dotF = Dot(F, color=LIGHT_BROWN)
        dotG = Dot(G, color=LIGHT_BROWN)
        dotH = Dot(H, color=LIGHT_BROWN)
        labelA = Tex('$A$').next_to(dotA, 0.1*DOWN+0.1*LEFT).set_color(DARK_BROWN).scale(0.75)
        labelB = Tex('$B$').next_to(dotB, 0.1*DOWN+0.1*RIGHT).set_color(DARK_BROWN).scale(0.75)
        labelC = Tex('$C$').next_to(dotC, 0.1*DOWN+0.1*RIGHT).set_color(DARK_BROWN).scale(0.75)
        labelD = Tex('$D$').next_to(dotD, 0.1*DOWN+0.1*LEFT).set_color(DARK_BROWN).scale(0.75)
        labelE = Tex('$E$').next_to(dotE, 0.1*UP+0.1*LEFT).set_color(DARK_BROWN).scale(0.75)
        labelF = Tex('$F$').next_to(dotF, 0.1*UP+0.1*RIGHT).set_color(DARK_BROWN).scale(0.75)
        labelG = Tex('$G$').next_to(dotG, 0.1*UP+0.1*RIGHT).set_color(DARK_BROWN).scale(0.75)
        labelH = Tex('$H$').next_to(dotH, 0.1*UP+0.1*LEFT).set_color(DARK_BROWN).scale(0.75)

        # self.add(dotA,dotB,dotC,dotD,dotE,dotF,dotG,dotH)

        # Rectangle avant
        l1=Line(A,B).set_color(ORANGE)
        l2=Line(B,C).set_color(ORANGE)
        l3=Line(C,D).set_color(ORANGE)
        l4=Line(D,A).set_color(ORANGE)
        # self.add(l1, l2, l3, l4)

        # Rectangle arrière
        l5 = Line(E,F).set_color(ORANGE)
        l6 = Line(F,G).set_color(ORANGE)
        l7 = DashedLine(G,H).set_color(ORANGE)
        l8 = DashedLine(H,E).set_color(ORANGE)
        # self.add(l5, l6, l7, l8)

        # Lignes avant-arrière
        l9 = Line(A,E).set_color(ORANGE)
        l10 = Line(B,F).set_color(ORANGE)
        l11 = Line(C,G).set_color(ORANGE)
        l12 = DashedLine(D,H).set_color(ORANGE)
        # self.add(l9, l10, l11, l12)

        parallelepipede = VGroup(dotA, dotB, dotC, dotD, dotE, dotF, dotG, dotH,
                                labelA, labelB, labelC, labelD, labelE, labelF, labelG, labelH,
                                l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12)

        self.play(FadeIn(parallelepipede))

        self.wait(3)

        diagAG = Line(A,G).set_color(RED)
        self.play(Create(diagAG))
        diagDF = Line(D,F).set_color(RED)
        self.play(Create(diagDF))
        diagCE = Line(C,E).set_color(RED)
        self.play(Create(diagCE))
        diagBH = Line(B,H).set_color(RED)
        self.play(Create(diagBH))
        M = (A+B+C+D+E+F+G+H)/8
        dotM = Dot(M, color=GREEN)
        labelM = Tex('$M$').next_to(dotM, 0.5*UP).set_color(GREEN).scale(0.75)
        middle = VGroup(dotM,labelM)
        self.add(middle)
        self.wait()

        self.remove(diagAG, diagDF, diagCE, diagBH, middle)
        self.wait()

        labelM1 = Tex('$M_1$').next_to(dotM, 0.5*UP).set_color(RED).scale(0.75)
        middle1 = VGroup(dotM.set_color(RED),labelM1)
        self.play(Create(diagDF.add_tip().set_color(BLUE)))
        self.add(middle1)

        self.wait()

        self.remove(middle1,diagDF)

        self.wait()

        labelM2 = Tex('$M_2$').next_to(dotM, 0.5*UP).set_color(RED).scale(0.75)
        middle2 = VGroup(dotM.set_color(RED),labelM2)
        self.play(Create(diagCE.add_tip().set_color(PURPLE)))
        self.add(middle2)
        self.wait()

        self.remove(middle2,diagCE)
        self.wait()

        parallelepipede_complete = VGroup(parallelepipede, middle.set_opacity(0), middle1.set_opacity(0), middle2.set_opacity(0))

        self.play(parallelepipede_complete.animate.scale(0.5).set_stroke(width=1).to_edge(UL), buff=0.5, run_time=2)
        self.wait()

        dotO = Dot(color=DARK_GRAY).next_to(parallelepipede, direction=DOWN, buff=1.5)
        labelO = Tex('$O$').next_to(dotO, 0.5*DOWN).set_color(DARK_GRAY).scale(0.75)
        origin = VGroup(dotO,labelO).scale(0.5)

        self.add(origin)
        self.wait()

        eq1 = MathTex(
            r'\vv{OM_1}',
            r'& =', 
            r'\vv{OD}',
            r'+',
            r'\tfrac{1}{2} \vv{DF} \\',
            r'\vv{OM_2}',
            r'& =',
            r'\vv{OC}',
            r'+',
            r'\tfrac{1}{2} \vv{CE} \\',
            tex_template=myTexTemplate
        )
        eq1.set_color(BLACK)
        eq1.scale(0.6)
        eq1.next_to(parallelepipede, direction=DOWN, buff=2.75)

        M = (dotD.get_center()+dotF.get_center())/2
        OM1 = Line(start=dotO, end=dotM).set_color(LIGHT_GRAY).set_stroke(width=1).add_tip(tip_length=0.2)
        self.add(middle1.set_opacity(1))
        self.play(Create(OM1), FadeIn(eq1[0]))
        self.wait()

        OD = Line(start=dotO, end=dotD).set_color(GRAY).add_tip(tip_length=0.2)
        DM = Line(start=dotD, end=dotM).set_color(GRAY).add_tip(tip_length=0.2)
        self.add(eq1[1])
        self.wait()
        self.play(Create(OD), FadeIn(eq1[2]))
        self.play(Create(DM), FadeIn(eq1[3]), FadeIn(eq1[4]))
        self.wait()

        self.remove(OM1, middle1, OD, DM)
        self.wait()

        OM2 = Line(start=dotO, end=dotM).set_color(LIGHT_GRAY).set_stroke(width=1).add_tip(tip_length=0.2)
        self.add(middle2.set_opacity(1))
        self.play(Create(OM2), FadeIn(eq1[5]))
        self.wait()

        OC = Line(start=dotO, end=dotC).set_color(GRAY).add_tip(tip_length=0.2)
        CM = Line(start=dotC, end=dotM).set_color(GRAY).add_tip(tip_length=0.2)
        self.add(eq1[6])
        self.wait()
        self.play(Create(OC), FadeIn(eq1[7]))
        self.play(Create(CM), FadeIn(eq1[8]), FadeIn(eq1[9]))
        self.wait()

        self.remove(OM2, middle2, OC, CM)
        self.wait()

        eq2 = MathTex(
            r'\vv{OM_1}', # 0
            r'& =', # 1
            r'\vv{OD}', # 2
            r'+', # 3
            r'\tfrac{1}{2}', # 4
            r'\vv{DF} \\', # 5
            r'& =', # 6
            r'\vv{OC}', # 7
            r'+', # 8
            r'\vv{CD}', # 9
            r'+', # 10
            r'\tfrac{1}{2}', # 11
            r'\vv{DF} \\', # 12
            r'& =', # 13
            r'\vv{OC}', # 14
            r'+', # 15
            r'\vv{CD}', # 16
            r'+', # 17
            r'\tfrac{1}{2}', # 18
            r'\left(', # 19
            r'\vv{DC}', # 20
            r'+', # 21
            r'\vv{CG}', # 22
            r'+', # 23
            r'\vv{GF}', # 24
            r'\right) \\', # 25
            r'& =', # 26
            r'\vv{OC}', # 27
            r'+', # 28
            r'\tfrac{1}{2}', # 29
            r'\left(', # 30
            r'\vv{CD}', # 31
            r'+', # 32
            r'\vv{CG}', # 33
            r'+', # 34
            r'\vv{GF}', # 35
            r'\right) \\', # 36
            r'& =', # 37
            r'\vv{OC}', # 38
            r'+', # 39
            r'\tfrac{1}{2}', # 40
            r'\left(', # 41
            r'\vv{CD}', # 42
            r'+', # 43
            r'\vv{DH}', # 44
            r'+', # 45
            r'\vv{HE}', # 46
            r'\right) \\', # 47
            r'& =', # 48
            r'\vv{OC}', # 49
            r'+', # 50
            r'\tfrac{1}{2}', # 51
            r'\vv{CE} \\', # 52
            r'& =', # 53
            r'\vv{OM_2} \\', # 54
            tex_template=myTexTemplate
        )
        eq2.set_color(BLACK)
        eq2.scale(0.6)
        eq2.next_to(parallelepipede, direction=RIGHT, buff=2.75)
        eq2.shift(DOWN)

        self.add(eq2[0:6])
        self.wait()
        framebox1 = SurroundingRectangle(eq2[2], buff = .1).set_color(BLUE)
        OD = Line(start=dotO, end=dotD).set_color(LIGHT_GRAY).set_stroke(width=1).add_tip(tip_length=0.2)
        self.play(
            Create(framebox1),
            Create(OD),
        )
        self.wait()

        OC = Line(start=dotO, end=dotC).set_color(RED).set_stroke(width=2).add_tip(tip_length=0.2)
        CD = Line(start=dotC, end=dotD).set_color(RED).set_stroke(width=2).add_tip(tip_length=0.2)
        OCCD = VGroup(OC, CD)
        framebox2 = SurroundingRectangle(eq2[7:10], buff = .1).set_color(BLUE)
        self.play(
            Create(OCCD),
            run_time = 2
        )
        self.add(eq2[6:13])
        self.play(
            ReplacementTransform(framebox1, framebox2)
        )
        self.wait()

        self.remove(OD, OCCD, framebox1, framebox2)
        self.wait()

        DF = Line(start=dotD, end=dotF).set_color(LIGHT_GRAY).set_stroke(width=1).add_tip(tip_length=0.2)
        DC = Line(start=dotD, end=dotC).set_color(RED).set_stroke(width=2).add_tip(tip_length=0.2)
        CG = Line(start=dotC, end=dotG).set_color(RED).set_stroke(width=2).add_tip(tip_length=0.2)
        GF = Line(start=dotG, end=dotF).set_color(RED).set_stroke(width=2).add_tip(tip_length=0.2)
        DCCGGF = VGroup(DC, CG, GF)

        framebox1 = SurroundingRectangle(eq2[12], buff = .1).set_color(BLUE)
        framebox2 = SurroundingRectangle(eq2[20:25], buff = .1).set_color(BLUE)

        self.play(
            Create(framebox1),
            Create(DF),
        )
        self.wait()
        self.play(
            Create(DCCGGF),
            run_time = 3
        )
        self.wait()
        self.add(eq2[13:26])
        self.wait()
        self.play(
            ReplacementTransform(framebox1, framebox2)
        )
        self.wait()

        self.remove(DF, DCCGGF, framebox1, framebox2)
        self.wait()

        framebox1 = SurroundingRectangle(eq2[16], buff = .1).set_color(BLUE)
        framebox2 = SurroundingRectangle(eq2[20], buff = .1).set_color(BLUE)
        self.play(
            Create(framebox1),
            Create(framebox2)
        )
        self.wait()

        self.add(eq2[26:37])
        self.wait()

        framebox3 = SurroundingRectangle(eq2[31], buff = .1).set_color(BLUE)
        self.play(
            Create(framebox3)
        )
        self.wait()

        self.remove(framebox1, framebox2, framebox3)
        self.wait()

        self.add(eq2[37:44])
        self.wait()

        CG = Line(start=dotC, end=dotG).set_color(GREEN).set_stroke(width=2).add_tip(tip_length=0.2)
        DH = Line(start=dotD, end=dotH).set_color(GREEN).set_stroke(width=2).add_tip(tip_length=0.2)
        CGDH = VGroup(CG, DH)
        self.play(
            Create(CGDH),
            run_time = 2
        )
        self.wait()
        self.add(eq2[44])
        self.wait()

        self.remove(CGDH)
        self.wait()

        self.add(eq2[45])
        self.wait()

        GF = Line(start=dotG, end=dotF).set_color(GREEN).set_stroke(width=2).add_tip(tip_length=0.2)
        HE = Line(start=dotH, end=dotE).set_color(GREEN).set_stroke(width=2).add_tip(tip_length=0.2)
        GFHE = VGroup(GF, HE)
        self.play(
            Create(GFHE),
            run_time = 2
        )
        self.wait()
        self.add(eq2[46:48])
        self.wait()

        self.remove(GFHE)
        self.wait()

        framebox1 = SurroundingRectangle(eq2[42:47], buff = .1).set_color(BLUE)
        self.add(eq2[48:52])
        self.wait()
        self.play(
            Create(framebox1)
        )
        self.wait()

        CDDHHE = VGroup(CD.set_color(GREEN), DH.set_color(GREEN), HE.set_color(GREEN))
        self.play(
            Create(CDDHHE),
            run_time = 3
        )
        CE = Line(start=dotC, end=dotE).set_color(PURPLE).set_stroke(width=2).add_tip(tip_length=0.2)
        self.play(
            Create(CE)
        )
        self.wait()
        self.add(eq2[52])
        self.wait()
        self.remove(framebox1, CDDHHE, CE)
        self.wait()

        framebox1 = SurroundingRectangle(eq1[5:10], buff = .1).set_color(BLUE)
        self.play(
            Create(framebox1)
        )
        self.wait()
        self.add(eq2[53:55])
        self.wait()
        self.remove(framebox1)

        conclusionl1 = Tex(
            r'Comme $\vv{OM_1} = \vv{OM_2}$, les points $M_1$ et $M_2$',
            tex_template=myTexTemplate
        ).set_color(BLACK).next_to(eq2, direction = DOWN, buff = 0.5).scale(0.6)
        conclusionl2 = Tex(
            r'sont au même endroit, soit au milieu',
            tex_template=myTexTemplate
        ).set_color(BLACK).scale(0.6).next_to(conclusionl1, direction = DOWN)
        conclusionl3 = Tex(
            r'des diagonales $\vv{CE}$ et $\vv{DF}$.',
            tex_template=myTexTemplate
        ).set_color(BLACK).scale(0.6).next_to(conclusionl2, direction = DOWN)
        self.play(Write(conclusionl1))
        self.play(Write(conclusionl2))
        self.play(Write(conclusionl3))
        self.wait()