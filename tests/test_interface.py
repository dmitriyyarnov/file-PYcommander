import unittest
import subprocess

class TestCLI(unittest.TestCase):
    def run_cmd(self, args):
        result = subprocess.run(
            ["python", "main.py"] + args,
            capture_output=True,
            text=True
        )
        return result

    def test_help(self):
        result = self.run_cmd(["--help"])
        self.assertIn("Команды", result.stdout)

    def test_copy_error(self):
        result = self.run_cmd(["copy", "none.txt", "dst.txt"])
        self.assertIn("не является файлом", result.stdout)


if __name__ == "__main__":
    unittest.main()
