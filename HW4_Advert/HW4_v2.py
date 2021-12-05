import json


class ColorizeMixin:
    """
    Класс для смены цвета текста
    """
    
    repr_color_code = 33  

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m{self.title} | {self.price} ₽'

class Base:
    """
    Доступ к атрибутам класса с помощью точки
    """
    
    def __init__(self, object):
        self.__object__ = object
        if ('price' in lesson) is False:
            setattr(self, 'price', 0)
        for key, value in self.__object__.items():
            if key == 'price':
                self.price = value
            if isinstance(value, dict):
                value = Base(value)
            self.__dict__[key] = value

class Advert(Base, ColorizeMixin):
    """
    Проверка значения для атрибута price& Если <0, то выводится ошибка
    """
    
    @property
    def price(self):
        return self.__price
               
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("ValueError: price must be >= 0")
        self.__price = value


if __name__ == "__main__":
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)
    
    lesson_str = """{
        "title": "python",
        "price": 111,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)
    
    lesson_str = '''{
        "title": "Вельш-корги",
        "price": 111,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }'''
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)
    
    lesson_str = '''{
        "title": "Вельш-корги",
        
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }'''
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)

    lesson_str = '''{
        "title": "Вельш-корги",
        "price": -111,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }'''
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)
