class TimeDesk:
	def metod(self,seconds):
		if isinstance(seconds,int):
			self.seconds = seconds
		else:
			raise ValueError("seconds should be int")
		mint= 60
		hour=3600
		day=86400
		self.b = self.seconds // day
		self.c= self.seconds - self.b*day
		self.z= self.c//hour
		self.v= self.c-self.z*hour
		self.q=self.v//mint
		self.n=self.v%mint
		return f'{self.b}-day,{self.z},-hour,{self.q},-mint,{self.n}- sec)'
sec=TimeDesk()
print(sec.metod(86401))

























