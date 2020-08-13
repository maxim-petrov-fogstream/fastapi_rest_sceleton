import os


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("POSTGRES_HOST", "localhost"),
                "port": os.getenv("POSTGRES_PORT", "5432"),
                "user": os.getenv("POSTGRES_USER", "shelter"),
                "password": os.getenv("POSTGRES_PASSWORD", "shelter"),
                "database": os.getenv("POSTGRES_DB", "shelter"),
            },
        },
    },
    "apps": {
        "admin": {
            "models": ["admin.models", "aerich.models"],
            "default_connection": "default",
        },
        "users": {
            "models": ["users.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
