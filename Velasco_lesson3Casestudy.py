sales_data = [
    {"product": "Laptop", "price": 50000, "quantity": 2},
    {"product": "Mouse", "price": 500, "quantity": 5},
    {"product": "Keyboard", "price": None, "quantity": 3},
    {"product": "Monitor", "price": 8000, "quantity": "two"},
    {"product": "USB", "price": 300, "quantity": 10},
    {"product": "Headset", "price": "1500", "quantity": 4},
    {"product": "Webcam", "price": 2500, "quantity": None}
]

def clean_data(data):
    cleaned = []

    for record in data:
        try:
            price = int(record["price"])
            quantity = int(record["quantity"])

            cleaned.append({
                "product": record["product"],
                "price": price,
                "quantity": quantity
            })

        except (ValueError, TypeError):
            print(f"Invalid record skipped: {record['product']}")

    return cleaned


def calculateSales(data):
    for record in data:
        record["total_sales"] = record["price"] * record["quantity"]
    return data

def filter_sales(data, threshold):
    return [item for item in data if item["total_sales"] > threshold]

def summarize_sales(data):
    total_revenue = sum(item["total_sales"] for item in data)
    average_sales = total_revenue / len(data)

    highest = max(data, key=lambda x: x["total_sales"])
    lowest = min(data, key=lambda x: x["total_sales"])

    print("\nSales Summary")
    print("-------------")
    print("Total Revenue:", total_revenue)
    print("Average Sales:", average_sales)
    print("Highest Sale:", highest["product"])
    print("Lowest Sale:", lowest["product"])

cleaned_data = clean_data(sales_data)

print("\nCleaned Data:")
print(cleaned_data)

updated_data = calculateSales(cleaned_data)

filtered_products = filter_sales(updated_data, 5000)

print("\nFiltered Products (Sales > 5000):")
for product in filtered_products:
    print(product["product"])

summarize_sales(updated_data)
