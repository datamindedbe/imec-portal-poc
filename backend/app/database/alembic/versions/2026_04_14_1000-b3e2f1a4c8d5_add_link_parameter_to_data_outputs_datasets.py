"""Add link_parameter to data_outputs_datasets

Revision ID: b3e2f1a4c8d5
Revises: da88cd1fb1fc
Create Date: 2026-04-14 10:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b3e2f1a4c8d5'
down_revision: Union[str, None] = 'da88cd1fb1fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'data_outputs_datasets',
        sa.Column('link_parameter', sa.String(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column('data_outputs_datasets', 'link_parameter')
