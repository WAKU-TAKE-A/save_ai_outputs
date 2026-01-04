from pathlib import Path

# ============================================================
# Configuration (AI-editable)
# ============================================================

# Output directory name.
# Generative AI MAY change this value if needed.
OUTPUT_DIR_NAME = "contents_code"

# ------------------------------------------------------------
# Generated contents
# ------------------------------------------------------------
# Generative AI MAY output ONLY this dictionary when requested.
# Keys   : output file names
# Values : file contents (Markdown, code, documents, etc.)
#
# If this dictionary is empty, no files will be generated.
contents_code = {
    "hoge1.md": r"(hoge1 content)",
    "hoge2.md": r"(hoge2 content)",
}

# ============================================================
# Implementation (usually unchanged)
# ============================================================

def main():
    output_dir = Path(__file__).resolve().parent / OUTPUT_DIR_NAME
    output_dir.mkdir(exist_ok=True)

    for name, content in contents_code.items():
        path = output_dir / name
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()
