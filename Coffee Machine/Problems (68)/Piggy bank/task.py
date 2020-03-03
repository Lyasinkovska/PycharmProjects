class PiggyBank:

	def __init__(self, dollars, cents):
		self.dollars = dollars
		self.cents = cents
		self.capacity = 100

	def add_money(self, deposit_dollars, deposit_cents):
		self.deposit_dollars = deposit_dollars
		self.deposit_cents = deposit_cents
		self.cents += self.deposit_cents + (self.deposit_dollars + self.dollars) * 100
		self.dollars = self.cents // 100
		self.cents %= 100
		return self.cents, self.dollars
