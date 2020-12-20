from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QLineEdit, QLabel
from PyQt5.QtCore import Qt

from api.pokemon import find_pokemon_by_id
from models.pokemon import Pokemon

"""
    Classe TeamLayout sert à afficher l'équipe pokemons
    sur la mainwindow.
"""
class TeamLayout(QWidget) :
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.team = []
        self.listWidget = []
        self.ui()
    """ 
        Mise en place des différents widgets dans un grid layout
    """
    def ui(self) :
        listLayout = QGridLayout()
        labelTitle = QLabel("Equipe pokémon :")
        listLayout.addWidget(labelTitle,0,0)
        """
            On boucle sur la listWidget pour instancier les ItemTeam qui compose le TeamLayout
        """
        for i in range(0,5):
            self.listWidget.append(ItemTeam(self.callback))
            listLayout.addWidget(self.listWidget[i], i+1,0)
        self.setLayout(listLayout)
        
"""
    Classe ItemTeam implementant le layout d'un pokemon de l'équipe
"""
class ItemTeam(QWidget) :
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.name = ""
        self.ui()

    def ui(self) :
        itemLayout = QGridLayout()
        
        self.labelName = QLabel(str(self.name))

        """
            Definition des boutons supprimer et ajouter
        """
        self.btnDelete = QPushButton("x")
        self.btnDelete.clicked.connect(self.delete)
        
        self.btnAdd = QPushButton("+")
        self.btnAdd.clicked.connect(self.add)

        itemLayout.addWidget(self.labelName, 0,0)
        itemLayout.addWidget(self.btnDelete, 0,1)
        itemLayout.addWidget(self.btnAdd, 0,2)
        self.btnDelete.setEnabled(False)
        self.setLayout(itemLayout)
        
    """
        Fonction add ajoutant le pokemon sur l'item
    """
    def add(self) :
        self.name = self.callback()
        self.btnDelete.setEnabled(True)
        self.update()

    """
        Fonction delete supprimant le pokemon de l'item
    """
    def delete(self) :
        self.name = ""
        self.btnDelete.setEnabled(False)
        self.update()

    """
        Fonction update mettant a jour le label name d'item
    """
    def update(self) :
        self.labelName.setText(self.name)

