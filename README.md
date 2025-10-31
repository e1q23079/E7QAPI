# E7QAPI

## API ドキュメント

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 概要

このリポジトリは `main.py` から起動する簡単なスクリプト/API を想定しています。

## セットアップと実行例

PowerShell の例:

```powershell
# 任意：仮想環境を作る
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1

# 実行
python main.py
```

Bash / WSL の例:

```bash
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

## 環境変数（.env）

```ini
APIKEY=
```

## データファイルについて

```json
{
    "<code>": {
        "message": "sample message"
    }
}
```
