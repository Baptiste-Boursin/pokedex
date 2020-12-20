import sys

from PyQt5.QtWidgets import QApplication
from api.pokemon import find_pokemon_by_range
from ui.mainWindow import MainWindow


pokemon_first_gen = [0, 151]

listPokemon = find_pokemon_by_range(*pokemon_first_gen)
app = QApplication(sys.argv)
mw = MainWindow(listPokemon)

sys.exit(app.exec_())