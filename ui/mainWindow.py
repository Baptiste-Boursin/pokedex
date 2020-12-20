import requests

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QStatusBar, QAction, qApp, QMainWindow, QLineEdit,QComboBox
from PyQt5.QtGui import QIcon,QPixmap

from ui.pokemonDisplay import AffichagePokemon
from ui.navLayout import NavLayout
from ui.teamLayout import TeamLayout
from api.pokemon import find_pokemon_by_id


"""
    Classe MainWindow mettant en place tout les élements à afficher ainsi que les paramètres de la fenetre en elle même
"""
class MainWindow(QMainWindow):
    def __init__(self,liste):
        super().__init__()
        self.liste = liste
        self.current_pokemon= find_pokemon_by_id(self.liste[0].get('id'))
        self.displayPokemon = AffichagePokemon(self.current_pokemon)
        self.width = 800
        self.height = 800
        
        self.UI()

    #fonction appelée par le navLayout pour modifier l'index 
    def navigation(self, index):
        if index < len(self.liste) and index >= 0:
            self.current_pokemon = find_pokemon_by_id(self.liste[index].get('id'))
            self.displayPokemon.update_UI(self.current_pokemon)
            
    #fonction appelée par TeamLayout pour récupérer le nom du pokémon courrant
    def callback_get_current_pokemon_name(self):
        return self.current_pokemon.name

    def UI(self):

        # Création des grid layout
        mainGridLayout = QGridLayout()
        #mainGridLayout.setGeometry(0,0,400,400)
        rightGridLayout = QGridLayout()
       
        # Ajout de l'affichage pokemon dans la partie en bas à droite
        rightGridLayout.addWidget(self.displayPokemon,0,0)
        rightGridLayout.addWidget(NavLayout(self.liste,self.navigation),1,0)
           
        
        # Ajout d'un grid layout dans le main layout pour diviser la partie droite du layout principal en deux
        mainGridLayout.addLayout(rightGridLayout,0,1)

        # Ajout de l'affichage de l'équipe dans la partie gauche du mainGridLayout
        mainGridLayout.addWidget(TeamLayout(self.callback_get_current_pokemon_name),0,2)

        # Fonction quitter pour fermer l'application
        exitAct = QAction(QIcon('images/exit.jpg'),'Quitter',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Quitter l'application")
        exitAct.triggered.connect(qApp.quit)

        # Ajout d'un menu 'Quitter' qui permet 
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Quitter')
        fileMenu.addAction(exitAct)

        widget = QWidget()
        widget.setLayout(mainGridLayout)

        self.setCentralWidget(widget)
        self.setGeometry(300,300,800,500)
        self.setWindowTitle('Pokedex')
        self.show()