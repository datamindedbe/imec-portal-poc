from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.data_output_configuration.base_model import BaseTechnicalAssetConfiguration


class AzureApiTechnicalAssetConfiguration(BaseTechnicalAssetConfiguration):
    __tablename__ = "azure_api_technical_asset_configurations"

    api_name: Mapped[str] = mapped_column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "AzureApiTechnicalAssetConfiguration",
    }
