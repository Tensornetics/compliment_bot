import unittest
from compliment_generator import generate_compliment


class TestComplimentGenerator(unittest.TestCase):
    def test_generate_compliment(self):
        compliment = generate_compliment()
        self.assertIsInstance(compliment, str)
        self.assertGreater(len(compliment), 0)


if __name__ == "__main__":
    unittest.main()
