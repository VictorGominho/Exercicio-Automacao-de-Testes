

from Pages.ProductsPage import ProductsPage


class Test_3:

    def test_fazer_logout(self, abrir_browser):
        login_page = abrir_browser
        login_page.make_login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_burger_menu(), 'Menu da página principal não encontrado.'
        assert products_page.make_logout(), 'Erro ao fazer Logout.'

