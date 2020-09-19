from nuts_and_bolts.models import Subcategory, Category, Brand, Product
from nuts_and_bolts import db, create_app

app = create_app()
db.create_all(app=create_app())


def populate_categories():
    power_tools = Category(
        name='power tools'
    )
    hand_tools = Category(
        name='hand tools'
    )

    db.session.add(power_tools)
    db.session.add(hand_tools)

    db.session.commit()


def populate_subcategories():
    drills = Subcategory(
        name='drills',
        category_id=1
    )
    circular_saws = Subcategory(
        name='circular saws',
        category_id=1
    )
    screw_drivers = Subcategory(
        name='screw drivers',
        category_id=2
    )
    hand_saws = Subcategory(
        name='hand saws',
        category_id=2
    )

    db.session.add(drills)
    db.session.add(circular_saws)
    db.session.add(screw_drivers)
    db.session.add(hand_saws)

    db.session.commit()


def populate_brands():
    black_and_decker = Brand(name='black & decker')
    bosch = Brand(name='bosch')
    channellock = Brand(name='channellock')
    dewalt = Brand(name='dewalt')
    dremel = Brand(name='dremel')
    milwakee = Brand(name='milwakee')

    db.session.add(black_and_decker)
    db.session.add(bosch)
    db.session.add(channellock)
    db.session.add(dewalt)
    db.session.add(dremel)
    db.session.add(milwakee)

    db.session.commit()


def populate_products():
    super_drill = Product(
        sku = 12345678,
        name = 'super drill',
        price = 55.99,
        brand_id = 1,
        subcategory_id = 1
    )
    crazy_drill = Product(
        sku = 23456789,
        name = 'crazy drill',
        price = 59.99,
        brand_id = 2,
        subcategory_id = 1
    )
    super_circular_saw = Product(
        sku = 34567890,
        name = 'super circular saw',
        price = 80.00,
        brand_id = 3,
        subcategory_id = 2
    )
    crazy_circular_saw = Product(
        sku = 45678901,
        name = 'crazy circular saw',
        price = 95.99,
        brand_id = 4,
        subcategory_id = 2
    )
    super_screw_driver = Product(
        sku = 56789012,
        name = 'super screw driver',
        price = 9.99,
        brand_id = 5,
        subcategory_id = 3
    )
    crazy_screw_driver = Product(
        sku = 67890123,
        name = 'crazy screw driver',
        price = 12.99,
        brand_id = 6,
        subcategory_id = 3
    )
    super_hand_saw = Product(
        sku = 78901234,
        name = 'super hand saw',
        price = 15.99,
        brand_id = 1,
        subcategory_id = 4
    )
    crazy_hand_saw = Product(
        sku = 89012345,
        name = 'crazy hand saw',
        price = 19.99,
        brand_id = 2,
        subcategory_id = 4
    )

    db.session.add(super_drill)
    db.session.add(crazy_drill)
    db.session.add(super_circular_saw)
    db.session.add(crazy_circular_saw)
    db.session.add(super_screw_driver)
    db.session.add(crazy_screw_driver)
    db.session.add(super_hand_saw)
    db.session.add(crazy_hand_saw)

    db.session.commit()



with app.app_context():

    populate_categories()
    populate_subcategories()
    populate_brands()
    populate_products()

    print(db.session.query(Category).all())
    print(db.session.query(Subcategory).all())
    print(db.session.query(Brand).all())
    print(db.session.query(Product).all())

