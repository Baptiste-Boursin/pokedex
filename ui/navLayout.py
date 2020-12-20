from PyQt5.QtWidgets import QWidget,QPushButton, QGridLayout,QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

from api.pokemon import find_pokemon_by_id, find_pokemon_by_name

"""
    Classe NavLayout sert a mettre en place l'affichage des boutons de navigation
    du pokedex
"""
class NavLayout(QWidget):

    def __init__(self, liste, callback, index = 0) :
        super().__init__()
        self.liste = liste
        self.index = index
        self.callback = callback

        # Barre de recherche
        self.search = QLineEdit()
        self.search.setMaximumWidth(400)
        self.btnSearch = QPushButton('Search')
        self.btnSearch.resize(200,80)
        self.btnSearch.clicked.connect(self.search_click)
        
        # Boutons de navigation entre les Pokémons
        self.btnLeft = QPushButton('←')
        self.btnLeft.clicked.connect(self.previous)
        
        self.btnRight = QPushButton('→')
        self.btnRight.clicked.connect(self.next)

        if self.index == 0:
            self.btnLeft.setEnabled(False)
        
        if self.index == len(self.liste):
            self.btnRight.setEnabled(False)

        layout = QGridLayout()

        layout.addWidget(self.search,1,0)
        layout.addWidget(self.btnSearch,1,1)
        layout.addWidget(self.btnLeft, 0, 0)
        layout.addWidget(self.btnRight, 0, 1)

        self.setLayout(layout)


    # Passer pour pokémon précédent
    def previous(self):
     
        # Si on va vers index 0, on désactive le bouton précédent(btnLeft)
        if self.index == 1 :
            self.index = self.index - 1
            self.callback(self.index)
            self.btnLeft.setEnabled(False)
        # Si on va vers l'index len(liste)-1, on active le bouton suivant(btnRight)
        elif self.index == len(self.liste) -1 :
            self.index = self.index - 1
            self.callback(self.index)
            self.btnRight.setEnabled(True)
        else :
            self.index = self.index - 1
            self.callback(self.index)

            
    # Passer au pokémon suivant
    def next(self):
        
        # si on va vers l'index 1, on active le bouton précédent
        if self.index == 0 :
            self.index = self.index + 1
            self.callback(self.index)
            self.btnLeft.setEnabled(True)
        # Si on arrive au dernier pokémon on désactive le bouton suivant    
        elif self.index == len(self.liste) -2:
            self.index = self.index + 1
            self.callback(self.index)
            self.btnRight.setEnabled(False)
        else :
            self.index = self.index + 1
            self.callback(self.index)

    def search_click(self):
        pkmn_search_value = self.search.text()
        
        pokemon = None
        # recherche par name 
        if pkmn_search_value.isalpha() :
            pokemon = find_pokemon_by_name(pkmn_search_value)
        # recherche par id
        elif pkmn_search_value.isnumeric() :
            pokemon = find_pokemon_by_id(pkmn_search_value)

        if not pokemon:
            QMessageBox.about(self, "Attention !", "Ce Pokémon n'existe pas")
            return

        self.index = [pkmn.get('id') for pkmn in self.liste].index(pokemon.id)

        self.callback(self.index)
        if self.index == 0:
            self.btnLeft.setEnabled(False)
        else :
            self.btnLeft.setEnabled(True)
    
        if self.index == len(self.liste)-1:
            self.btnRight.setEnabled(False)
        else :
            self.btnRight.setEnabled(True)
