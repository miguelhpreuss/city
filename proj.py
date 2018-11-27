#Projeto Final de Python
#Miguel Hellmann Preuss e Thiago Sales
from turtle import*
from random import*
from time import*

#variaveis iniciais
d1,d2,d3,d4,d5=500,500,500,500,500 #dinheiro inicial
g1,g2,g3,g4,g5=100,80,60,40,20     #combustivel inicial
posto=200                          #combustivel no posto
consumo=0.01                       #consumo de combustivel por loop
velocidade=1                   #velocidade dos carros
pt1,pt2,pt3,pt4,pt5=(55,10),(85,10),(140,10),(55,110),(115,110)#ponto de estacionamentos
cde=0                              #verificador de estacionados(cde=contador de estacionados)
precoCombustivel=2#preço do combustivel
tempo=time()


#rotina de posição inicial das tarts
def posTart(t,x,y,ang):  
    t.hideturtle() #esconde tartaruga
    t.speed(0)     #velocidade 0(mais rapida)
    t.pu()         #faz com que a turtle não desenhe
    t.goto(x,y)    #define a posição
    t.showturtle() #a tartaruga reaparece (o inverso do hideturtle) 
    t.seth(ang)    #define o angulo inicial (0=leste,90=norte,180=oeste,270=sul)


#rotina para curvas do carro
def carroCurvas(t,gasolina):
    if t.pos()==(50,-200) or t.pos()==(250,-75):
        t.seth(90) #norte
    if t.pos()==(250,200) or t.pos()==(-50,75):
        t.seth(180)#oeste
    if t.pos()==(-250,75) or t.pos()==(-50,200):
        t.seth(270)#sul
    if t.pos()==(-250,-200) or t.pos()==(50,-75):
        t.seth(0)#leste
    if t.pos()==(-50,150) and (gasolina<20):#entra no posto
        t.seth(180)


#rotina para estacionar
def estacionar(t,dinheiro):
    global cde
    if (cde==0) and (dinheiro<200):
        if t.pos()==(55,-75):
            t.seth(90)
            cde=cde+1
    if (cde==1) and (dinheiro<200):
        if t.pos()==(85,-75):
            t.seth(90)
            cde=cde+1
    if (cde==2) and (dinheiro<200):
        if t.pos()==(140,-75):
            t.seth(90)
            cde=cde+1
    if (cde==3) and (dinheiro<200):
        if t.pos()==(55,200):
            t.seth(270)
            cde=cde+1
    if (cde==4) and (dinheiro<200):
        if t.pos()==(115,200):
            t.seth(270)
            cde=cde+1


#rotina para andar
def CarroAndar(t):
    if t.pos()!=pt1 and t.pos()!=pt2 and t.pos()!=pt3 and t.pos()!=pt4 and t.pos()!=pt5:
        t.fd(velocidade)


#rotina para mudar de shape conforme a direção e nível do combutível
def shapeCombustivel(t,gasolina):
    x,y=t.pos()
    CarroAndar(t)
    xa,ya=t.pos()
    if xa>x:
        if gasolina<20:
            t.shape("carroVermelhoDireita.gif")
        if 20<=gasolina<=50:
            t.shape("carroAmareloDireita.gif")
        if gasolina>50:
            t.shape("carroVerdeDireita.gif")
    if xa<x:
        if gasolina<20:
            t.shape("carroVermelhoEsquerda.gif")
        if 20<=gasolina<=50:
            t.shape("carroAmareloEsquerda.gif")
        if gasolina>50:
            t.shape("carroVerdeEsquerda.gif")
    if ya<y:
        if gasolina<20:
            t.shape("carroVermelhoBaixo.gif")
        if 20<=gasolina<=50:
            t.shape("carroAmareloBaixo.gif")
        if gasolina>50:
            t.shape("carroVerdeBaixo.gif")
    if ya>y:
        if gasolina<20:
            t.shape("carroVermelhoCima.gif")
        if 20<=gasolina<=50:
            t.shape("carroAmareloCima.gif")
        if gasolina>50:
            t.shape("carroVerdeCima.gif")


#mudar shape de caminhão conforme direção
def caminhaoShape():
    global posto
    x,y=c.pos()
    if posto<300:
        c.fd(velocidade)
    if posto>=300 and c.pos()!=(160,-225):
        c.fd(velocidade)
    xa,ya=c.pos()
    if xa>x:
        c.shape("caminhaoD.gif")
    if xa<x:
        c.shape("caminhaoE.gif")
    if ya>y:
        c.shape("caminhao.gif")
    if ya<y:
        c.shape("caminhaoB.gif")


#rotina com todas as rotinas do carro agrupadas
def Carro(t,gasolina,dinheiro):
    carroCurvas(t,gasolina)
    estacionar(t,dinheiro)
    shapeCombustivel(t,gasolina)


#rotina para o caminhao tanque
def Caminhao():
    global posto
    caminhaoShape()
    if c.pos()==(250,-225):
        c.seth(90) #norte
    if c.pos()==(250,200):
        c.seth(180)#oeste
    if c.pos()==(-50,150):
        c.seth(180)
    if c.pos()==(-50,200):
        c.seth(270)#sul
    if c.pos()==(50,-75) or c.pos()==(-250,-225):
        c.seth(0)#leste
    if c.pos()==(-250,150):
        posto=1000
        p.clear()
        p.write(posto/10,font=("times",20,"normal"))
        c.seth(270)


#cria todos os shapes personalizados
screen=Screen()
shapes=["cidade.gif","carroVerdeCima.gif","carroVerdeBaixo.gif","carroVerdeEsquerda.gif","carroVerdeDireita.gif","carroVermelhoCima.gif",
        "carroVermelhoBaixo.gif","carroVermelhoEsquerda.gif","carroVermelhoDireita.gif","carroAmareloCima.gif","carroAmareloBaixo.gif",
        "carroAmareloEsquerda.gif","carroAmareloDireita.gif","caminhao.gif","caminhaoE.gif","caminhaoB.gif","caminhaoD.gif"]
for x in shapes:
    screen.addshape(x) 


#cria todas as turtles
city=Turtle() #cenario
t1=Turtle()   #carro1
t2=Turtle()   #2
t3=Turtle()   #3
t4=Turtle()   #4
t5=Turtle()   #5
c=Turtle()    #caminhao tanque
p=Turtle()    #contador do posto


#define o cenario
city.shape("cidade.gif")


#usando a rotina para posicionar
posTart(t1,-200,-200,0) 
posTart(t2,100,200,180)
posTart(t3,-250,0,270) #tartaruga 3 começa na posição x=-250 e y=0 e virada pro sul
posTart(t4,-150,75,180)
posTart(t5,250,0,90)
posTart(c,160,-225,0)


#contador inicial de gasolina do posto
p.hideturtle()
p.pu()
p.goto(-280,170)
p.write(posto/10,font=("times",20,"normal"))


#shape caminhao
c.shape("caminhaoD.gif")


#loop infinito
while True:
    delay(1)
    if (time()-tempo)>5:
        print("c1: c2: c3: c4: c5:")
        print(d1,d2,d3,d4,d5)
        tempo=time()
    Carro(t1,g1,d1)
    Carro(t2,g2,d2)
    Carro(t3,g3,d3)
    Carro(t4,g4,d4)
    Carro(t5,g5,d5)
    Caminhao()
    g1=g1-consumo
    g2=g2-consumo
    g3=g3-consumo
    g4=g4-consumo
    g5=g5-consumo
    if t1.pos()==(-250,150):
        g1=randint(50,100)
        posto=posto-g1
        d1=d1-(precoCombustivel*g1)
        t1.seth(270)
        p.clear()
        p.write(posto/10,font=("times",20,"normal"))

    if t2.pos()==(-250,150):
        g2=randint(50,100)
        posto=posto-g2
        d2=d2-(precoCombustivel*g2)
        t2.seth(270)
        p.clear()
        p.write(posto/10,font=("times",20,"normal"))

    if t3.pos()==(-250,150):
        g3=randint(50,100)
        posto=posto-g3
        d3=d3-(precoCombustivel*g3)
        t3.seth(270)
        p.clear()
        p.write(posto/10,font=("times",20,"normal"))

    if t4.pos()==(-250,150):
        g4=randint(50,100)
        posto=posto-g4
        d4=d4-(precoCombustivel*g4)
        t4.seth(270)
        p.clear()
        p.write(posto/10,font=("times",20,"normal"))

    if t5.pos()==(-250,150):
        g5=randint(50,100)
        posto=posto-g5
        d5=d5-(precoCombustivel*g5)
        t5.seth(270)
        p.clear()
        p.write(posto/10,font=("times",20,"normal"))


