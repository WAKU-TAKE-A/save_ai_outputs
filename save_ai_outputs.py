from pathlib import Path

# 生成するデータを以下に都度書き込みます。
contents_code = {
    "hoge1.md": r"(hoge1の内容) ",
    "hoge2.md": r"(hoge2の内容) ",
}

def main():
    output_dir = Path(__file__).resolve().parent / "contents_code"
    output_dir.mkdir(exist_ok=True)
    for name, content in contents_code.items():
        path = output_dir / name
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()
