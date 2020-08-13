from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    """Модель Пользователя."""

    is_active = fields.BooleanField(default=False, description="Is Active")
    first_name = fields.CharField(
        default=False, description="Is Active", max_length=255,
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"


User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="User", exclude_readonly=True)
from tortoise import Model, fields


class Aerich(Model):
    version = fields.CharField(max_length=50)
    app = fields.CharField(max_length=20)

    class Meta:
        ordering = ["-id"]
