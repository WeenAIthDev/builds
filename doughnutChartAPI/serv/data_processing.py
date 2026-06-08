from pydantic import BaseModel

class Data(BaseModel):
    label: list[str]
    values: list[float]

class DataVisual(Data) :
    color: dict[str, str]
    figsize: tuple[int, int]
    title: str