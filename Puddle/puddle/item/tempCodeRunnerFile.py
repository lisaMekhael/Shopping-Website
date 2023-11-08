from .models import Item  

items = Item.objects.all()

for item in items:
    print(f"Item ID: {item.id}")
    print(f"Item Name: {item.name}")
    print(f"Item Description: {item.descrip}")

    print('-' * 40)
