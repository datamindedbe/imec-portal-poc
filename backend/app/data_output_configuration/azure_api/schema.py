from typing import Any, ClassVar, Literal, Optional
from uuid import UUID

from pydantic import field_validator
from sqlalchemy.orm import Session

from app.configuration.environments.platform_service_configurations.schemas import (
    AzureApiConfig,
)
from app.data_output_configuration.azure_api.model import (
    AzureApiTechnicalAssetConfiguration as AzureApiTechnicalAssetConfigurationModel,
)
from app.data_output_configuration.base_schema import (
    AssetProviderPlugin,
    FieldDependency,
    PlatformMetadata,
    SelectOption,
    UIElementCheckbox,
    UIElementMetadata,
    UIElementNumber,
    UIElementRadio,
    UIElementString,

)

from app.data_output_configuration.data_output_types import DataOutputTypes
from app.data_output_configuration.enums import UIElementType
from app.data_products.schema import DataProduct
from app.users.schema import User


class AzureApiTechnicalAssetConfiguration(AssetProviderPlugin):
    name: ClassVar[str] = "AzureApiTechnicalAssetConfiguration"
    version: ClassVar[str] = "1.0"

    api_name: str
    api_type: str = "Platform-managed"
    roles: list[str] = []

    @field_validator("max_replicas", "max_requests_per_minute", mode="before")
    @classmethod
    def coerce_empty_string_to_none(cls, v: Any) -> Any:
        if v == "":
            return None
        return v

    @field_validator("roles", mode="before")
    @classmethod
    def coerce_roles_to_list(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [r.strip() for r in v.split(",") if r.strip()]
        return v or []
    rate_limiting_enabled: bool = True
    max_replicas: Optional[int] = None
    max_requests_per_minute: Optional[int] = None
    base_url: Optional[str] = None

    configuration_type: Literal[DataOutputTypes.AzureApiTechnicalAssetConfiguration]

    _platform_metadata = PlatformMetadata(
        display_name="API",
        icon_name="azure-api-logo.svg",
        platform_key="azureapi",
        parent_platform="azure",
        result_label="Resulting API",
        result_tooltip="The API you can access through this technical asset",
        detailed_name="API",
        link_parameter_label="Role",
    )

    def get_link_parameter_options(self) -> list[str]:
        return self.roles

    class Meta:
        orm_model = AzureApiTechnicalAssetConfigurationModel

    def validate_configuration(self, data_product: DataProduct, db: Session):
        pass

    def on_create(self):
        pass

    @classmethod
    def get_url(
        cls, id: UUID, db: Session, actor: User, environment: Optional[str] = None
    ) -> str:
        return "https://portal.azure.com/"

    def get_configuration(
        self, configs: list[AzureApiConfig]
    ) -> Optional[AzureApiConfig]:
        """
        No filtering on API configuration as there should only be 1 entry per environment.
        """
        return next((config for config in configs), None)

    @classmethod
    def get_ui_metadata(cls, db: Session) -> list[UIElementMetadata]:
        base_metadata = super().get_ui_metadata(db)
        base_metadata += [
            UIElementMetadata(
                name="api_name",
                label="API Name",
                required=True,
                type=UIElementType.String,
                string=UIElementString(initial_value=""),
            ),
            UIElementMetadata(
                name="api_type",
                label="Type",
                required=True,
                type=UIElementType.Radio,
                radio=UIElementRadio(
                    initial_value="Platform-managed",
                    options=[
                        SelectOption(label="Platform-managed", value="Platform-managed"),
                        SelectOption(label="External", value="External"),
                    ],
                ),
            ),
            UIElementMetadata(
                name="rate_limiting_enabled",
                label="Rate Limiting Enabled",
                required=False,
                type=UIElementType.Checkbox,
                checkbox=UIElementCheckbox(initial_value=True),
            ),
            UIElementMetadata(
                name="roles",
                label="Roles (comma-separated)",
                required=False,
                type=UIElementType.String,
                string=UIElementString(initial_value=""),
                depends_on=[FieldDependency(field_name="api_type", value="Platform-managed")],
            ),
            UIElementMetadata(
                name="max_replicas",
                label="Max Replicas",
                required=False,
                type=UIElementType.Number,
                number=UIElementNumber(min=1),
                depends_on=[FieldDependency(field_name="api_type", value="Platform-managed")],
            ),
            UIElementMetadata(
                name="max_requests_per_minute",
                label="Max Requests per Minute",
                required=False,
                type=UIElementType.Number,
                number=UIElementNumber(min=1),
                depends_on=[FieldDependency(field_name="rate_limiting_enabled", value=True)],
            ),
            UIElementMetadata(
                name="base_url",
                label="Base URL",
                required=False,
                type=UIElementType.String,
                string=UIElementString(initial_value=""),
                depends_on=[FieldDependency(field_name="api_type", value="External")],
            ),
        ]
        return base_metadata
