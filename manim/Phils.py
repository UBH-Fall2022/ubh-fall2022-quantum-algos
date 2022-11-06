from manim import *

class Phil(Scene):
    def construct(self):
        a = Text("Phil's Algorithm")
        self.add(a)
        self.play(Write(a))
        self.wait()
        self.play(Uncreate(a))
        self.wait()
        
        b = MathTex(r"\vec{a_0} = \left[{\begin{array}{cc} 1 \\ 0 \\ \end{array}} \right]")
        
        self.add(b)
        self.play(Create(b))
        self.wait()
        
        translate = ApplyMethod(b.shift, UP)
        self.play(translate)

        c = MathTex(r"H_2 = \frac{1}{\sqrt{2}} \left({\begin{array}{cc} 1 & 1 \\ 1 & -1 \\ \end{array}} \right)").next_to(b, DOWN)
        self.add(c)
        self.play(Create(c))
        self.wait() 

        translate2 = [ApplyMethod(t.shift, UP) for t in [b,c]]        
        self.play(*translate2)
      
        d = MathTex(r"\vec{a_1} = H_2\vec{a_0}", color=BLUE).next_to(c, DOWN)
        self.add(d)
        self.play(Create(d))
        self.wait()
     
        translate3 = [ApplyMethod(t.shift, UP) for t in [b,c, d]]        
        self.play(*translate3)     
        
        e = MathTex(r"\vec{a_1} = \frac{1}{\sqrt{2}} \left({\begin{array}{cc} 1 & 1 \\ 1 & -1 \\ \end{array}} \right) \left[{\begin{array}{cc} 1 \\ 0 \\ \end{array}} \right]").next_to(d, DOWN)
        self.add(e)
        self.play(Create(e))
        self.wait()
        
        f = MathTex(r"\vec{a_1} = \frac{1}{\sqrt{2}} \left[{\begin{array}{cc} 1 \\ 1 \\ \end{array}} \right]").next_to(e, DOWN)
        #self.add(f)
        self.play(Transform(mobject=e, target_mobject=f))
        self.play(ApplyMethod(e.next_to, d, DOWN))


        self.wait()        

        
        
  
        
        
        
        
        
        
        #translate = ApplyMethod(b.shift, UP)
        #self.play(translate)
        
        
        