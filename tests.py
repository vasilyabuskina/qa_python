import pytest
from main import BooksCollector
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector() # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Гордость и предубеждение и зомби') # добавляем две книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # проверяет есть ли добаленная книга в списке
    def test_add_new_book_added_book_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        assert 'Горе от ума' in collector.books_rating

    # одну и ту же книгу можно добавить только один раз
    def test_add_new_book_same_book_twice_adds_one(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Горе от ума')
        assert len(collector.get_books_rating()) == 1

    #добавляет новую книгу в словарь и выставляет ей по умолчанию рейтинг 1
    def test_add_new_book_add_book_gets_rating_1_by_default(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        assert collector.books_rating['Горе от ума'] == 1


    #проверяет валидный значения рейтинга от 1 до 10
    @pytest.mark.parametrize('rate', [1, 5, 10])
    def test_set_book_rating_from_1_to_10(self, rate):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_rating('Горе от ума', rate)
        assert collector.books_rating['Горе от ума'] == rate

    #нельзя выставить рейтинг меньше 1
    @pytest.mark.parametrize('rate', [-5, -1, 0])
    def test_set_book_rating_less_than_one_not_allowed(self, rate):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_rating('Горе от ума', rate)
        assert collector.books_rating['Горе от ума'] != rate

    #проверка добвление книги в избранное
    def test_add_book_in_favorites_add_1_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_book_in_favorites('Горе от ума')
        assert 'Горе от ума' in collector.favorites

    #книга добвляется в избранное только 1 раз
    def test_add_book_in_favorites_add_book_to_favorites_twice_adds_once(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_book_in_favorites('Горе от ума')
        collector.add_book_in_favorites('Горе от ума')
        assert len(collector.favorites) == 1

    #нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_add_not_existing_book_not_allowed(self):
        collector = BooksCollector()
        collector.add_new_book('Два капитана')
        collector.add_book_in_favorites('Горе от ума')
        assert 'Горе от ума' not in collector.favorites

    #проверка удаления книги из избранного
    def test_delete_book_from_favorites_delete_book_not_in_favourites(self):
        collector = BooksCollector()
        collector.add_new_book('Два капитана')
        collector.add_book_in_favorites('Два капитана')
        collector.delete_book_from_favorites('Два капитана')
        assert 'Два капитана' not in collector.favorites