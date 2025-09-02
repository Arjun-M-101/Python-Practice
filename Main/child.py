from parent import Mom
class Daughter(Mom):
    def __init__(self, gold):
        self.gold = gold
    def money(self):
        return f"Daugher spends money for her marriage. {self.gold}"
marriage=Daughter("Mom's gold is also for daughter.")
print(marriage.savings())  # Because Daughter inherits from Mom, so she can access the savings (method).
print(marriage.money())  # Daughter also has her own money (method).