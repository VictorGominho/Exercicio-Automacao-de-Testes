from Pages.ProductsPage import ProductsPage


class Test_2:

    def test_efetuar_login(self, abrir_browser):
        login_page = abrir_browser
        login_page.make_login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_products_page(), "Página de Produtos não encontrada."

