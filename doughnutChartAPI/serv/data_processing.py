from pydantic import BaseModel

class Data(BaseModel):
    label: list[str]
    values: list[float]

class DataVisual(Data) :
    color: dict[str]
    figsize: tuple[int]
    title: str