
from app import database


class Categoria(database.Model):

    __tablename__ = 'categorias'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(100), nullable=False)
    id_tienda = database.Column(database.Integer, nullable=False)
    activo = database.Column(database.Integer, nullable=False)

    @staticmethod
    def get_all():
        return Categoria.query.all()


    def get_by_id(id):
        return Categoria.query.filter_by(id=id).firts       
