import importlib.util
import sys
from pathlib import Path

plugin_path = Path(__file__).parent.parent / "efficiency-nodes-comfyui" / "py" / "bnk_adv_encode.py"
if not plugin_path.exists():
    raise ImportError("\033[31mPlease install [efficiency-nodes-comfyui] first!!!\033[0m")

spec = importlib.util.spec_from_file_location("bnk_adv_encode", plugin_path)
module = importlib.util.module_from_spec(spec)
sys.modules["bnk_adv_encode"] = module
spec.loader.exec_module(module)

AdvancedCLIPTextEncode = getattr(module, "AdvancedCLIPTextEncode")

NODE_CLASS_MAPPINGS = {
    "AdvancedCLIPTextEncode": AdvancedCLIPTextEncode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AdvancedCLIPTextEncode": "Advanced CLIP Text Encode",
}