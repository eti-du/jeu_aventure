
"""
Programme réalisé par Duroy, Etienne, 1G1
"""
import pygame
pygame.init()#initialisation graphique
fenetre = pygame.display.set_mode((1280, 820), flags=pygame.RESIZABLE|pygame.SCALED)
pygame.display.set_caption("| Jeu d'aventure |")
font = pygame.font.Font('freesansbold.ttf', 20)
fenetre.blit(font.render("... CHARGEMENT ...", True, (245, 215, 20)),(500,370))
pygame.display.flip()
image1 = pygame.image.load("vestibule.jpg")
image2 = pygame.image.load("salle-a-manger.jpg")
image3 = pygame.image.load("cuisine.jpg")
image4 = pygame.image.load("chambre.jpg")
image5 = pygame.image.load("salon.jpg")
image6 = pygame.image.load("grenier.jpg")
imageclef = pygame.image.load("clef3.png")
imagefin  = pygame.image.load("piecevide.jpg")
textimpo = font.render("Déplacement impossible", True, (245, 15, 10))
textclef = font.render("La clef se trouve ici, dans cette pièce, maintenant il faut aller ouvrir la porte", True, (245, 25, 110))
textporteferme = font.render("Il faut d'abord trouver la clef pour pouvoir entrer", True, (245, 15, 10))

cleftrouve = False
x = 10
y = 10
actuelsalle = "salle" + str(x) + '_' + str(y)
class salles:
    '''La liste des salles'''
    def __init__(self,nom,porten,portee,portes,porteo,x,y,image):
        self.portenord  = porten
        self.porteest   = portee
        self.portesud   = portes
        self.porteouest = porteo
        self.nom = nom
        self.x = x
        self.y = y
        self.image = image
        self.clef = False
        #self.text = text
    def texte(self):
        return font.render("Vous vous trouvez dans " + self.nom + ".", True, (0, 255, 0))
    def contientclef(self):
        self.clef = True

#création des salles
salle10_10 = salles('le vestibule',False,False,True,True,0,0,image1)
salle10_8 = salles('la salle à manger',True,False,False,True,0,1,image2)
salle9_8 = salles('la cuisine',False,True,False,True,1,1,image3)
salle9_9 = salles('la 2ème chambre',False,True,False,False,1,1,image4)
salle9_10 = salles('la 1re chambre',False,True,False,False,1,1,image4)
salle10_9 = salles('le salon',True,False,True,True,1,1,image5)
salle8_8 = salles('le grenier',False,True,False,False,1,1,image6)
salle7_8 = salles('du trésor',False,True,False,False,1,1,imagefin)
salle9_10.contientclef() #défini quel salle contient la clef

def decrireLaPiece():
    global cleftrouve
    fenetre.fill((55,55,55))#remplir la fenetre de gris
    fenetre.blit(eval(actuelsalle).image,(0,0))#afficher l'image à la prochaine actualisation
    fenetre.blit(eval(actuelsalle).texte(),(0,740))#afficher le texte à la prochaine actualisation
    if eval(actuelsalle).clef == True:
        fenetre.blit(imageclef,(350,265))
        fenetre.blit(textclef,(0,800))
        cleftrouve = True
    pygame.display.flip()# Actualisation de l'affichage


def decision(direction):
    global piece,x,y,actuelsalle 
    def deplacementimpossible():
        global cleftrouve,actuelsalle,x
        if eval(actuelsalle).nom == 'le grenier':
            if cleftrouve == False:
                fenetre.blit(textporteferme,(0,800))
                pygame.display.flip()
            else:
                x -= 1
                deplacementpossible()
        else:
            fenetre.blit(textimpo,(0,760))
            pygame.display.flip()
    def deplacementpossible():
        global x,y,actuelsalle
        actuelsalle = "salle" + str(x) + '_' + str(y)
        decrireLaPiece()
    #flèche haut : le personnage désire aller au nord
    if direction==pygame.K_UP:
        if eval(actuelsalle).portenord == True:
            y += 1
            deplacementpossible()
        else:
            deplacementimpossible()
    #flèche bas : le personnage désire aller au sud
    elif direction==pygame.K_DOWN:
        if eval(actuelsalle).portesud == True:
            y -= 1
            deplacementpossible()
        else:
            deplacementimpossible()
    #flèche droite : le personnage désire aller à l'est
    elif direction==pygame.K_RIGHT:
        if eval(actuelsalle).porteest == True:
            x += 1
            deplacementpossible()
        else:
            deplacementimpossible()
    #flèche gauche : le personnage désire aller à l'ouest
    elif direction==pygame.K_LEFT:
        if eval(actuelsalle).porteouest == True:
            x -= 1
            deplacementpossible()
        else:
            deplacementimpossible()
    else:
        deplacementimpossible()



decrireLaPiece()
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False#fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:#lecture du clavier
            piece = decision(event.key)#event remplacé par "event.type"
            if event.key == pygame.K_ESCAPE or event.unicode == 'w':
                loop = False#espace ou la touche w pour quitter
pygame.quit()



