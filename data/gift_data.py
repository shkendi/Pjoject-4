from models.gift import GiftModel
from models.comment import CommentModel

gifts_list = [
	GiftModel(name="roses", price=12.50, in_stock=True, rating=4.6, status="delivered", img="https://img.ltwebstatic.com/images3_pi/2022/11/12/1668222257610097076ce6f3844335dce1b1f70d50.webp", user_id=1),
	GiftModel(name="lily", price=10.90, in_stock=True, rating=4.8, status="ordered", img="https://img.ltwebstatic.com/images3_pi/2022/12/21/16715926353eb2cca17ad614bce86dfd2ae0c1978a_thumbnail_900x.webp", user_id=1),
	GiftModel(name="tulip", price=9.99, in_stock=False, rating=3.4, status="order dispached", img="https://img.ltwebstatic.com/images3_pi/2022/08/23/1661236810e0350362116eccd943ff5f3fc58e3442_thumbnail_900x.webp", user_id=1)
]

comments_list = [CommentModel(content="This is a great gift", gift_id=1, user_id=1)]
