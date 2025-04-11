from typing import Any

from requests import post

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class ShopifyProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # FIXME: UIから設定できるようにする
            store_id = credentials.get("shopify_store_id")
            access_token = credentials.get("shopify_storefront_access_token")
            # store_id = "timon-dev"
            # access_token = "0bab106ddb2760096129a2843a386722"

            res = post(
                f"https://{store_id}.myshopify.com/api/unstable/graphql.json",
                json={"query": "{ __type(name: \"App\") { name } }"},
                headers={
                    "X-Shopify-Storefront-Access-Token": access_token,
                    "Content-Type": "application/json",
                },
            )
            r = res.json()
            print(r)
            if "errors" in r:
                raise Exception(f"Error: {r['errors']}")
            pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
