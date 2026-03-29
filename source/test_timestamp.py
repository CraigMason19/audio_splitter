import unittest

from source.timestamp import Timestamp

class TestTimestampParsing(unittest.TestCase):
    def test_valid_inputs(self):
        valid_inputs = [
            "16:01",
            "52:12",
            "1:2:3",
            "01:02:03",
            "12:34:56",
            "00:00",
            "23:59:59",
            "1234:59:00",
            "1234:59:0",
        ]

        for ts in valid_inputs:
            with self.subTest(ts=ts):
                obj = Timestamp.from_string(ts)
                self.assertIsInstance(obj, Timestamp)

    def test_invalid_structure(self):
        invalid_inputs = [
            "123",
            "12:34:56:78",
            "1",
            "1:",
            ":30",
            "::",
        ]

        for ts in invalid_inputs:
            with self.subTest(ts=ts):
                with self.assertRaises(ValueError):
                    Timestamp.from_string(ts)

    def test_invalid_non_numeric(self):
        invalid_inputs = [
            "aa:bb",
            "12:xx:34",
            "1:2:three",
            "--:10",
            "5:!0",
        ]

        for ts in invalid_inputs:
            with self.subTest(ts=ts):
                with self.assertRaises(ValueError):
                    Timestamp.from_string(ts)

    def test_invalid_empty(self):
        invalid_inputs = [
            "",
            " ",
            " : : ",
        ]

        for ts in invalid_inputs:
            with self.subTest(ts=ts):
                with self.assertRaises(ValueError):
                    Timestamp.from_string(ts)

    def test_invalid_negative_values(self):
        invalid_inputs = [
            "-1:10:10",
            "10:-1:10",
            "10:10:-1",
        ]

        for ts in invalid_inputs:
            with self.subTest(ts=ts):
                with self.assertRaises(ValueError):
                    Timestamp.from_string(ts)

    def test_invalid_minute_second_ranges(self):
        invalid_inputs = [
            "0:60:00",
            "0:00:60",
            "10:99:10",
            "10:10:99",
        ]

        for ts in invalid_inputs:
            with self.subTest(ts=ts):
                with self.assertRaises(ValueError):
                    Timestamp.from_string(ts)

if __name__ == "__main__":
    unittest.main()