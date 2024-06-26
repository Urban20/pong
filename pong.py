import pygame

pygame.init()
resol = (900,500)
pantalla = pygame.display.set_mode(resol)
pygame.display.set_caption('PONG, por mati urban')
texto = pygame.font.SysFont('Cooper',30)


#colores--------------------
blanco =(255,255,255)
negro =(0,0,0)
gris_osc =(35, 35, 35)
violeta =(123, 56, 190)
gris_claro =(203, 203, 203 )
#colores----------------------
text_jug1 = texto.render('JUGADOR 1',1,violeta)
text_jug2 = texto.render('JUGADOR 2',1,violeta)

tiempo = pygame.time.Clock()
class Jugador:
    def  __init__(self,coord_x,coord_y,tecla_arriba,tecla_abajo,color):
        self.coordX= coord_x
        self.coordY= coord_y
        self.ancho = 10
        self.largo = 100
        self.color= color
        self.velY=1
        #teclas--------
        self.t_arriba= tecla_arriba
        self.t_abajo = tecla_abajo
        #-------------
    def generar(self):
        jugador_= pygame.draw.rect(pantalla,self.color,(self.coordX,self.coordY,self.ancho,self.largo))
        return jugador_
    def teclado(self,tecla):
        if tecla[self.t_arriba]:
            self.velY += -1.5
            self.coordY += self.velY
        if tecla[self.t_abajo]:
            self.velY += 1.5
            self.coordY += self.velY

    def quieto(self):
        self.velY = 0

    def colisiones(self):
        if self.coordY <= 0:
            self.coordY=0
        if self.coordY >= 372:
            self.coordY=372

class Pelota:
    def __init__(self):
        self.pelotaX= 450
        self.pelotaY= 250
        self.color = violeta
        self.radio= 10
        self.velocidadX=5
        self.velocidadY=5

    def generar(self):
        pelota_= pygame.draw.circle(pantalla,self.color,(self.pelotaX,self.pelotaY),self.radio)
        return pelota_
        
    def movimiento(self):
        self.pelotaX += self.velocidadX
        self.pelotaY += self.velocidadY

    def rebotar(self):
        if self.pelotaY >= 482 or self.pelotaY <= 0:
            self.velocidadX *= 1
            self.velocidadY *= -1
        if self.pelotaX < 0 or self.pelotaX >900:
            self.pelotaX = 450
            self.pelotaY = 250

            self.velocidadX *= -1
            self.velocidadY *= -1
            
        
pelota = Pelota()
jugador1= Jugador(50,50,pygame.K_w,pygame.K_s,gris_claro)
jugador2= Jugador(850,50,pygame.K_UP,pygame.K_DOWN,gris_claro)

contador_1 = 0
contador_2= 0


def puntuacion(puntos):

    score= puntos.render(f'jugador 1: {contador_1} / jugador 2: {contador_2}',1,negro)
    return score


while True:
    try:
        pantalla.fill(gris_osc)
        
        pantalla.blit(text_jug1,(0,0))
        pantalla.blit(text_jug2,(780,0))

        teclas = pygame.key.get_pressed()

        #jugador1----------------
        jugador1.generar()
        jugador1.teclado(teclas)
        jugador1.colisiones()
        #------------------------
        #jugador2----------------
        jugador2.generar()
        jugador2.teclado(teclas)
        jugador2.colisiones()
        #------------------------
        #pelota------------------
        pelota.movimiento()
        pelota.rebotar()
        #------------------------
        
        if pelota.generar().colliderect(jugador1.generar()) or pelota.generar().colliderect(jugador2.generar()):
            pelota.velocidadX *= -1

        if pelota.pelotaX <= 0:
            contador_2 +=1
            
        if pelota.pelotaX >= 900:
            contador_1 +=1
            
        pantalla.blit(puntuacion(texto),(340,0))

        tiempo.tick(60)
        pygame.display.flip()
        eventos = pygame.event.get()
        for even in eventos:
            if even.type == pygame.KEYUP:
                jugador1.quieto()
                jugador2.quieto()
            
            if even.type == pygame.QUIT:
                pygame.quit()
    except pygame.error:
        pass
        
        