import unittest
import requests

class TestIntegration(unittest.TestCase):
    def test_api_connection(self):
        """Teste de Integração: Valida se a API externa está respondendo"""
        url = "https://brasilapi.com.br/api/cptec/v1/cidade/sao-paulo"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("SÃO PAULO", response.text.upper())

if __name__ == "__main__":
    unittest.main()
