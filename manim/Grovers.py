from manim import *
import numpy as np

class Grover(Scene):
    def construct(self):
    
    
        # Create Grid
        numplane = NumberPlane(
            x_range = (-5, 15, 1),
            y_range = (-15, 15, 1),
            x_length = 20,
            y_length = 20,
        )
        
        m_axis = Line([-5, 0, 0], [15, 0, 0])
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
        ghostArrowAP = DashedLine([-5, 0, 0], [3, -2, 0], buff=0)
       
        #vector a''/second reflection
        arrowAPP = Arrow([-5, 0, 0], [-2, 3.35, 0], buff=0)
        app_label = MathTex(r"\vec{a''}").next_to(arrowAPP.get_end(),DOWN)
        
        #angle 1
        angle = Angle(m_axis, arrowA, radius = 2.0)
        theta = MathTex(r"\theta").next_to(angle)
        
        #angle 2
        angle2 = Angle(arrowAP, m_axis, radius = 2.5)
        theta2 = MathTex(r"-\theta").next_to(angle2)
        
        equals = MathTex(r"\theta = arcsin(\sqrt{k/N})\\k=1\\N=2") 
        
        # angle 3
        angle3 = Angle(arrowAP, arrowAPP, radius = 1.5)
        theta3 = MathTex(r"2\theta").next_to(angle3).shift([-0.2, 0.75, 0])
        
        
        
        
        

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
        #angle 1
        self.add(angle, theta)
        self.play(Create(angle), Create(theta))
        self.wait()
        
        #equals
        self.add(equals.to_edge(UR))
        self.play(Create(equals))
        
        #transformation 1
        self.add(ghostArrowA.add_tip())
        self.play(Transform(mobject = arrowA, target_mobject = arrowAP))
        
        
        #angle 2
        self.add(angle2, theta2)
        self.play(Create(angle2), Create(theta2))
        
        #vector a'
        self.add(ghostArrowAP.add_tip())
        #self.add(arrowAP)
        self.add(ap_label)
        #self.play(Create(arrowAP))
        self.play(FadeIn(ap_label))
        self.wait()
       
        #transformation 2
      
        self.play(Transform(mobject = arrowA, target_mobject = arrowAPP))
        self.add(app_label)
        self.wait()

        #angle 3
        self.add(angle3, theta3)
        self.play(Create(angle3), Create(theta3))
        self.wait()
        
        #self.play(Rotate(mobject = arrowAP, axis = np.array([-5,2,0]), about_point = (-5,0,0), angle=1))
        
        
        
        
        