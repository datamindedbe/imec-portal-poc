from .config_schema import BaseEnvironmentPlatformServiceConfigurationDetail


class AzureApiConfig(BaseEnvironmentPlatformServiceConfigurationDetail):
    api_manager: str
    subscription_id: str
