from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

product_query = """
query searchProducts($query: String!, $first: Int) {
  search(query: $query, first: $first, types: PRODUCT) {
    edges {
      node {
        ... on Product {
          id
          title
          description
          onlineStoreUrl
          totalInventory
          createdAt
          updatedAt
          featuredImage {
            src
          }
        }
      }
    }
  }
}
"""

class ShopifyGetProductTool(Tool):

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # FIXME: UIから設定できるようにする
        store_id = self.runtime.credentials.get("shopify_store_id")
        # store_id = "timon-dev"
        if not store_id:
            raise Exception("shopify_store_id is required")
        access_token = self.runtime.credentials.get("shopify_storefront_access_token")
        # access_token = "0bab106ddb2760096129a2843a386722"
        if not access_token:
            raise Exception("shopify_storefront_access_token is required")

        query = tool_parameters.get("query")
        if not query:
            raise Exception("query is required")

        res = requests.post(
            f"https://{store_id}.myshopify.com/api/unstable/graphql.json",
            json={
            "query": product_query,
            "variables": {
                "query": query,
                "first": 10,
            }
            },
            headers={
            "X-Shopify-Storefront-Access-Token": access_token,
            "Content-Type": "application/json",
            },
        )
        r = res.json()
        if "errors" in r:
            raise Exception(f"Error: {r['errors']}")

        if not r["data"]["search"]["edges"]:
            raise Exception(f"Product not found, {r}")

        print('response:', type(r), r)

        # NOTE: dict型のみ（list型は受け付けない）
        yield self.create_json_message({
            "results": r["data"]["search"]["edges"]
        })
