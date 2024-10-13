from django.shortcuts import render

nombres = [
    "Spider-Man",
    "Iron Man",
    "Thor",
    "Hulk",
    "Black Widow",
    "Captain America",
    "Doctor Strange",
    "Superman",
    "Batman",
    "Wonder Woman",
    "The Flash",
    "Aquaman",
    "Green Lantern",
    "Cyborg",
]


def mostrar_lista(request):
    return render(request, "index.html", {"nombres": nombres})
