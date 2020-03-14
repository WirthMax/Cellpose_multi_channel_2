from PyQt5 import QtGui, QtCore, Qt, QtWidgets

from . import io

def mainmenu(parent):
    main_menu = parent.menuBar()
    file_menu = main_menu.addMenu("&File")
    # load processed data
    loadImg = QtGui.QAction("&Load image (*.tif, *.png, *.jpg)", parent)
    loadImg.setShortcut("Ctrl+L")
    loadImg.triggered.connect(lambda: io.load_image(parent))
    file_menu.addAction(loadImg)

    parent.loadMasks = QtGui.QAction("Load &masks (*.tif, *.png, *.jpg)", parent)
    parent.loadMasks.setShortcut("Ctrl+M")
    parent.loadMasks.triggered.connect(lambda: io.load_masks(parent))
    file_menu.addAction(parent.loadMasks)
    parent.loadMasks.setEnabled(False)

    loadManual = QtGui.QAction("Load &processed/labelled image (*_seg.npy)", parent)
    loadManual.setShortcut("Ctrl+P")
    loadManual.triggered.connect(lambda: io.load_manual(parent))
    file_menu.addAction(loadManual)

    #loadStack = QtGui.QAction("Load &numpy z-stack (*.npy nimgs x nchan x pixels x pixels)", parent)
    #loadStack.setShortcut("Ctrl+N")
    #loadStack.triggered.connect(lambda: parent.load_zstack(None))
    #file_menu.addAction(loadStack)

    parent.saveSet = QtGui.QAction("&Save masks and images (as *.npy)", parent)
    parent.saveSet.setShortcut("Ctrl+S")
    parent.saveSet.triggered.connect(lambda: io.save_sets(parent))
    file_menu.addAction(parent.saveSet)
    parent.saveSet.setEnabled(False)

    parent.savePNG = QtGui.QAction("Save masks as P&NG", parent)
    parent.savePNG.setShortcut("Ctrl+N")
    parent.savePNG.triggered.connect(lambda: io.save_png(parent))
    file_menu.addAction(parent.savePNG)
    parent.savePNG.setEnabled(False)

    parent.saveServer = QtGui.QAction("Send manually labelled data to server", parent)
    parent.saveServer.triggered.connect(lambda: io.save_server(parent))
    file_menu.addAction(parent.saveServer)
    parent.saveServer.setEnabled(False)

def editmenu(parent):
    main_menu = parent.menuBar()
    edit_menu = main_menu.addMenu("&Edit")
    parent.undo = QtGui.QAction('Undo previous mask/trace', parent)
    parent.undo.setShortcut("Ctrl+Z")
    parent.undo.triggered.connect(parent.undo_action)
    parent.undo.setEnabled(False)
    edit_menu.addAction(parent.undo)

    parent.ClearButton = QtGui.QAction('Clear all masks', parent)
    parent.ClearButton.setShortcut("Ctrl+0")
    parent.ClearButton.triggered.connect(parent.clear_all)
    parent.ClearButton.setEnabled(False)
    edit_menu.addAction(parent.ClearButton)

    parent.remcell = QtGui.QAction('Remove selected cell (Ctrl+CLICK)', parent)
    parent.remcell.setShortcut("Ctrl+Click")
    parent.remcell.triggered.connect(parent.remove_action)
    parent.remcell.setEnabled(False)
    edit_menu.addAction(parent.remcell)

def helpmenu(parent):
    main_menu = parent.menuBar()
    help_menu = main_menu.addMenu("&Help")
    openHelp = QtGui.QAction("&Help window", parent)
    openHelp.setShortcut("Ctrl+H")
    openHelp.triggered.connect(parent.help_window)
    help_menu.addAction(openHelp)