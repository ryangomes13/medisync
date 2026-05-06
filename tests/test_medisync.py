import unittest
import requests

class TestIntegration(unittest.TestCase):
    def test_api_connection(self):
        # Usando um endpoint estável da BrasilAPI para o teste de integração
        response = requests.get("https://brasilapi.com.br/api/banks/v1/1")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
