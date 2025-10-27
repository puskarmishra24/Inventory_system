"""Inventory System Module.

This module provides functions for managing an inventory of items.
It allows adding, removing, saving, loading, and displaying inventory data
securely and following best practices in code quality, security, and style.
"""

import json
from datetime import datetime


def add_item(
    item: str = "default",
    quantity: int = 0,
    logs: list[str] | None = None,
    stock_data: dict[str, int] | None = None,
) -> dict[str, int]:
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []
    if stock_data is None:
        stock_data = {}

    if not isinstance(item, str):
        print("Invalid item name.")
        return stock_data

    if not isinstance(quantity, int):
        print("Invalid quantity type.")
        return stock_data

    if quantity < 0:
        print("Quantity cannot be negative.")
        return stock_data

    stock_data[item] = stock_data.get(item, 0) + quantity
    logs.append(f"{datetime.now()}: Added {quantity} of {item}")
    return stock_data


def remove_item(
    item: str,
    quantity: int,
    stock_data: dict[str, int],
) -> dict[str, int]:
    """Remove a specific quantity of an item from the inventory safely."""
    try:
        if item not in stock_data:
            print(f"Item '{item}' not found!")
            return stock_data

        if quantity < 0:
            print("Quantity to remove cannot be negative.")
            return stock_data

        stock_data[item] -= quantity
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as error:
        print(f"Error removing item: {error}")
    return stock_data


def get_quantity(item: str, stock_data: dict[str, int]) -> int:
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_name: str = "inventory.json") -> dict[str, int]:
    """Load inventory data from a JSON file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty data.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning empty inventory.")
    return {}


def save_data(stock_data: dict[str, int], file_name: str = "inventory.json") -> None:
    """Save current inventory data to a JSON file safely."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
    except OSError as error:
        print(f"Error saving data: {error}")


def print_data(stock_data: dict[str, int]) -> None:
    """Print all items and their quantities."""
    print("Items Report:")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(stock_data: dict[str, int], threshold: int = 5) -> list[str]:
    """Check and return items below a given threshold."""
    return [item for item, quantity in stock_data.items() if quantity < threshold]


def main() -> None:
    """Main function for testing inventory operations."""
    stock_data: dict[str, int] = {}

    stock_data = add_item("apple", 10, stock_data=stock_data)
    stock_data = add_item("banana", 2, stock_data=stock_data)
    stock_data = add_item("pear", 5, stock_data=stock_data)

    stock_data = remove_item("apple", 3, stock_data)
    stock_data = remove_item("orange", 1, stock_data)

    print("Apple stock:", get_quantity("apple", stock_data))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    stock_data = load_data()

    print_data(stock_data)
    print("Eval removed for safety.")


if __name__ == "__main__":
    main()
