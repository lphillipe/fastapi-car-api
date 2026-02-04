from sqlalchemy.orm import Mapped, mapped_column

from car_api.models import Base

class User():
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)