
class tee_string:
	def __init__(self, in_str=""):
		self.str = list(in_str)

	def swap(i, j):
		x = str[i]
		str[i] = str[j]
		str[j] = x
	def to_string():
		return ''.join(self.str)
	def dup():
		return tee_string(self.to_string())

	def reverse(self, f = 0, t = len(self.str)-1):
		while f < t:
			x = self.str[f]
			self.str[f] = self.str[t]
			self.str[t] = x
			f = f+1
			t = t-1

	def move_front(self, f, t, len):
		for i in range(0, len):
			x = self.str[t+i]
			self.str[t+i] = self.str[f+i]
			self.str[f+i] = x
	def move_back(self, f, t, len):
		move_front(self, t, f, len)
	def move(self, f, t, len):
		if f > t:
			move_front(self, f, t, len)
		else
			move_back(self, f, t, len)

	def sub_words(self, sp):
		ret = []
		begin = 0
		for i in range(0, len(self.str)-1):
			if i in sp:
				if i-1 > begin:
					ret.add([begin, i-1])
				begin = i+1
		return ret
	def reverse_words(self, sp, f, t):
		ret = sub(self, sp)

	def is_palindrome(self, f = 0, t = len(self.str)):
		while f < t:
			if self.str[f] != self.str[t]:
				return False
			f = f+1
			t = t-1
		return True
	def sub_palindromes(self, f = 0, t = len(self.str)):
		ret = []
		l = (t-f)>>1
		for i in range(1, l):
			for j in range(0, i-1):
				if self.str[f+i-j] == self.str[f+i+j]:
					ret.append([])
			for j in range(0, i-1):
				if self.str[] == self.str[]:
					ret.append([])
		return ret
	def max_palindromes(self, f = 0, t = len(self.str)-1):
		pass

	def do_permutation(self, str, f, t, ret):
		if t <= 1:
			return
		if f == t:
			for i in range(0, t):
				ret.add(str[i:])
		else:
			for j in range(f, t):
				str.swap(j, f)
				do_permutation(f+1, t)
				str.swap(j, f)
	def permutation(self, f = 0, t = len(self.str)-1):
		ret = []
		do_permutation(self, self.dup(), f, t, ret)
		return ret
	def next_permutation():
		pass
