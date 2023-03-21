from models.gift import GiftModel
from models.comment import CommentModel

gifts_list = [
	GiftModel(name="roses", price=12.50, in_stock=True, rating=4.6, status="delivered", img="https://img.ltwebstatic.com/images3_pi/2022/11/12/1668222257610097076ce6f3844335dce1b1f70d50.webp", user_id=1),
	GiftModel(name="lily", price=10.90, in_stock=True, rating=4.8, status="ordered", img="https://img.ltwebstatic.com/images3_pi/2022/12/21/16715926353eb2cca17ad614bce86dfd2ae0c1978a_thumbnail_900x.webp", user_id=1),
	GiftModel(name="tulip", price=9.99, in_stock=False, rating=3.4, status="order dispached", img="https://img.ltwebstatic.com/images3_pi/2022/08/23/1661236810e0350362116eccd943ff5f3fc58e3442_thumbnail_900x.webp", user_id=1),
    GiftModel(name="bike", price=500.00, in_stock=True, rating=4.4, status="order dispached", img="https://pedegoelectricbikes.com/wp-content/uploads/2022/08/Avenue-ST-Carribean-Blue-Mags.jpg;%20?%3E", user_id=1),
    GiftModel(name="winter hat", price=60.99, in_stock=True, rating=4.6, status="order dispached", img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG3XXCvN2ZvA3B4FL6aBzBPbXLKmFE4N1KSauR_KUFU2F7kZAma4TYclJXORUFnjD4rSw&usqp=CAU", user_id=1),
    GiftModel(name="scarfe", price=100.99, in_stock=True, rating=4.7, status="ordered", img="https://cdn.shopify.com/s/files/1/0876/3374/products/cressida-pure-cashmere-pashmina-rose-10_1200x.jpg?v=1669307847", user_id=1),
    GiftModel(name="hat", price=70.99, in_stock=True, rating=4.2, status="ordered", img="https://img.ltwebstatic.com/images3_pi/2021/07/16/1626424184a0602e7fadf931ca5432fe9d962f08f6_thumbnail_900x.webp", user_id=1),
    GiftModel(name="red roses", price=20.99, in_stock=True, rating=4.9, status="", img="https://www.hauteflorist.co.uk/images/products/755ab4dc01b5f084f126ab7c9f04646b.png", user_id=1),
    GiftModel(name="pink roses", price=17.99, in_stock=True, rating=4.1, status="", img="https://i.pinimg.com/originals/ef/46/b5/ef46b5511c5af4e1af6855eed3e0879d.jpg", user_id=1),
    GiftModel(name="purple roses", price=16.00, in_stock=True, rating=4.6, status="", img="https://thumbs.dreamstime.com/z/purple-natural-roses-background-49440307.jpg", user_id=1),
    GiftModel(name="white orchid", price=25.99, in_stock=True, rating=3.4, status="", img="https://www.google.com/aclk?sa=l&ai=DChcSEwj628STo7D9AhWJ3FEKHeSTDhUYABAFGgJ3cw&sig=AOD64_1zWZzAQ2nq6Y2VsZqlLOY7FgFACw&adurl&ctype=5&ved=2ahUKEwj41bmTo7D9AhWmricCHTjBBDUQvhd6BAgBEFo", user_id=1),
    GiftModel(name="saphire ring", price=1999.00, in_stock=True, rating=4.7, status="", img="https://cdn.shopify.com/s/files/1/2094/5289/products/star_pt_oval_position1_blue-saph_plain_64dcbfa7-5bd2-4449-932f-8f219bbfd3fd.png?v=1670695171&width=768", user_id=1),
    GiftModel(name="diamond ring", price=5000.00, in_stock=True, rating=5.0, status="", img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAT5gdT0RwtQZqjeeNCxrYh9PcIx8gLgFuqHaY-RXj_mrON0Sd0p8KzqsuMa2iQVWt770&usqp=CAU", user_id=1),
    GiftModel(name="brilliant earth ring", price=2000.00, in_stock=True, rating=4.9, status="", img="https://image.brilliantearth.com/blogprod/news/wp-content/uploads/2018/11/29000433/Pinterest-Pic-Reina.jpg", user_id=1),
    GiftModel(name="strawberry fruit necklace", price=1500.00, in_stock=True, rating=4.8, status="", img="https://m.media-amazon.com/images/I/41R-I5eDmaL._UY625_.jpg", user_id=1),
]

comments_list = [CommentModel(content="This is a great gift", gift_id=1, user_id=1)]
