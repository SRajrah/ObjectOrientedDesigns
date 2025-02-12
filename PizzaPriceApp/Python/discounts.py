from discountStrategy import DiscountStrategy
class NoDiscount(DiscountStrategy):
    """Default strategy - no discount applied."""
    def apply_discount(self, price: float) -> float:
        return price  # No change

class PercentageDiscount(DiscountStrategy):
    """Applies a percentage-based discount."""
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(DiscountStrategy):
    """Applies a fixed discount on the price."""
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount

    def apply_discount(self, price: float) -> float:
        return max(price - self.discount_amount, 0)  # Ensures price doesn't go negative

class BuyOneGetOneFree(DiscountStrategy):
    """BOGO: Buy one pizza, get one free (applied at order level)."""
    def apply_discount(self, price: float) -> float:
        return price / 2  # Since 2 pizzas cost the price of 1