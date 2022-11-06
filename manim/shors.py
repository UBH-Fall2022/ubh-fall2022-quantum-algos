from manim import *

class shors(Scene):
    def construct(self):
        a = Text("Classical Steps:")
        #The horse does not eat cucumber salad
        
        self.add(a.to_edge(UP))
        self.play(Create(a))
        self.wait()
        
        b = Text("1: Choose number 'N' to be factored", color=BLUE).next_to(a, DOWN)
        c = Text("Let N = 18").next_to(b, DOWN)
        c.align_to(b, LEFT)
        
        self.add(b)
        self.play(Create(b))
        self.wait()
        self.add(c)
        self.play(Create(c))
        self.wait()
        
        d = Text("2: Choose a random number 'a'\nsuch that a < N", color=BLUE).next_to(c, DOWN)
        d.align_to(c, LEFT)
        
        self.add(d)
        self.play(Create(d))
        self.wait()
        
        e = Text("Let a = 5").next_to(d, DOWN)
        e.align_to(d, LEFT)
        
        self.add(e)
        self.play(Create(e))
        self.wait()
        
        f = Text("3: Compute GCD(a, N)", color=BLUE).next_to(e, DOWN)
        f.align_to(e, LEFT)
        
        
        self.add(f)
        self.play(Create(f))
        self.wait()
        
        g = Text("GCD = 1").next_to(f, DOWN)
        g.align_to(f, LEFT)
        
        self.add(g)
        self.play(Create(g))
        self.wait()
        
        self.play(Uncreate(a),Uncreate(b),Uncreate(d),Uncreate(f))
        translate = [ApplyMethod(t.shift, 1.7*UL) for t in [c,e,g]]        
        translate2 = [ApplyMethod(t.shift, .35*UP) for t in [c,e,g]]
        self.wait()
        
        e.next_to(c, DOWN)
        e.align_to(c, LEFT)
        
        g.next_to(e, DOWN)
        g.align_to(e, LEFT)

        self.play(*translate)        
        self.play(*translate2)
        self.wait()
        
        h = Text("4: Is GCD = 1 ?", color=BLUE)
        self.add(h)
        self.play(Create(h))
        self.wait()
        
        i = Text("YES!", color=ORANGE).next_to(h, DOWN)
        self.add(i)
        self.play(Create(i))
        
        j = Text("∴ Perform period-finding routine\n(Quantum Step)", color=BLUE).next_to(i, DOWN)
        self.add(j)
        self.play(Create(j))
        self.wait()
        
        self.play(Uncreate(h),Uncreate(i))
        
        k = Text("Quantum Steps:", color=BLUE).next_to(i, DOWN)

        self.play(Transform(mobject=j, target_mobject=k))
    
        sl = ApplyMethod(j.to_edge, UP)
        self.play(sl)
        self.wait()
        
        
        #l = Text()
        
        