class Token:
	def __init__(self, _type, lexeme, literal, line):
		self._type = _type
		self.lexeme = lexeme
		self.literal = literal
		self.line = line
		
	def toString(self):
		"""
		Return string representation of Token.
		
		:rtype: String
		"""
		
		retStr = f"{type} {lexeme} {literal"
		return retStr
