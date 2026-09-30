import platform
import shutil
import subprocess


class GPUManager:

    def __init__(self):
        self.gpu_available = False
        self.gpus = []

        self.refresh()

    def refresh(self):

        self.gpu_available = False
        self.gpus = []

        nvidia_smi = shutil.which(
            "nvidia-smi"
        )

        if not nvidia_smi:
            return

        try:

            result = subprocess.run(
                [
                    nvidia_smi,
                    "--query-gpu=index,name,"
                    "memory.total,memory.used,"
                    "memory.free,utilization.gpu",
                    "--format=csv,noheader,nounits"
                ],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode != 0:
                return

            for line in result.stdout.strip().splitlines():

                if not line.strip():
                    continue

                parts = [
                    item.strip()
                    for item in line.split(",")
                ]

                if len(parts) < 6:
                    continue

                self.gpus.append(
                    {
                        "index": int(parts[0]),
                        "name": parts[1],
                        "memory_total_mb": int(parts[2]),
                        "memory_used_mb": int(parts[3]),
                        "memory_free_mb": int(parts[4]),
                        "utilization_percent": int(parts[5])
                    }
                )

            self.gpu_available = (
                len(self.gpus) > 0
            )

        except Exception:
            self.gpu_available = False
            self.gpus = []

    def status(self):

        self.refresh()

        return {
            "gpu_available": self.gpu_available,
            "gpu_count": len(self.gpus),
            "gpus": self.gpus,
            "platform": platform.platform()
        }


gpu_manager = GPUManager()
