from enum import Enum
from typing import List
from pydantic import BaseModel

class DType(str, Enum):
    NUMERIC = "numeric"
    BOOLEAN = "boolean"
    CATEGORICAL = "categorical"
    DATETIME = "datetime"
    UNKNOWN = "unknown"

class Column(BaseModel):
    column_name: str
    dtype: DType

class DatasetUploadResponse(BaseModel):
    columns: List[Column]
    row_count: int

