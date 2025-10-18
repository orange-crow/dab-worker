from typing import Any
from dataclasses import dataclass
import json

@dataclass
class TaskMeta:
    task_id: str
    dab_image_address: str
    dab_image_tag: str
    dataset_name: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "dab_image_address": self.dab_image_address,
            "dab_image_tag": self.dab_image_tag,
            "dataset_name": self.dataset_name
        }

@dataclass
class Respond:
    task_meta: TaskMeta = None
    dataset_size: int = None
    error: str = None
    messages: dict = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_meta": self.task_meta.to_dict() if self.task_meta else None,
            "dataset_size": self.dataset_size,
            "error": self.error,
            "messages": self.messages
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
