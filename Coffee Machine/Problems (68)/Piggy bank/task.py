class PiggyBank:
	def __init__(self, dollars, cents):
		self.dollars = dollars
		self.cents = cents
		self.capacity = 99

	def add_money(self, deposit_dollars, deposit_cents):
		self.deposit_dollars = deposit_dollars
		self.deposit_cents = deposit_cents

		if (self.cents + self.deposit_cents) <= self.capacity:
			self.cents += self.deposit_cents
			self.dollars += self.deposit_dollars
		else:

			self.cents += (self.deposit_cents + self.cents) % 100
			self.dollars += (self.deposit_cents + self.cents) // 100






bank = PiggyBank(0, 50)K
print(bank.dollars, bank.cents)
bank.add_money(0, 100)
print(bank.dollars, bank.cents)
bank.add_money(0, 200)
print(bank.dollars, bank.cents)
