from pydantic import BaseModel


class Model(BaseModel):
    a: int
    b: float
    c: str


if __name__ == '__main__':
    model = Model(a=3.000, b='2.72', c=b'binary data')
    print(model.model_dump())
