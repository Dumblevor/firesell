from app import app, db
from data.product_data import product_list, comments_list, ratings_list
from data.customer_data import customer_list
from data.order_data import order_list, orderline_list
from data.seller_data import seller_list
from data.pictures_data import picture_list

with app.app_context():

    try:
        print("recreating database...")
        db.drop_all()
        db.create_all()

        print("seeding db now...")

        db.session.add_all(seller_list)
        db.session.commit()

        db.session.add_all(customer_list)
        db.session.commit()

        db.session.add_all(product_list)
        db.session.commit()

        db.session.add_all(picture_list)
        db.session.commit()

        db.session.add_all(ratings_list)
        db.session.commit()

        db.session.add_all(order_list)
        db.session.commit()

        db.session.add_all(orderline_list)
        db.session.commit()

        db.session.add_all(comments_list)
        db.session.commit()

        print("goodbye")

    except Exception as e:
        print(e)
