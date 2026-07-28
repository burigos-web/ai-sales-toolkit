"""
AI Sales Toolkit
Margin Calculator
"""

def calculate_margin(cost: float, sale_price: float) -> float:
    """
    Calculate gross margin percentage.

    Args:
        cost: Product or service cost.
        sale_price: Final selling price.

    Returns:
        Gross margin percentage.
    """
    if cost < 0:
        raise ValueError("Cost cannot be negative.")

    if sale_price <= 0:
        raise ValueError("Sale price must be greater than zero.")

    margin = ((sale_price - cost) / sale_price) * 100
    return round(margin, 2)


if __name__ == "__main__":
    cost = 100.00
    sale_price = 180.00

    margin = calculate_margin(cost, sale_price)

    print(f"Cost: {cost}")
    print(f"Sale price: {sale_price}")
    print(f"Gross margin: {margin}%")
