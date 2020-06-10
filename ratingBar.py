import sys
def n_digit(n,string):
	while(len(string) < n):
		string += ' '
	return string

class ratingBar:
	def __init__(self,length,starting = ''):
		self.length = length
		self.one = 100 / length
		self.n = len(str(self.length))
		self.starting = starting
		sys.stdout.write('%s%s%s/%s|%s|0%%'%(self.starting,'|' * int(bool(self.starting)),n_digit(self.n,'0'),length,' ' * length))
		sys.stdout.flush()
		self.len = 0
	def flush(self,length):
		str1 = '#' * length + ' ' * (self.length - length)
		sys.stdout.flush()
		sys.stdout.write('\r%s%s%s/%s|%s|%s%%'%(self.starting,'|' * int(bool(self.starting)),n_digit(self.n,str(length)),self.length,str1,self.one * length))
		if(length == self.length):
			sys.stdout.write('\n')
			sys.stdout.flush()
		self.len = length
	def count(self):
		self.len += 1
		self.flush(self.len)
