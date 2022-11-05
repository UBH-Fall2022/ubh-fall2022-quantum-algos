from manim import *

class Grover(Scene):
    def construct(self):
    
    
        # Create Grid
        numplane = NumberPlane(
            x_range = (-5, 15, 1),
            y_range = (-15, 15, 1),
            x_length = 20,
            y_length = 20,
        )
        # axes labels hit/miss vectors
        m_labels = numplane.get_x_axis_label(MathTex(r"\vec{m}"))
        h_labels = numplane.get_y_axis_label(MathTex(r"\vec{h}"))
        
        #initial vector
        dotA = Dot([-5,0,0])
        arrowA = Arrow([-5, 0, 0], [3, 2, 0], buff=0)
        a_label = MathTex(r"\vec{a}").next_to(arrowA.get_end(),DOWN)
        ghostArrowA = DashedLine([-5, 0, 0], [3, 2, 0], buff=0)
        
        # vector a'/first reflection
        arrowAP = Arrow([-5, 0, 0], [3, -2, 0], buff=0)
        ap_label = MathTex(r"\vec{a'}").next_to(arrowAP.get_end(),DOWN)
       
        
        
        
        # Animation #
        self.add(numplane)
        self.play(FadeIn(numplane))
        self.add(m_labels, h_labels)
        self.play(FadeIn(m_labels, h_labels))
        self.wait()
        
        # vector a0
        self.add(dotA, arrowA)
        self.play(Create(arrowA))
        self.add(a_label)
        self.play(FadeIn(a_label))
        self.wait()
        
        self.add(ghostArrowA.add_tip())
        
        self.play(Transform(mobject = arrowA, target_mobject = arrowAP))
        
        #vector a'
        self.add(arrowAP)
        self.add(ap_label)
        self.play(Create(arrowAP), FadeIn(ap_label))
        self.wait()
        
        
        
        