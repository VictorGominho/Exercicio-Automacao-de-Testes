
class Test_1:

    def test_click_login_button(self, abrir_browser):
        login_page = abrir_browser
        login_page.click_login_button()
        assert login_page.is_login_page(), "Aplicação não permaneceu na mesma URL."
        assert login_page.has_login_message_error(), 'Mensagem de erro não encontrada!'


