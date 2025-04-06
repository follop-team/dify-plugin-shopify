# Shopify Dify プラグイン

## 概要

Dify で Shopify の店舗データと対話できるツール🔧

## 実装済みのツール

- 店舗の製品情報を問い合わせる機能

## 設定方法

### 1. 店舗IDの取得

Shopifyの管理画面にログインし、URLの中に表示されている以下の部分が店舗IDです。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/store_id.png?raw=true)

### 2. 店舗アプリを作成し、管理APIのアクセストークンを取得

> すでに店舗アプリが存在する場合は、この手順をスキップしてもOKです。新しく作成しても構いません。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_1.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_2.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_3.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_4.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_5.png?raw=true)

> アクセス権限を設定する際は、必要な権限のみを選択すればOKです。たとえば現在は「商品情報の読み取り」だけで十分です。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_6.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_7.png?raw=true)

### 3. 店舗IDとアクセストークンをDifyに入力

プラグインをクリックし、「Shopify」ツールを選択して「設定」→「認証」をクリックします。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/auth.png?raw=true)

### 4. ツールの使用

必要に応じて自由に使用できます。

> 例：AIに製品画像、タイトル、説明文、価格などを分析させて、改善の余地があるかをチェックすることも可能です。

#### 製品情報を問い合わせた場合の返却例：

```json
{
  "text": "",
  "files": [],
  "json": [
    {
      "createdAt": "2023-07-01T05:54:08Z",
      "description": "this is description",
      "descriptionHtml": "<p>this is <strong>description</strong></p>",
      "featuredMedia": {
        "preview": {
          "image": {
            "url": "https://cdn.shopify.com/s/files/1/0784/6720/3389/products/Main_b13ad453-477c-4ed1-9b43-81f3345adfd6.jpg?v=1688190848"
          }
        }
      },
      "handle": "the-collection-snowboard-liquid",
      "media": [
        {
          "mediaContentType": "IMAGE",
          "preview": {
            "image": {
              "url": "https://cdn.shopify.com/s/files/1/0784/6720/3389/products/Main_b13ad453-477c-4ed1-9b43-81f3345adfd6.jpg?v=1688190848"
            }
          }
        }
      ],
      "onlineStoreUrl": null,
      "priceRangeV2": {
        "maxVariantPrice": {
          "amount": "749.95",
          "currencyCode": "CNY"
        },
        "minVariantPrice": {
          "amount": "749.95",
          "currencyCode": "CNY"
        }
      },
      "status": "ACTIVE",
      "title": "The Collection Snowboard: Liquid",
      "updatedAt": "2025-03-17T08:31:13Z",
      "variants": [
        {
          "displayName": "The Collection Snowboard: Liquid - Default Title",
          "image": null,
          "price": "749.95"
        }
      ]
    }
  ]
}
```

次のプロセスステップで必要なデータを抽出または統合するには、データ変換ノードを使用してください。

追加のデータニーズがある場合は、[Issueをプロジェクトに提出](https://github.com/chekun/dify-plugin-shopify)してください。

---

翻訳や表現を少しカスタマイズしたい場合は、気軽に言ってくださいね。
