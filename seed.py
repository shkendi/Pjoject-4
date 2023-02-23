
from app import app, db
from models.gift import GiftModel
from models.comment import CommentModel
from models.user import UserModel
# from models.user_gift import UserGiftModel

with app.app_context():
    try:
        print("Creating our database...")
        db.drop_all()
        db.create_all()

        print("Seeding the database!")
        # ! User seeding
        user = UserModel(
            email="endi1@email.com",
            username="endi1",
            password="Letmein3?"
		)
        user.save()

        gift = GiftModel(
            name="Roses",
            price=12.50,
            in_stock=True,
            rating=4.6,
            status="delivered",
            img="https://img.ltwebstatic.com/images3_pi/2022/11/12/1668222257610097076ce6f3844335dce1b1f70d50.webp",
            user_id=user.id
        )
        gift.save()

        # hat = UserGiftModel(gift_id=gift.id, user_id=user.id)
        # hat.save()
        # user_gift = UserGiftModel(gift_id=gift.id, user_id=user.id)
        # user_gift.save()

        comment = CommentModel(content="Amazing comment.", gift_id=gift.id)
        comment.save()

        print("Database seeded!")
    except Exception as e:
        print(e)
