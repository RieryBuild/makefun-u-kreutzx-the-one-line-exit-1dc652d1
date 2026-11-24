import os

LINE = "I, the night nurse, resign \u2014 the printer jammed on this letter four times, which I choose to interpret as management's final feedback."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
