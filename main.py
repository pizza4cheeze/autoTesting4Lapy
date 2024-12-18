from test_cats_by_href import TestCatsByHref
from test_cats_by_class import TestCatsByClass
from test_search_hay import TestSearchHay
from test_catalog_search import TestCatalogSearch
from test_brand_search import TestBrandSearch
from test_price_filter import TestPriceFilter
from test_no_results import TestSearchInvalidQuery

if __name__ == "__main__":
    print("Запуск тестов...")

    # Тест с поиском по href
    print("Запуск теста: 'Кошки' (по href)...")
    test_href = TestCatsByHref()
    test_href.setup()
    test_href.test()

    # Тест с поиском по class
    print("Запуск теста: 'Кошки' (по class)...")
    test_class = TestCatsByClass()
    test_class.setup()
    test_class.test()

    # Тест поиска сена с календулой
    print("Запуск теста: 'Поиск товара сена с календулой'...")
    test_hay = TestSearchHay()
    test_hay.setup()
    test_hay.test()

    # Тест поиска через кнопку "Каталог"
    print("Запуск теста: 'Поиск через кнопку Каталог'...")
    test_catalog_search = TestCatalogSearch()
    test_catalog_search.setup()
    test_catalog_search.test()

    # Тест поиска по бренду "Grandin"
    print("Запуск теста: 'Поиск по бренду Grandin'...")
    test_brand_search = TestBrandSearch()
    test_brand_search.setup()
    test_brand_search.test()

    # Тест поиска по ценовому фильтру
    print("Запуск теста: 'Поиск по ценовому фильтру'...")
    test_price_filter = TestPriceFilter()
    test_price_filter.setup()
    test_price_filter.test()

    # Тест поиска по некорректному запросу
    print("Запуск теста: 'Поиск по некорректному запросу'...")
    test_no_results = TestSearchInvalidQuery()
    test_no_results.setup()
    test_no_results.test()

    print("Все тесты выполнены.")
