from DataAccessLayer.DataAccessObject.Dependencies.DTO import DTO


class DAO(DTO):
    """
    Metodo de Creación (registro) de entidad (DTO)
    """

    def create(self, dto: DTO):
        pass
    """
    Metodo de lectura de entidad (DTO) persistente
    """

    def read(self, id: int):
        pass
    """
    Lectura de Todos los Elementos T (DTO) que pertenencen al conjunto (DTO) en base de datos
    """

    def readALL(self):
        pass
    """
    Proceso de eliminacion de elemento que pertenece al conjunto (DTO),
    tal que sea identificable por un id = ID
    """

    def delete(self, id: int):
        pass
    """
    Proceso de actualizacion de entidad T,
    tal que t es elemento del conjunto DTO
    """

    def update(self, dto: DTO):
        pass
