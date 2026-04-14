from typing import Optional

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.data_output_configuration.base_model import BaseTechnicalAssetConfiguration


class AzureApiTechnicalAssetConfiguration(BaseTechnicalAssetConfiguration):
    __tablename__ = "azure_api_technical_asset_configurations"

    api_type: Mapped[str] = mapped_column(String, nullable=False, default="Platform-managed")
    rate_limiting_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    max_replicas: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    max_requests_per_minute: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    base_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "AzureApiTechnicalAssetConfiguration",
    }
