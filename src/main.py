#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Iágson Carlos Lima Silva on Tuesday, August 15, 2023.
# Copyright (c) 2023 @iagsoncarlos. All rights reserved.

__author__      = 'Iágson Carlos Lima Silva'
__copyright__   = 'Copyright (c) 2023 @iagsoncarlos'


import sys

from PyQt5.QtWidgets import QApplication

from interface.gui import PyCGUI


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PyCGUI()
    window.show()

    sys.exit(app.exec_())