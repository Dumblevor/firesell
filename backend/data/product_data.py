from models.product import ProductModel
from models.comment import CommentModel
from models.rating import RatingModel
from models.product_category import CategoryModel


category_list = [
    CategoryModel(name="Cybersecurity"),
    CategoryModel(name="Creative"),
    CategoryModel(name="Productivity"),
    CategoryModel(name="Games"),
    CategoryModel(name="Workspace management"),
    CategoryModel(name="Anti-virus"),
    CategoryModel(name="Anti-malware"),
    CategoryModel(name="VPN"),
    CategoryModel(name="Password manager"),
    CategoryModel(name="Adblocker"),
    CategoryModel(name="Digital Content"),
    CategoryModel(name="Analytics")
]


product_list = [
    ProductModel(
        name="App1",
        price=2.99,
        description="Launch your own ecommerce site in minutes",
        product_owner_ID=3,
        categories=[category_list[5]]
    ),
    ProductModel(
        name="App2",
        price=3.99,
        description="Use real-time data to convert web visitors into readers",
        product_owner_ID=1,
        categories=[category_list[2], category_list[4]]

    ),
    ProductModel(
        name="App3",
        price=555,
        description="Manage monetize, and analyze your affiliate product promotions at scale",
        product_owner_ID=2,
        categories=[category_list[1]]
    ),
]


comments_list = [
    CommentModel(content="This is a great", user_id=1, product_id=1),
    CommentModel(content="This is a great", user_id=2, product_id=3),
    CommentModel(content="This is a great", user_id=3, product_id=2)
]

ratings_list = [
    RatingModel(rating=2.3, product_id=2, rating_owner=1),
    RatingModel(rating=3.3, product_id=3, rating_owner=2),
    RatingModel(rating=4.3, product_id=1, rating_owner=3)
]