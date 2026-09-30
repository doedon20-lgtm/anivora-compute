from pathlib import Path

from app.config import Config


class StorageManager:

    def __init__(self):

        self.base_path = (
            Path(Config.DATA_DIR)
            / "jobs"
        )

        self.base_path.mkdir(
            parents=True,
            exist_ok=True
        )

    def status(self):

        files = 0
        bytes_used = 0

        for file in self.base_path.rglob("*"):

            if file.is_file():

                files += 1

                try:
                    bytes_used += (
                        file.stat().st_size
                    )
                except OSError:
                    pass

        return {
            "path": str(
                self.base_path
            ),
            "files": files,
            "bytes": bytes_used
        }


storage_manager = StorageManager()
