from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):

    # campos
    id: Mapped[int] = mapped_column(primary_key=True)
    nombreUsuario: Mapped[str] = mapped_column(
        String(15), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(
        String(20), nullable=False)

    # def serialize(self):
    #   return {
    #       "id": self.id,
    #       "email": self.email,
    #       # do not serialize the password, its a security breach
    #   }


class Comentario(db.Model):

    # campos
    id: Mapped[int] = mapped_column(primary_key=True)
    descripcion: Mapped[str] = mapped_column(String(200), nullable=False)
    fechaCreacion: Mapped[date] = mapped_column(Date)
    # publicacionId:


class Adjunto(db.Model):

    # campos
    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(15), nullable=False)
    # publicacionId:


class Publicacion(db.Model):

    # campos
    id: Mapped[int] = mapped_column(primary_key=True)
    descripcion: Mapped[str] = mapped_column(String(200), nullable=False)
    fechaCreacion: Mapped[date] = mapped_column(Date)
    #usuarioId:
