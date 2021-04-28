# Conoway's Game of Life (MVC implementation)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Overview
The Game of Life was invented in 1970 by the British mathematician John Horton Conway.

This is the [original article](http://ddi.cs.uni-potsdam.de/HyFISCH/Produzieren/lis_projekt/proj_gamelife/ConwayScientificAmerican.htm) of Game of Life with the relative [community](https://www.conwaylife.com/). 

The main focus on this implementation is on familiarizing with MVC pattern below.

<img src="https://github.com/iacopoerpichini/ConowayGameOfLife/blob/master/img/mvc.png">

### Game of Life rules 
The game is played on a two-dimensional board implemented with a numpy array.

Each grid location is either empty or populated by a single cell. A location’s neighbors are any cells in the surrounding eight adjacent locations. 

The simulation of starts from an initial state of populated locations and then progresses through time.

The evolution of the board state is governed by a few simple rules:

  1. Each populated location with one or zero neighbors dies (from loneliness).
  2. Each populated location with four or more neighbors dies (from overpopulation).
  3. Each populated location with two or three neighbors survives.
  4. Each unpopulated location that becomes populated if it has exactly three populated neighbors.
  5. All updates are performed simultaneously in parallel.
  
This figure illustrates the rules for cell death, survival, and birth:

<img src="https://github.com/iacopoerpichini/ConowayGameOfLife/blob/master/img/rules.PNG">



### Features
My implementation of Game of Life application have the following features:
  
  1. A visual simulation displayed on a square black board with fixed size 50x50px.
  2. Start/pause/clear/singleStep buttons that allowed users to run the simulation.
  3. Drawing/editing of state on the board with the left click of the mouse. If users click on the board set to alive/death a single cell and is possible to hold the click and drag the mouse for drawing.
  4. A slider that allow to set the speed of the simulation when is not running.
  5. A menu bar with load/save function for board.

### Simulation

![Alt Text](https://github.com/iacopoerpichini/ConowayGameOfLife/blob/master/img/simulation.gif)

### Directories Layout

```bash
├── gui                 # Contain the user interface generated with QtDesigner
│   ├── ...             # and python code generated with PyUiC (main window and two dialog)  
├── img                 # Some image for readme
│   ├── ... 
├── mvc                 # The core of the project that uses mvc
│   ├── boardGol.py     # A custom widget for edit the game of life board
│   ├── controller.py   # The controller that have the view and the model
│   ├── model.py        # Raw data gestion
│   ├── view.py         # The connection with elements in the view with model
├── pattern             # Fome pattern found on-line for test the simulation
│   ├── ... 
├── README.md
├── gol.py              # File for run the application (main)
├── requirements.txt
```

### Requirements
The project is developed with PyCharm and i found an interesting [guide](https://pythonpyqt.com/how-to-install-pyqt5-in-pycharm/) for integrate QTdesigner and PyUIC in the ide.

The following version of libraries are used:

| Software   | Version           |
| -----------|-------------------|
| **Python** | tested on v3.6    | 
| **PyQT5**  | tested on v5.15.2 |
| **Numpy**  | tested on v1.19.2 |

### Usage
After installation of requirements [download](https://github.com/iacopoerpichini/ConowayGameOfLife.git) the project and run it in a terminal.

```sh
$ cd ConowayGameOfLife
$ python gol.py
```

Is possible to start the simulation via command line and chose a grid dimension, the grid is 50x50px by default.

Note: the grid is always a square grid. 

Example: (-s is gridSize variable in gol.py)

```sh
$ python gol.py -s 20
```
This start a simulation with a grid 20x20 px, if you load a saved pattern in other dimension the grid size change according to the pattern loaded.

