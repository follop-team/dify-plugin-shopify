# Shopify

[Project Repo](https://github.com/chekun/dify-plugin-shopify)

## Overview

A tool in Dify that helps you interact with Shopify store data 🔧

## Implemented Tools
  
  - Query product information from your store

## Configuration

### 1. Get Store ID

After logging into the Shopify admin panel, the store ID is the part shown in the URL as illustrated below.

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/store_id.png?raw=true)

### 2. Create Store App and Get Admin API Access Token

> If you already have a store app, you can skip this step or create a new one.

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_1.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_2.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_3.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_4.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_5.png?raw=true)

> When setting access scopes, only select necessary permissions, such as read access to products for now.

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_6.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_7.png?raw=true)

### 3. Enter Store ID and Access Token in Dify

Click on plugins, click on the Shopify tool, then click on set authorization.

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/auth.png?raw=true)

### 4. Using the Tool

Use according to your needs

> For example, you can have AI analyze your product icons, product titles and descriptions, and whether product prices can be optimized, etc.

Example response for querying product information:

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

You can use transformation nodes to extract or integrate the data needed for the next process node.

If you have additional data needs, you can [create an issue]((https://github.com/chekun/dify-plugin-shopify)) in the project.