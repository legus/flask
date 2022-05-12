from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from aplicacion.app import db

class Libros(db.Model):
	"""Libros"""
	__tablename__ = 'libros'
	id = Column(Integer, primary_key=True)
	titulo = Column(String(200),nullable=False)
	descripcion = Column(String(200),nullable=False)
	editorial = Column(String(200),nullable=False)
	paginas = Column(Integer)
	annio = Column(Integer)
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))