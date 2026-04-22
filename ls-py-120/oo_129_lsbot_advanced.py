# 1:

'''
1.  Create an abstract base Character class. It should have attributes for name, health (default 100), and level (default 1). It should also have a take_damage method.
2.  Implement three concrete character classes inheriting from Character: Warrior, Mage, and Rogue.
    •   Warrior: Has an extra attribute rage (default 0). Override the take_damage method so that taking damage increases their rage.
    •   Mage: Has an extra attribute mana (default 100). Implement a cast_spell method that consumes mana.
    •   Rogue: Has an extra attribute energy (default 100). Implement a stealth_attack method that consumes energy.
3.  Create a Party class that acts as a container for Character objects.
    •   It should have methods to add_member and remove_member.
    •   Implement a party_attack method that iterates through all members of the party and makes them perform a signature move (rage_smash for Warrior, cast_spell for Mage, stealth_attack for Rogue). This demonstrates polymorphism.
    •   Overload the __str__ method to display the status of all party members.
4.  Create a custom exception class PartyFullError that is raised when someone tries to add a member to a full party (let's say a party has a max size of 4).
5.  Demonstrate creating a party, adding different character types, and using the party_attack and __str__ methods.
'''

class Character:
    def __init__(self, name, health=100, level=1):
        self.name = name
        self.health = health
        self.level = level

    def take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        return f"""Name: {self.name}
Health: {self.health}
Level: {self.level}"""

class Warrior(Character):
    def __init__(self, name, health=100, level=1, rage=0):
        super().__init__(name, health, level)
        self.rage = rage

    def take_damage(self, damage):
        print(f"{self.name} takes {damage} points of damage and adds 4 points of rage.")
        super().take_damage(damage)
        self.rage += 4

    def rage_smash(self):
        print(f"{self.name} rage-smashes!")

    def signature_move(self):
        self.rage_smash()

    def __str__(self):
        return f"""{super().__str__()}
Rage: {self.rage}"""

class Mage(Character):
    MANA_COST = 10

    def __init__(self, name, health=100, level=1, mana=100):
        super().__init__(name, health, level)
        self.mana = mana

    def cast_spell(self):
        if self.mana > Mage.MANA_COST:
            self.mana -= Mage.MANA_COST
            print(f'{self.name} casts a spell.')
        else:
            print(f"{self.name} doesn't have enough mana.")

    def signature_move(self):
        self.cast_spell()

    def __str__(self):
        return f"""{super().__str__()}
Mana: {self.mana}"""

class Rogue(Character):
    ENERGY_COST = 10

    def __init__(self, name, health=100, level=1, energy=100):
        super().__init__(name, health, level)
        self.energy = energy

    def stealth_attack(self):
        if self.energy > Rogue.ENERGY_COST:
            self.energy -= Rogue.ENERGY_COST
            print(f'{self.name} does a stealth attack.')
        else:
            print(f"{self.name} doesn't have enough energy.")

    def signature_move(self):
        self.stealth_attack()

    def __str__(self):
        return f"""{super().__str__()}
Energy: {self.energy}"""

class Party:
    MAX_MEMBERS = 4

    def __init__(self):
        self.members = []

    def add_member(self, member):
        if len(self.members) == Party.MAX_MEMBERS:
            raise PartyFullError("The party is full.")

        self.members.append(member)
        print(f"{member.name} added to party.")

    def remove_member(self, member):
        self.members.remove(member)
        print(f"{member.name} removed from party.")

    def party_attack(self):
        print("Attack all together!")
        for member in self.members:
            member.signature_move()

    def __str__(self):
        party_status = "Party status:"
        for member in self.members:
            party_status += f"\n\n{member}"
        return party_status

class PartyFullError(Exception):
    pass

warrior1 = Warrior("Bob")
mage1 = Mage("Vum")
rogue1 = Rogue("Ror")
rogue2 = Rogue("Ror2")

warrior1.take_damage(15)
warrior1.rage_smash()
print(warrior1)

mage1.cast_spell()
print(mage1)

rogue1.stealth_attack()
print(rogue1)

party1 = Party()

party1.add_member(warrior1)
party1.add_member(mage1)
party1.add_member(rogue1)
party1.add_member(rogue2)
party1.remove_member(rogue1)

party1.party_attack()

print(party1)

# 2:

'''
1.  Create a LibraryItem base class with attributes like title, author_artist, and a unique item_id. It should have a boolean is_checked_out status.

2.  Create two subclasses, Book and DVD, that inherit from LibraryItem.
    •   Book should have an additional isbn attribute.
    •   DVD should have an additional runtime_minutes attribute.

3.  Create a Member class with name and a list of borrowed_items.

4.  Create a Library class that acts as the main controller.
    •   It should use composition to hold a collection of LibraryItem objects and a collection of Member objects.
    •   Implement methods like add_item, register_member, lend_item(member_id, item_id), and return_item(member_id, item_id).

5.  Implement custom exception classes: ItemNotAvailableError (raised when trying to lend an already checked-out item) and MemberNotFoundError.

6. Override the __repr__ method for LibraryItem and its subclasses to provide a developer-friendly representation of the objects.
'''

class LibraryItem:
    item_id = 0

    def __init__(self, title, author_artist):
        self.title = title
        self.author_artist = author_artist
        self.is_checked_out = False
        LibraryItem.item_id += 1
        self.item_id = LibraryItem.item_id

    def __repr__(self):
        return (f"LibraryItem({repr(self.title)}, "
                f"{repr(self.author_artist)}, {self.item_id})")

class Book(LibraryItem):
    def __init__(self, title, author_artist, isbn):
        super().__init__(title, author_artist)
        self.isbn = isbn

    def __repr__(self):
            return (f"Book({repr(self.title)}, {repr(self.author_artist)}, "
                    f"{self.item_id}, {repr(self.isbn)})")

class DVD(LibraryItem):
    def __init__(self, title, author_artist, runtime_minutes):
        super().__init__(title, author_artist)
        self.runtime_minutes = runtime_minutes

    def __repr__(self):
            return (f"DVD({repr(self.title)}, {repr(self.author_artist)}, "
                    f"{self.item_id}, {self.runtime_minutes})")

class Member:
    member_id = 0

    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

        Member.member_id += 1
        self.member_id = Member.member_id

class Library:
    books_and_dvds = {}
    members = {}

    def add_item(self, item):
        Library.books_and_dvds[item.item_id] = item

    def register_member(self, member):
        Library.members[member.member_id] = member

    def lend_item(self, member_id, item_id):
        member = Library.members.get(member_id)
        item = Library.books_and_dvds.get(item_id)

        if not member:
            raise MemberNotFoundError(f"Member not found.")

        if not item:
            print("Item is not and was not in the library.")
            return

        if item.is_checked_out:
            raise ItemNotAvailableError(f"'{item.title}' is already checked out.")

        item.is_checked_out = True
        member.borrowed_items.append(item)
        print(f"Lent '{item.title}' by {item.author_artist} to {member.name}.")

    def return_item(self, member_id, item_id):
        member = Library.members.get(member_id)
        item = Library.books_and_dvds.get(item_id)

        if not member:
            raise MemberNotFoundError(f"Member not found.")

        if not item:
            raise ItemNotFoundError("Item is not and was not in the library.")

        if item not in member.borrowed_items:
            print(f"Error: {member.name} did not borrow '{item.title}'.")
            return

        item.is_checked_out = False
        member.borrowed_items.remove(item)
        print(f"{member.name} has returned '{item.title}'.")

class ItemNotAvailableError(Exception):
    pass

class ItemNotFoundError(Exception):
    pass

class MemberNotFoundError(Exception):
    pass

talent = Book('Talent', 'Tyler Cowen', 4192951034)
comedian = DVD('Comedian', 'Jerry Seinfeld', 90)
konstantin = Member('Konstantin')
library = Library()
library.add_item(talent)
library.add_item(comedian)
library.register_member(konstantin)
library.lend_item(1, 1)
# library.return_item(2, 1)
library.return_item(1, 2)
library.return_item(1, 1)

# 3:

'''
1.  Create a Product class with name, price, and quantity.
2.  Create a VendingMachine class that "has-a" dictionary of Product objects, where keys are slot IDs (e.g., "A1").
    •   It should also have an attribute for current_balance.
    •   Implement methods insert_coin(amount), select_product(slot_id), and return_coins().
3.  The select_product method should handle all logic:
    •   Check if the product exists.
    •   Check if the product is in stock (quantity > 0).
    •   Check if current_balance is sufficient.
    •   If all checks pass, dispense the product (decrement quantity), calculate change, and reset current_balance.
4.  Define three custom exception classes: InsufficientFundsError, OutOfStockError, and InvalidSelectionError. These should be raised in the appropriate scenarios within select_product.
5.  Implement a class method from_inventory_file(filepath) on VendingMachine that can create a new VendingMachine instance populated with products from a simple text file.
6.  Override the __str__ method for VendingMachine to display a user-friendly list of available products, their prices, and quantities.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class VendingMachine:
    def __init__(self):
        self.products = {}
        self.current_balance = 0

    def insert_coin(self, amount):
        self.current_balance += amount
        print(f"Inserted {amount}. Current balance is {self.current_balance}.")
        return self.current_balance

    def select_product(self, slot_id):
        if slot_id not in self.products:
            raise InvalidSelectionError(f"No slot ID named {slot_id}.")

        if self.products[slot_id].quantity < 1:
            raise OutOfStockError(f"Out of stock.")

        if self.current_balance < self.products[slot_id].price:
            raise InsufficientFundsError(f"You are {self.products[slot_id].price - self.current_balance} short.")

        print(f"Dispensing {self.products[slot_id].name}.")
        self.products[slot_id].quantity -= 1

        print(f"Your change is {self.current_balance - self.products[slot_id].price}")
        self.current_balance = 0

    @classmethod
    def from_inventory_file(cls, filepath):
        new_machine = cls()

        with open(filepath, 'r') as f:
            for line in f:
                slot_id, name, price_str, quantity_str = line.strip().split(',')

                price = float(price_str)
                quantity = int(quantity_str)

                product = Product(name, price, quantity)
                new_machine.products[slot_id] = product

        return new_machine

    def __str__(self):
        to_print = ['Available Products:']

        if not self.products:
            to_print.append("This machine is empty.")
        else:
            for slot_id, product in self.products.items():
                line = (f"{slot_id}: {product.name} - ${product.price:.2f} (Qty: {product.quantity})")
                to_print.append(line)

        return '\n'.join(to_print)

class InsufficientFundsError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class InvalidSelectionError(Exception):
    pass

ramen = Product('Ramen', 5, 10)
vm1 = VendingMachine()
vm1.products['A1'] = ramen
print(vm1)
vm1.insert_coin(6)
vm1.select_product('A1')

# 4:

'''
1.  Create a MenuItem base class with name and price.
2.  Create FoodItem and DrinkItem subclasses. FoodItem should have a calories attribute, and DrinkItem should have a boolean is_alcoholic attribute.
3. Create an Order class.
    •   It should contain a list of MenuItem objects.
    •   It should have a total_price property that calculates the sum of the prices of all items in the order.
4.  Create a Table class with a table_number and a current_order (an Order object). It should have methods like add_to_order(menu_item) and generate_bill(). The generate_bill method should return a formatted string with each item, its price, and the total.
5.  Create a Restaurant class that manages a collection of Table objects.
6.  Overload the + operator for the Order class so that two orders can be combined to create a new Order containing all items from both.
'''

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FoodItem(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

class DrinkItem(MenuItem):
    def __init__(self, name, price, is_alcoholic):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic

class Order:
    def __init__(self):
        self.items = []

    @property
    def total_price(self):
        order_total_price = 0

        for item in self.items:
            order_total_price += item.price
        return order_total_price

    def __add__(self, other_order):
        if not isinstance(other_order, Order):
            return NotImplemented

        new_order = Order()
        new_order.items = self.items + other_order.items
        return new_order

    def __iadd__(self, other_order):
        if not isinstance(other_order, Order):
            return NotImplemented

        return self.items.extend(other_order.items)

    def add_item(self, item):
        self.items.append(item)

class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.current_order = Order()

    def add_to_order(self, menu_item):
        self.current_order.add_item(menu_item)

    def generate_bill(self):
        bill = [f'Table {self.table_number} bill:']

        if not self.current_order.items:
            bill.append("Nothing yet!")
        else:
            for item in self.current_order.items:
                bill.append(f"{item.name}: ${item.price}")

            bill.append(f"Total: {self.current_order.total_price}")

            return '\n'.join(bill)

class Restaurant:
    def __init__(self):
        self.tables = []

    def add_table(self, table):
        if isinstance(table, Table):
            self.tables.append(table)
        else:
            print("Can only add Tables.")

# 5:

class Element:
    def __init__(self, name, symbol, atomic_weight):
        self.name = name
        self.symbol = symbol
        self.atomic_weight = atomic_weight

    def __repr__(self):
        return f'Element({repr(self.name)}, {repr(self.symbol)}, {repr(self.atomic_weight)})'

class Compound:
    def __init__(self, *elements):
        self._elements = list(elements)

    @property
    def formula(self):
        symbol_counts = {}
        for elem in self._elements:
            symbol_counts[elem.symbol] = symbol_counts.get(elem.symbol, 0) + 1

        formula_str = ''
        for symbol, count in symbol_counts.items():
            formula_str += symbol
            if count > 1:
                formula_str += str(count)

        return formula_str

    @property
    def molecular_weight(self):
        return sum(elem.atomic_weight for elem in self._elements)

    def __add__(self, other_compound):
        if not isinstance(other_compound, Compound):
            return NotImplemented

        combined_elements = self._elements + other_compound._elements

        return Compound(*combined_elements)

    def __iadd__(self, other_compound):
        if not isinstance(other_compound, Compound):
            return NotImplemented

        return self._elements + other_compound._elements

    def __eq__(self, other_compound):
        return self.molecular_weight == other_compound.molecular_weight

    def __lt__(self, other_compound):
        return self.molecular_weight < other_compound.molecular_weight

class AlchemicalLab:
    @staticmethod
    def transmute(element1, element2):
        new_weight = element1.atomic_weight + element2.atomic_weight
        return Element("New-Element", "??", new_weight)

    @staticmethod
    def validate_element(element):
        return isinstance(element, Element)

    @staticmethod
    def mix(compound1, compound2):
        try:
            if not (isinstance(compound1, Compound) and 
                    isinstance(compound2, Compound)):
                raise InvalidCompoundError("Invalid compound.")
            return compound1 + compound2
        except InvalidCompoundError as e:
            print(e)

class InvalidCompoundError(Exception):
    pass

hydrogen = Element("Hydrogen", "H", 1.008)
oxygen = Element("Oxygen", "O", 15.999)
carbon = Element("Carbon", "C", 12.011)
sodium = Element("Sodium", "Na", 22.990)
chlorine = Element("Chlorine", "Cl", 35.453)

print(hydrogen)
print(repr(carbon))
print("-" * 20)

water = Compound(hydrogen, hydrogen, oxygen)
salt = Compound(sodium, chlorine)
ethanol = Compound(carbon, carbon, hydrogen, hydrogen, hydrogen, hydrogen, hydrogen, oxygen, hydrogen)

print(f"Water Formula: {water.formula}") # H2O
print(f"Water Molecular Weight: {water.molecular_weight}") # 18.015
print(f"Salt Formula: {salt.formula}") # NaCl
print(f"Salt Molecular Weight: {salt.molecular_weight}") # 58.443

brine = water + salt
print(f"Brine Formula: {brine.formula}")
print(f"Brine Molecular Weight: {brine.molecular_weight}")

print(f"Is water < salt? {water < salt}")
print(f"Is salt < water? {salt < water}")

new_element = AlchemicalLab.transmute(hydrogen, carbon)
print(new_element)
print(f"New element weight: {new_element.atomic_weight}") # 13.019

print(f"Is hydrogen an Element? {AlchemicalLab.validate_element(hydrogen)}")
print(f"Is water an Element? {AlchemicalLab.validate_element(water)}")

print("Mixing valid compounds (water + salt):")
mixed_compound = AlchemicalLab.mix(water, salt)

if mixed_compound:
    print(f"Resulting compound formula: {mixed_compound.formula}")

print("Mixing invalid compound (water + 'not a compound'):")
AlchemicalLab.mix(water, "not a compound") # "Invalid compound."