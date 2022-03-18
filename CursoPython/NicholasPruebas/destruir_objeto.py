class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula: ", self.titulo)
        
    # Destructor de clase
    def __del__(self):
        print("Se Borra la pelicula: ", self.titulo)
        
p = Pelicula("The Crow", 98, 1994)
