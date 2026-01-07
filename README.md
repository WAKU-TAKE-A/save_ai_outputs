# save_ai_outputs.py

生成AIに **ファイル出力用の Python スクリプトそのものを生成させる** ための、
最小構成テンプレートです。
 
「生成AIの出力をどう保存するか」ではなく、  
**「保存するためのスクリプトを、生成AIに作らせる」** ことを目的としています。

---

## コンセプト

生成AIは、

- Markdown
- ソースコード
- README
- 設計書

などを生成するのが得意です。

一方で、それらを **複数ファイルとして整理して保存する** となると、
人間がスクリプトを書いたり、コピーペーストしたりしがちです。

このリポジトリでは、その作業自体を生成AIに任せます。

---

## 想定している使い方

### 1. カスタム指示で設定する

Geminiならパーソナライズ設定、ChatGPTならパーソナライズにあるカスタム指示に設定します。

設定の例：

```
以下は、生成AIにファイル出力用のPythonスクリプトそのものを生成させるための、最小構成テンプレートです。save-ai-outputs形式で出力して、と言ったらこのテンプレートを使います。特別な指示をしない限り、辞書のみを変更し、スクリプトすべてを出力するのがルールです。

スクリプト名:save_ai_outputs.py

---スクリプトの内容、始まり

from pathlib import Path

# Output directory name.
# Generative AI MAY change this value if needed.
OUTPUT_DIR_NAME = "contents_code"

# Generative AI MAY output ONLY this dictionary when requested.
# Keys   : output file names
# Values : file contents (Markdown, code, documents, etc.)
#
# If this dictionary is empty, no files will be generated.
contents_code = {
    "hoge1.md": r"(hoge1 content)",
    "hoge2.md": r"(hoge2 content)",
}

def main():
    output_dir = Path(__file__).resolve().parent / OUTPUT_DIR_NAME
    output_dir.mkdir(exist_ok=True)

    for name, content in contents_code.items():
        path = output_dir / name
        path.write_text(content, encoding="utf-8")
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()

---スクリプトの内容、終わり
```

---

### 2. プロンプトに入力する

上の「設定の例」をプロンプトに貼り付ければ、会話内ではある程度、通用します。

ただし、会話が長くなると忘れることもあります。

---

## 想定用途

* 生成AIにヘルプや設計書一式を一括生成させる
* 複数のコードファイルを一括生成させる
* ドキュメント雛形をスクリプトとして受け取る
* 生成AIの出力を「実行可能な成果物」に変換する

---

## ライセンス

MIT License


