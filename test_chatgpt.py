import unittest
from chatgpt_test import frage_chatgpt, api_key

class TestChatGPT(unittest.TestCase):
    def test_testmodus_antwort(self):
        """Testet die simulierte Antwort im Testmodus"""
        self.assertIn("simulierte Antwort", frage_chatgpt("Testfrage"))

    def test_testmodus_key(self):
        """Stellt sicher, dass der Testmodus läuft (kein API-Key vorhanden)"""
        self.assertIsNone(api_key)

if __name__ == "__main__":
    unittest.main()
