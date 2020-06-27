from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
import PyQt5.QtCore

class Tile():
    def __init__(self, controlled, position, button):
        self.controlled = controlled
        self.position = position
        self.btn = button

        self._style_selected = "border-color: blue;" "background-color: rgb(170, 170, 15);"
        self._style_deselected = "border-color: black; background-color: rgb(120, 120, 120);"
        self._style_movable = "border-color: black; background-color: rgb(0, 250, 45);"
        self._style_attackable = "border-color: black; background-color: rgb(250, 0, 0);"

        self.icon_comp = QIcon('D:/Development/Independent_Projects/Python/hexapawn/python_hexapawn/icons/pawn_black.png')
        self.icon_player = QIcon('D:/Development/Independent_Projects/Python/hexapawn/python_hexapawn/icons/pawn_white.png')
        self.icon_blank = QIcon()
    # __init__ end

    def change_control(self, new_controlled):
        self.controlled = new_controlled
        self.change_icon()
    # change_control end

    def change_icon(self):
        if (self.controlled == -1): # if controlled by computer
            self.btn.setIcon(self.icon_comp)
        elif(self.controlled == 1): # if controlled by player
            self.btn.setIcon(self.icon_player)
        else:
            self.btn.setIcon(self.icon_blank)
        # if end
    # change_icon end

    def get_pos(self):
        return self.position
    # get_pos end

    def get_controlled(self):
        return self.controlled
    # get_controlled end

    def is_attackable(self, attacker):
        attacker_pos = attacker.get_pos()
        attackableR = attacker_pos == self.position + 2 
        attackableL = attacker_pos == self.position + 4
        attackable = attackableL or attackableR
        print(attackableL, attackableR)
        if (self.controlled == -1 and attackable): return True
        else: return False
    # is_attackable end

    def is_movable(self, mover):
        mover_pos = mover.get_pos()
        movable = mover_pos == self.position + 3
        if (self.controlled == 0 and movable): return True
        else: return False
    # is_movable end

    def style_button(self, style):
        self.btn.setStyleSheet(style)
    # style_selected end

    def __str__(self):
        return 'Position %s Controlled by:%s'%(self.position, self.controlled)
    # __str__ end
# class end