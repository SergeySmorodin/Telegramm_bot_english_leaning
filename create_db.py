from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

# Модель для таблицы words
class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    target_word = Column(String(255), nullable=False)
    translate_word = Column(String(255), nullable=False)

# Модель для таблицы user_words
class UserWord(Base):
    __tablename__ = 'user_words'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    word_id = Column(Integer, ForeignKey('words.id'), nullable=False)
    passed_word = Column(Boolean, default=False, nullable=False)

# Модель для таблицы ignore_words
class IgnoreWord(Base):
    __tablename__ = 'ignore_words'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    word_id = Column(Integer, ForeignKey('words.id'), nullable=False)

# Модель для таблицы another_words
class AnotherWord(Base):
    __tablename__ = 'another_words'

    id = Column(Integer, primary_key=True)
    other_word = Column(String(255), nullable=False)


# Создаем базу данных
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Вставка данных в таблицу words
words_data = [
    ('apple', 'яблоко'),
    ('book', 'книга'),
    ('cat', 'кот'),
    ('dog', 'собака'),
    ('house', 'дом'),
    ('car', 'машина'),
    ('tree', 'дерево'),
    ('water', 'вода'),
    ('food', 'еда'),
    ('friend', 'друг'),
]

for target_word, translate_word in words_data:
    word = Word(target_word=target_word, translate_word=translate_word)
    session.add(word)

# Вставка данных в таблицу another_words
another_words_data = [
    'pear', 'notebook', 'bird', 'hare', 'apartment', 'bicycle',
    'scooter', 'wardrobe', 'bag', 'shoes', 'hairstyle', 'printer',
    'bear', 'giraffe', 'store', 'brick', 'crocodile',
    'gas mask', 'sunset', 'sea', 'beach', 'mouse', 'flowers',
    'palm tree', 'pineapple', 'clock', 'bush',
]

for other_word in another_words_data:
    another_word = AnotherWord(other_word=other_word)
    session.add(another_word)

session.commit()
session.close()

