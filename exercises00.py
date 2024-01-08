from datetime import datetime as dt 
import os 


class Exercise00:

	def __init__(self, text = ''):
		self.text = text

	# falls der entgegengenommene Text mehr als 17 Characters enthält, schreiben wir die ersten 17 und 3 punkte danach, sonst nur den ganzen Text und 3 punkte danach
	@property
	def txt(self):
		if len(self.text) <= 17:
			return self.text + "..."
		else:
			return self.text[:17] + "..."


	# standart library von Python, default ohne eingabe, falls wir format haben, wird text entsprechend ausgegeben
	def deadline(format = ''):
		deadline = dt(2023, 11, 15, 9, 0)
		modified = deadline.strftime(format)
		return modified


	# checking if the given string "order" or "dict" and accordingly giving back a statement, as we have 2 different .format 
	# the first one is for calling the method and the second is fomatting the string, so changing the order of the given strings
	def format(self, string):
		if string == "order":
			# the order of the statement is changed according to their numbers
			return "{2} - {1} - {0}"
		elif string == "dict":
			# we are taking the value of the key x and writing the value with 1 number after comma with .1f, and the same but with .4f with the key y
			return "x, y = ({x:.1f}, {y:.4f})"

	# TODO: dict format

	# no self as its a static method, default file_type is none, root is current dir, we also have the files under the dir
	# yield is used to show its a generator, the file type is also being checked in the code
	@staticmethod
	def listfiles(directory, file_type = None):
	    if file_type is None:
	        for root, subdirectory, files in os.walk(directory):
	            for file in files:
	                yield os.path.join(root, file)
	    else:
	        for root, subdirectory, files in os.walk(directory):
	            for file in files:
	                if file.endswith(file_type):
	                    yield file


	# collatz falls es kein int oder weniger als 1 ist, wird ([], 0) ausgegeben, sonst die operationen durchgeführt und jede Schritt gespeichert               
	def collatz(self, n):
		if type(n) != int or n < 1:
			return ([], 0)

		collatzlist = []
		collatzlist.append(n)

		while n > 1:
			if n % 2 == 1:
				n = 3 * n + 1
				collatzlist.append(n)
			else:
				n = n // 2
				collatzlist.append(n)

		return (collatzlist, len(collatzlist))

	# **kwargs to get the key and value arguments and then sort them to have them in an order, and then adding them all to a string with keys and values
	def __call__(self, **kwargs):
	    keys_sorted = sorted(kwargs.keys())
	    result = ""
	    for key in keys_sorted:
	    	result += "{key} = {kwargs[key]}\n"
	    return result


	#ex = Exercise00()
	#ex(c=None, a=1, d=4, b=’2’)

		# TODO: function parameters
		# TODO: argparse

