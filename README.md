# Shopify

[项目代码地址](https://github.com/chekun/dify-plugin-shopify)

## 概述

在Dify中可以帮你交互Shopify店铺数据的工具🔧

## 已实现的工具
  
  - 查询产品店铺产品信息

## 配置

### 1. 获取店铺ID

登录Shopify后台，网址中如下图所示的部分，即为店铺ID.

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/store_id.png?raw=true)

### 2. 创建店铺APP并获取后台 API 访问令牌

> 如果已经存在店铺APP，可以跳过，也可以创建一个新的。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_1.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_2.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_3.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_4.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_5.png?raw=true)

> 设置访问范围的时候，只需要选择必要的权限即可，比如目前仅需给出读取产品的权限。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_6.png?raw=true)

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/app_7.png?raw=true)

### 3. 将店铺ID和访问令牌填入Dify

点击插件，点击工具 Shopify , 点击设置授权。

![](https://github.com/chekun/dify-plugin-shopify/blob/main/_assets/screenshots/auth.png?raw=true)

### 4. 使用工具

按照自己的需求使用即可

> 举个例子，可以让AI分析你的产品图标，产品标题和文案，产品价格 是否可以优化等。

查询产品信息返回示例：

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

可以使用转换节点来提取或整合下一流程节点需要的数据。

如果您有额外的数据需求，可以在项目中发起[issue](https://github.com/chekun/dify-plugin-shopify)。