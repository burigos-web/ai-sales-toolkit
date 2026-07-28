"""
AI Sales Toolkit
Markup Calculator
"""


def calculate_markup(cost: float, sale_price: float) -> float:
    """
    Calculate markup percentage based on cost.
    """

    if cost <= 0:
        raise ValueError("Cost must be greater than zero.")

    markup = ((sale_price - cost) / cost) * 100

    return round(markup, 2)


if __name__ == "__main__":
    cost = 100
    sale = 180

    print(f"Markup: {calculate_markup(cost, sale)}%")
