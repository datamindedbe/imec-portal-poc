"""Add imec_schema technical asset configuration table

Revision ID: c7d3e8f2a1b9
Revises: b3e2f1a4c8d5
Create Date: 2026-04-14 11:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from app.shared.model import utcnow

# revision identifiers, used by Alembic.
revision: str = 'c7d3e8f2a1b9'
down_revision: Union[str, None] = 'b3e2f1a4c8d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'imec_schema_technical_asset_configurations',
        sa.Column(
            'id',
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey('data_output_configurations.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        sa.Column('schema', sa.String(), nullable=True),
        sa.Column('created_on', sa.DateTime(timezone=False), server_default=utcnow()),
        sa.Column('updated_on', sa.DateTime(timezone=False), onupdate=utcnow()),
        sa.Column('deleted_at', sa.DateTime(timezone=False), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('imec_schema_technical_asset_configurations')
