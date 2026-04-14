from typing import Any, ClassVar, Literal, Optional

from sqlalchemy.orm import Session

from app.data_output_configuration.base_schema import (
    AssetProviderPlugin,
    PlatformMetadata,
    UIElementMetadata,
    UIElementType,
)
from app.data_output_configuration.data_output_types import DataOutputTypes
from app.data_output_configuration.imec_schema.model import (
    ImecSchemaTechnicalAssetConfiguration as ImecSchemaTechnicalAssetConfigurationModel,
)


class ImecSchemaTechnicalAssetConfiguration(AssetProviderPlugin):
    name: ClassVar[str] = "ImecSchemaTechnicalAssetConfiguration"
    version: ClassVar[str] = "1.0"

    configuration_type: Literal[DataOutputTypes.ImecSchemaTechnicalAssetConfiguration]
    schema: str = ""

    _platform_metadata = PlatformMetadata(
        display_name="Schema",
        icon_name="databricks-logo.svg",
        platform_key="imec_databricks",
        parent_platform=None,
        detailed_name="Schema",
        result_label="Resulting schema",
        result_tooltip="The schema you can access through this technical asset",
    )

    class Meta:
        orm_model = ImecSchemaTechnicalAssetConfigurationModel

    def validate_configuration(self, data_product: Any, db: Any) -> None:
        pass

    def get_configuration(self, configs: list) -> Optional[None]:
        return None

    @classmethod
    def get_ui_metadata(cls, db: Session) -> list[UIElementMetadata]:
        base_metadata = super().get_ui_metadata(db)
        base_metadata += [
            UIElementMetadata(
                name="schema",
                type=UIElementType.String,
                label="Schema",
                tooltip="The name of the schema to give access to",
                required=True,
            ),
        ]
        return base_metadata
