from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import remove_query_param, replace_query_param


class SelectorPagination(PageNumberPagination):
    """
    Наш стандарный класс пагинатор

    Attributes:
        page_size (int): Дефолтный размер страницы
        page_size_query_param (str): Параметр, отвечающий за размер страницы
        max_page_size (int): Максимальный размер страницы
    """
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100

    def get_next_link(self):
        """
        Функция получения следующей страницы
        """
        if not self.page.has_next():
            return None
        url = self.get_url(self.request)
        page_number = self.page.next_page_number()
        return replace_query_param(url, self.page_query_param, page_number)

    def get_previous_link(self):
        """
        Функция получения предыдущей страницы
        """
        if not self.page.has_previous():
            return None
        url = self.get_url(self.request)
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return remove_query_param(url, self.page_query_param)
        return replace_query_param(url, self.page_query_param, page_number)

    def get_url(self, request):
        """
        Функция сбора нового урла, чтобы он ссылался не на текущий инстанс, а на миксер
        """
        return 'http://127.0.0.1/' + request.path
