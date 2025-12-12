# Pygame Project by Kirill Konstantinovskii (100005773)
# The game concept
1. Player role:
-	You are an alien controlling a UFO.
2.	Controls:
-	W – move up
-	S – move down
-	A – move left
-	D – move right
-	P – pause menu (or pause button on the screen)
-	Left Mouse Button click – collect planets
3.	Goal of the Game
-	Avoid asteroids to stay alive.
-	Collect planets to earn points.
4.	Object Spawning
-	Asteroids spawn randomly on the right side of the screen and move left.
-	Planets also spawn randomly on the right side and move left.
5.	Health System
-	The player has 3 HP.
-	Getting hit by an asteroid = lose 1 HP.
-	When HP reaches zero → Game Over.
6.	Game mode
-	The game is infinite — it continues as long as you survive.
7.	High Score System
-	The game keeps track of the best score.
-	The high score is saved across all new game runs.

# How to run the game
1.	Make sure you have Python 3.x installed on your computer
2.	Install Pygame library via console:
-	pip install pygame
3.	Download the project with all files and assets
4.	Open the project folder via terminal (or VS code / PyCharm etc.)
5.	Run the main game file:
-	python main.py
6.	In opened game window use W, S, A, D to move UFO and survive!

# The additional features and classes
1.	Features
-	High score system
-	Random speed position of asteroids and planets appearing
-	3 HP system (loosing HP when colliding with asteroids)
-	Animated images of asteroids, planets and effects
-	Skins variety 
2.	Classes
-	UFO
-	Asteroid
-	Planet
-	Indicators (HPs, Planets, Score)
-	Background

