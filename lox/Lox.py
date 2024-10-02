import sys
import os

class Lox:
	def __init__(self):
		pass
	
	def pylox_main(self, args):
		"""
		Driver method, in book it is named main, but here it is named 
		pylox_main to avoid naming conflicts.
		
		:param list args: list containing path to executable file.
		:return: None. 
		"""
		
		argLength = len(args)
		
		if argLength > 1:
			sys.exit("Usage: pylox [script]")
		elif argLength == 1:
			self.runFile(args[0])
		else:
			self.runPrompt()
		
	def runFile(self, path):
		"""
		Read a file and execute it.
		
		:param String path: path where file to be executed is located.
		:return: None.
		"""
		
		filePath = os.path.normpath(path)
		file1 = open(filePath, "r+")
		lines = file1.readlines()
		self.run(lines)
	
	def runPrompt(self):
		"""
		Interactively execute one code line at a time.
		
		:return: None.
		"""
		
		line = raw_input()
		while True:
			if line == None:
				break
			self.run(line)
	
	def run(self, source):
		"""
		Execute a line of code.
		
		:param String source: line of code to be executed. 
		"""
		
		scanner = Scanner(source)
		tokens = scanner.scanTokens()
		
		for token in tokens:
			print(token)
	
	
		
		
