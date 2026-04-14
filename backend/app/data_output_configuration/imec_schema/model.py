from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.data_output_configuration.base_model import BaseTechnicalAssetConfiguration


class ImecSchemaTechnicalAssetConfiguration(BaseTechnicalAssetConfiguration):
    __tablename__ = "imec_schema_technical_asset_configurations"

    schema: Mapped[str] = mapped_column(String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "ImecSchemaTechnicalAssetConfiguration",
    }
