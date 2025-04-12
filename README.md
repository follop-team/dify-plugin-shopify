# Shopify Dify Tool プラグイン

## 概要

Dify で Shopify の店舗データと対話できるツール 🔧

## 実装ツール

- 店舗の製品情報を問い合わせる機能

## デバッグ手順

- 環境ファイルを作成します。

```bash
cp .env.example .env
```

- Dify のデバッグ画面から取得した情報を`.env`に貼り付けます。

```env
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=debug.dify.ai
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=1bc183af-fd11-48e7-9c19-22e26397c30d
```

- 実行します。

```bash
python -m main
```

## パッケージ化してローカルファイルとしてアップロードする

```bash
dify plugin package ./dify-plugin-shopify
```
