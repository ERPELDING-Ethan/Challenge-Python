# script pion.py
'''Pas d'import de module, cela me parrait louche'''

def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'z':
        PosY -= 20
    # déplacement vers le bas
    '''Remplir'''
    # déplacement vers la droite
    '''Remplir'''

    # déplacement vers la gauche
    '''Remplir'''

    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion,PosX -10, PosY -10, PosX +10, PosY +10)

# Création de la fenêtre principale
'''Il faut créer la fenètre principale'''

# position initiale du pion
PosX = 230
PosY = 150

# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
for i in range (30):
    Canevas.create_line(0,20*i,480,20*i)
    Canevas.create_line(20*i,0,20*i,320)
Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='black',fill='red')
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.pack(padx =5, pady =5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

Mafenetre.mainloop()
