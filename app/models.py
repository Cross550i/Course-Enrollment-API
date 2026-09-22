from database import Base
from sqlalchemy import Integer, String, ForeignKey, Table, Column, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime



#промежуточная таблица-связка
enrollment_association = Table(
    "enrollment",
    Base.metadata,
    Column("student_id", ForeignKey("students.id", ondelete="CASCADE"), primary_key=True),
    Column("course_id", ForeignKey("course.id"), onupdate="CASCADE", primary_key=True)
)


class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    max_student: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime] = mapped_column(server_default=func.now())

    students: Mapped[list["Student"]] = relationship(secondary=enrollment_association, back_populates="course")


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    course: Mapped[list["Course"]] = relationship(secondary=enrollment_association, back_populates="students")
