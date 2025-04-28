from typing import Any

from requests import post

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class ShopifyProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            store_id = credentials.get("shopify_store_id")
            access_token = credentials.get("shopify_storefront_access_token")

            res = post(
                f"https://{store_id}.myshopify.com/api/2025-07/graphql.json",
                json={"query": "{ __type(name: \"App\") { name } }"},
                headers={
                    "X-Shopify-Storefront-Access-Token": access_token,
                    "Content-Type": "application/json",
                },
                verify=False
            )
            r = res.json()
            print(r)
            if "errors" in r:
                raise Exception(f"Error: {r['errors']}")
            pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
