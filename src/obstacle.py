# -*- coding: utf-8 -*-
class Obstacle:
	"""Un obstacle est defini par ses coordonnees dans la matrice et sa taille.
	La taille d'un objet est une case de la matrice ou un carré de cases de la matrice.
	"""
	def __init__(self, x, y, taille):
		self.x=x
		self.y=y
		self.taille=taille
		
		