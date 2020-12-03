from nuts_and_bolts.models import Product, User
from nuts_and_bolts import db, create_app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

app = create_app()
db.create_all(app=create_app())


def populate_user():
    manager = User(
        email = 'manager@nutsandbolts.com',
        password = bcrypt.generate_password_hash('B01Yellow!!').decode('utf-8')
    )

    db.session.add(manager)

    db.session.commit()


def populate_products():
    screw_driver_set = Product(
        sku=204663546,
        name='Husky Screwdriver Set (15-Piece)',
        price='29.97',
        description='The Husky 15-Piece Screwdriver Set includes eight slotted screwdrivers and seven Phillips screwdrivers for all your fastening work. The handle is crafted in a special pentagonal shape to provide greater torque and increased comfort, with a unique, dual material design to eliminate grip slippage during high-torque applications. The tip size markings are injected on the end of the handle for easy identification, while the alloy steel blades are heat treated for strength and the precision formed tips ensure an accurate fit to limit cam-out.',
        quantity=10
    )
    clamps = Product(
        sku=205086878,
        name='Dewalt Medium and Large Trigger Clamp (4-Pack)',
        price='36.97',
        description='DEWALT is the number 1 brand for woodworking and the Pro. These DEWALT 4-Pack Medium and Large Trigger Clamp pack is ideal for a variety of jobs including holding, spreading and glue ups. The Large Trigger Clamp have the capability to convert to a spreader with 1 touch of the quick change button. They also have a 300 lb. clamping force that makes them ideal for larger fastening jobs the Pro may have. The Medium clamp in this 4-pack have a clamping force of 100 lbs. No matter the job, DEWALT is guaranteed tough.',
        quantity=20
    )
    snips = Product(
        sku=302716396,
        name='Milwaukee 10 in. Straight-Cut Aviation Snips',
        price='13.97',
        description='Cut more metal than ever with Milwaukee Aviation Snips. The forged blades deliver up to 10X more cuts than cast blades. Bolt Lock prevents the blades from loosening and a durable chrome plating provides rust resistance. A metal lock secures the tool for storage and easily operates with 1 hand. Perfect for straight cuts.',
        quantity=30
    )
    torque_wrench = Product(
        sku=205913996,
        name='Husky 20 ft./lbs. to 100 ft./lbs. 3/8 in. Drive Torque Wrench',
        price='69.97',
        description='The Husky 3/8 in. Click Torque Wrench is made of alloy steel construction for strength and long-lasting performance. Its ergonomically designed handle easily turns to set torque. The finish provides resistance to corrosion and wipes clean easily.',
        quantity=40
    )
    laser = Product(
        sku=205910686,
        name='Bosch BLAZE 100 ft. Laser Distance Measurer',
        price='79.97',
        description='Instant information for most common laser measure functions, including area, distance, length, volume, continuous measurement and addition/subtraction. User doesn\'t need 2 measurements to get the third for area measurement. Backlighting allows user to see information in dark areas with better resolution. Handy pocket-size design that makes unit easy to use anywhere. Measuring distance extends to 100 ft. with +/- 1/16 in . accuracy.',
        quantity=50
    )

    db.session.add(screw_driver_set)
    db.session.add(clamps)
    db.session.add(snips)
    db.session.add(torque_wrench)
    db.session.add(laser)

    db.session.commit()


with app.app_context():

    populate_user()
    populate_products()

    print(db.session.query(User).all())
    print(db.session.query(Product).all())
