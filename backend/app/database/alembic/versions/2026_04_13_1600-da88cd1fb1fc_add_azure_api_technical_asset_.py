"""Add azure api technical asset configuration table

Revision ID: da88cd1fb1fc
Revises: 0ec1c67a9b31
Create Date: 2026-04-13 16:00:17.558766

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from app.shared.model import utcnow

# revision identifiers, used by Alembic.
revision: str = 'da88cd1fb1fc'
down_revision: Union[str, None] = '0ec1c67a9b31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "azure_api_technical_asset_configurations",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("data_output_configurations.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("api_name", sa.String(), nullable=False),
        sa.Column("api_type", sa.String(), nullable=False, server_default="Platform-managed"),
        sa.Column("rate_limiting_enabled", sa.Boolean(), nullable=False, server_default="true"),
        sa.Column("max_replicas", sa.Integer(), nullable=True),
        sa.Column("max_requests_per_minute", sa.Integer(), nullable=True),
        sa.Column("base_url", sa.String(), nullable=True),
        sa.Column("created_on", sa.DateTime(timezone=False), server_default=utcnow()),
        sa.Column("updated_on", sa.DateTime(timezone=False), onupdate=utcnow()),
        sa.Column("deleted_at", sa.DateTime(timezone=False), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("azure_api_technical_asset_configurations")
