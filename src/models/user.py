import uuid

from passlib.hash import bcrypt
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from src.infra.database.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    _password = Column("password", String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password: str):
        self._password = bcrypt.hash(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        return bcrypt.verify(raw_password, self._password)
