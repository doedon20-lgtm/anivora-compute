import os


class Config:
    APP_NAME = "AniVora Compute"
    VERSION = "0.1.0"

    HOST = os.getenv(
        "ANIVORA_COMPUTE_HOST",
        "0.0.0.0"
    )

    PORT = int(
        os.getenv(
            "ANIVORA_COMPUTE_PORT",
            "8100"
        )
    )

    DATA_DIR = os.getenv(
        "ANIVORA_COMPUTE_DATA",
        "data"
    )
