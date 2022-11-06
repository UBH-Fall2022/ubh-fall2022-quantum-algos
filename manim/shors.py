from manim import *

class shors(Scene):
    def construct(self):
        
        Tit = Text("Shor's Algorithm", color=BLUE)
        self.add(Tit)
        self.play(Create(Tit))
        self.wait(3)     

        self.play(Uncreate(Tit))
        
        a = Text("Classical Steps:")
        #The horse does not eat cucumber salad
        
        self.add(a.to_edge(UP))
        self.play(Create(a))
        self.wait()
        
        b = Text("1: Choose number 'N' to be factored", color=BLUE).next_to(a, DOWN)
    
        self.add(b)
        self.play(Create(b))
        self.wait()

        
        d = Text("2: Choose a random number 'a'\nsuch that a < N", color=BLUE).next_to(b, DOWN)
        d.align_to(b, LEFT)
        
        self.add(d)
        self.play(Create(d))
        self.wait()


        f = Text("3: Compute GCD(a, N)", color=BLUE).next_to(d, DOWN)
        f.align_to(d, LEFT)   
        
        self.add(f)
        self.play(Create(f))
        self.wait()
        
        
        h = Text("Is GCD = 1 ?", color=BLUE).next_to(f,DOWN)
        self.add(h)
        self.play(Create(h))
        self.wait()
        
        i = Text("If not, we're done! We found a factor of N", color=ORANGE).next_to(h, DOWN)
        i.align_to(f, LEFT)   

        self.add(i)
        self.play(Create(i))
        self.wait()
       
        j = Text("Otherwise, Perform period-finding routine\n(Quantum Step)", color=BLUE).next_to(i, DOWN)
        j.align_to(i, LEFT)   

        self.add(j)
        self.play(Create(j))
        self.wait()
        
        self.play(Uncreate(a),Uncreate(b),Uncreate(d),Uncreate(f))        
        self.play(Uncreate(h),Uncreate(i))        
        self.wait()
 
        k = Text("Quantum Steps:", color=BLUE).next_to(i, DOWN)

        self.play(Transform(mobject=j, target_mobject=k))
    
        sl = ApplyMethod(j.to_edge, UP)
        self.play(sl)
        self.wait()
        
        v = MathTex(r"f(x)=a^{x} mod N").next_to(j, DOWN)
       
        self.add(v)
        self.play(Create(v))
        self.wait()
        
        lw = Text("Find the smallest integer r\nsuch that f(x+r) = f(x)", color=BLUE).next_to(v, DOWN)
      
        self.add(lw)
        self.play(Create(lw))
        self.wait() 
 
        
        l = Text("Initialize a pair of qubit registers to").next_to(lw, DOWN)
        l.align_to(LEFT)
        
        self.add(l)
        self.play(Create(l))
        
        l2 = MathTex(r"\frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle |0\rangle").next_to(l, DOWN)
        
        self.add(l2)
        self.play(Create(l2))
        self.wait()  
        
        self.play(Uncreate(l), Uncreate(lw))

        self.play(ApplyMethod(l2.next_to, v, DOWN))



        tr = Text("f(x) is then constructed as a quantum function\nand applied to our initial state").next_to(l2, DOWN)
        
        self.add(tr)
        self.play(Write(tr))     
        
        
        ld = MathTex(r"\frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle |f(x)\rangle").next_to(tr, DOWN)
        
        self.add(ld)
        self.play(Create(ld))
        self.wait()    

        self.play(Uncreate(tr))
        self.play(ApplyMethod(ld.next_to, l2, DOWN))
        self.wait()
        
        
        q = Text("Then perform Quantum Fourier Transform on the input:").next_to(ld, DOWN)
        self.add(q)
        self.play(Create(q))
        
        op = MathTex(r"U_{QFT} |x\rangle = \frac{1}{\sqrt{N}} \sum_{y}e^{2\pi ixy/N} |y\rangle").next_to(q, DOWN)
        
        self.add(op)
        self.play(Create(op))
        self.wait()     

        self.play(Uncreate(q))
        self.play(ApplyMethod(op.next_to, ld, DOWN))
        self.wait()    

        re = Text("The resulting state...").next_to(op, DOWN)
        self.add(re)
        self.play(Create(re))
        self.wait()
        
        self.play(Uncreate(op),Uncreate(ld),Uncreate(l2))        
        
        
        ef = MathTex(r"\frac{1}{N} \sum_{x}\sum_{y} e^{2\pi ixy/N} |y\rangle |f(x)\rangle").next_to(v, DOWN)
         
        self.add(ef)
        self.play(Create(ef), Uncreate(re)) 
        self.wait()   
        
        po = Text("Reduce y/N and take the denominator as the guess for r", font_size=36).next_to(ef, DOWN)
        self.add(po)
        self.play(Create(po)) 
        self.wait()

        sfg = Text("If f(x) = f(x + r) then we have found a valid r and we're done!", font_size=36, color=ORANGE).next_to(po,DOWN)
        fff = Text("Else, try some multiples of r.\nIf this doesn't work, repeat the quantum process", font_size=36).next_to(sfg, DOWN)
        self.add(sfg)
        self.add(fff)
        self.play(Create(sfg), Create(fff)) 
        self.wait(5)        
        