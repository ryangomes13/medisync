import unittest
from src.main import MedicamentoManager

class TestMediSync(unittest.TestCase):
    def setUp(self):
        self.manager = MedicamentoManager()

    def test_adicao_sucesso(self):
        # Caminho Feliz
        resultado = self.manager.adicionar_medicamento("Aspirina", "08:00")
        self.assertTrue(resultado)
        self.assertEqual(len(self.manager.listar_medicamentos()), 1)

    def test_adicao_invalida(self):
        # Entrada Inválida
        resultado = self.manager.adicionar_medicamento("", "")
        self.assertFalse(resultado)

    def test_lista_vazia_inicial(self):
        # Caso Limite
        self.assertEqual(len(self.manager.listar_medicamentos()), 0)

if __name__ == "__main__":
    unittest.main()
