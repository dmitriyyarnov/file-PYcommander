import unittest
import shutil
from pathlib import Path
from core.copy import copy_file
from core.delete import delete_path
from core.count import count_files
from core.search import search_files

class TestCoreFunctions(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_data")
        self.test_dir.mkdir(exist_ok=True)
        (self.test_dir / "file1.txt").write_text("Hello")
        (self.test_dir / "file2.log").write_text("Log")
        (self.test_dir / "subdir").mkdir(exist_ok=True)
        (self.test_dir / "subdir" / "file3.txt").write_text("Subdir")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy_file(self):
        dst = self.test_dir / "copy.txt"
        copy_file(self.test_dir / "file1.txt", dst)
        self.assertTrue(dst.exists())

    def test_delete_file(self):
        f = self.test_dir / "file2.log"
        delete_path(f)
        self.assertFalse(f.exists())

    def test_count_files(self):
        self.assertEqual(count_files(self.test_dir), 3)

    def test_search_files(self):
        result = search_files(self.test_dir, r".*\.txt")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
