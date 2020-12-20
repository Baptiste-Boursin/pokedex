# Classe GridLayout
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QLabel, QStatusBar, QAction, qApp, QMainWindow, QLineEdit, QComboBox


# Création de la classe GridLayout
class PokemonDisplay(QWidget):
    def __init__(self, pokemon):
        super().__init__()
        self.pokemon = pokemon

        self.image = QLabel()

        self.numLabel = QLabel("Number :")
        self.nomLabel = QLabel("Name :")
        self.typeLabel = QLabel("Type :")
        self.heightLabel = QLabel("Height :")
        self.weightLabel = QLabel("Weight :")

        self.numValue = QLabel()
        self.nomValue = QLabel()
        self.typeValue = QLabel()
        self.heightValue = QLabel()
        self.weightValue = QLabel()

        self.UI()

    def UI(self):
        self.updateUI(self.pokemon)

        # Initialisation du Layout pour l'affichage des données
        grid = QGridLayout()

        # Ajout des composants dans le Layout
        grid.addWidget(self.numLabel, 0, 0)
        grid.addWidget(self.nomLabel, 1, 0)
        grid.addWidget(self.typeLabel, 2, 0)
        grid.addWidget(self.heightLabel, 3, 0)
        grid.addWidget(self.weightLabel, 4, 0)

        grid.addWidget(self.numValue, 0, 1)
        grid.addWidget(self.nomValue, 1, 1)
        grid.addWidget(self.typeValue, 2, 1)
        grid.addWidget(self.heightValue, 3, 1)
        grid.addWidget(self.weightValue, 4, 1)
        grid.addWidget(self.image, 5, 1)
        self.setLayout(grid)

    # modification de l'affichage du Widget
    def updateUI(self, pokemon):
        self.pokemon = pokemon
        self.nomValue.setText(pokemon.name)
        self.typeValue.setText(', '.join(pokemon.types))
        self.numValue.setText(str(pokemon.id))
        self.heightValue.setText(str(pokemon.height))
        self.weightValue.setText(str(pokemon.weight))

        if os.path.exists('img_pokemon.png'):
            os.remove('img_pokemon.png')

        open('img_pokemon.png', 'wb').write(self.pokemon.image)
        img = QPixmap('img_pokemon.png')
        self.image.setPixmap(img)
