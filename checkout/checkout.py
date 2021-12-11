from dataclasses import dataclass, field

import logging

@dataclass
class Checkout:
    prices: dict[str,float] = field(default_factory=dict)
    discounts: dict[str,float] = field(default_factory=dict)
    items: dict[str,float] = field(default_factory=dict)
    # total: float = field(default_factory=float)

    @dataclass
    class Discount:
        number_of_items: int 
        price: float


    logging.basicConfig(level=logging.INFO)
    logger=logging.getLogger()


    def add_item_price(self, item_name: str, price: float)-> None:
        self.prices[item_name] = price
        self.logger.info(f"Prices : {self.prices}")

    def add_item(self, item_name: str)-> None:
        # self.total += self.prices[item_name]
        # if item_name in self.items:
        #     self.items[item_name] += 1
        # else:
        #     self.items[item_name] = 1
        if item_name not in  self.prices :
            raise Exception(f"f{item_name} does not have a price")
            
        self.items[item_name] = 1 if item_name not in self.items else self.items[item_name]+1

        self.logger.info(f"Items : {self.items}")

    def add_discount(self, item_name:str , num_of_items_to_qualify: int, new_price: float)-> None:
        discount = self.Discount(num_of_items_to_qualify, new_price)
        self.discounts[item_name] = discount
        
    def calculate_current_total(self)-> float:                
        # self.logger.info(f"Total : {self.total}")
        total = 0
        for item_name, count in self.items.items():
            total += self.calculate_item_total(item_name, count)
        return total

    def calculate_item_total(self, item_name:str, count:int)-> float:
        total=0
        if item_name in self.discounts:
            discount = self.discounts[item_name]
            if count >= discount.number_of_items:
                total += self.calculate_item_discounted_total(item_name, count, discount)
            else:
                total += self.prices[item_name] * count
        else:
            total += self.prices[item_name] * count

        return total

    def calculate_item_discounted_total(self, item_name: str, count: int, discount: Discount)-> float:
        total = 0

        no_of_discounts = count/discount.number_of_items
        total += no_of_discounts * discount.price
        remaining = count % discount.number_of_items
        total += remaining * self.prices[item_name]

        return total

