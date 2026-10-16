

from fastapi import FastAPI

app = FastAPI()


books = [
    {
        "title":"Атлантика",
        "author":"Андрэ Иолан",
        "genre":"научная фантастика"




    },
    {
        "title": "Расследование Дьяка",
        "author": "Антон Гиров",
        "genre": "Детектив"

    },
{
        "title": "Пространство",
        "author": "Александр Мостовов",
        "genre": "Научная фантастика"

    },



]

@app.get("/")
def get_info():
    return {

        "message":"API Books",
        "endpoint":"/books"
    }
@app.get("/books")
def get_artefacts():
    return books



