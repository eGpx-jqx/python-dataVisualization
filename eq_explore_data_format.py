import json
import pathlib

path = pathlib.Path("resource/eq_data_30_day_m1.json")
text = path.read_text(encoding="utf-8")
load_obj = json.loads(text)

format_path = pathlib.Path("resource/eq_data_30_day_m1_format.json")
format_path.write_text(json.dumps(load_obj, indent=4), encoding="utf-8")
