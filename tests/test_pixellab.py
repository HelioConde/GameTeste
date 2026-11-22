import base64
import io
import unittest
from unittest import mock

from PIL import Image
from tools.generate_pixellab import CHARACTERS, MOTIONS, PixelLabError, generate, parse_png


class PixelLabPipelineTests(unittest.TestCase):
    def test_supported_characters_have_animations(self):
        self.assertIn("hero", CHARACTERS)
        self.assertIn("enemy", CHARACTERS)
        for name in CHARACTERS:
            self.assertIn("run", MOTIONS[name])
            self.assertIn("attack", MOTIONS[name])

    def test_dry_run_does_not_call_api_or_need_secret(self):
        with mock.patch("tools.generate_pixellab.api_request", side_effect=AssertionError("network accessed")):
            with mock.patch.dict("os.environ", {}, clear=True):
                plan = generate("hero", "core", dry_run=True)
        self.assertEqual(plan["target"], "hero")
        self.assertIn("run", plan["motions_needed"])

    def test_base64_png_can_be_decoded_to_rgba(self):
        source = Image.new("RGB", (96, 96), (23, 45, 67))
        stream = io.BytesIO()
        source.save(stream, format="PNG")
        data = "data:image/png;base64," + base64.b64encode(stream.getvalue()).decode("ascii")
        output = parse_png({"base64": data})
        with Image.open(io.BytesIO(output)) as image:
            self.assertEqual(image.mode, "RGBA")
            self.assertEqual(image.size, (96, 96))

    def test_invalid_image_fails(self):
        with self.assertRaises(PixelLabError):
            parse_png({"base64": "incorrect"})


if __name__ == "__main__":
    unittest.main()
