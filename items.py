from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, InventoryItem

engine = create_engine('postgresql://catalog:catalog-pw@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Inventory for Clothes
category1 = Category(name="Clothes")

session.add(category1)
session.commit()

inventoryItem2 = InventoryItem(name="Black Shirt", category=category1)

session.add(inventoryItem2)
session.commit()


inventoryItem1 = InventoryItem(name="White Shirt", category=category1)

session.add(inventoryItem1)
session.commit()

inventoryItem2 = InventoryItem(name="Pink Shirt", category=category1)

session.add(inventoryItem2)
session.commit()

inventoryItem3 = InventoryItem(name="Gray Shirt", category=category1)

session.add(inventoryItem3)
session.commit()

inventoryItem4 = InventoryItem(name="Black Pants", category=category1)

session.add(inventoryItem4)
session.commit()

inventoryItem5 = InventoryItem(name="Blue Pants", category=category1)

session.add(inventoryItem5)
session.commit()

inventoryItem6 = InventoryItem(name="Pink Pants", category=category1)

session.add(inventoryItem6)
session.commit()

inventoryItem7 = InventoryItem(name="Black and White Stripe Pants", category=category1)

session.add(inventoryItem7)
session.commit()

inventoryItem8 = InventoryItem(name="Skirt", category=category1)

session.add(inventoryItem8)
session.commit()


# Inventory for Cars
category2 = Category(name="Cars")

session.add(category2)
session.commit()


inventoryItem1 = InventoryItem(name="Isuzu", category=category2)

session.add(inventoryItem1)
session.commit()

inventoryItem2 = InventoryItem(name="GMC", category=category2)

session.add(inventoryItem2)
session.commit()

inventoryItem3 = InventoryItem(name="Buick", category=category2)

session.add(inventoryItem3)
session.commit()

inventoryItem4 = InventoryItem(name="Plymouth", category=category2)

session.add(inventoryItem4)
session.commit()

inventoryItem5 = InventoryItem(name="Mazda", category=category2)

session.add(inventoryItem5)
session.commit()

inventoryItem6 = InventoryItem(name="Chevrolet", category=category2)

session.add(inventoryItem6)
session.commit()


# Inventory for Stocks
category1 = Category(name="Stocks")

session.add(category1)
session.commit()


inventoryItem1 = InventoryItem(name="PRA Health Sciences, Inc", category=category1)

session.add(inventoryItem1)
session.commit()

inventoryItem2 = InventoryItem(name="MV Oil Trust", category=category1)

session.add(inventoryItem2)
session.commit()

inventoryItem3 = InventoryItem(name="Seanergy Maritime Holdings Corp", category=category1)

session.add(inventoryItem3)
session.commit()

inventoryItem4 = InventoryItem(name="Dynavax Technologies Corp", category=category1)

session.add(inventoryItem4)
session.commit()

inventoryItem2 = InventoryItem(name="Guaranty Bancshares, Inc", category=category1)

session.add(inventoryItem2)
session.commit()


print("added items!")