"""Add azureapi service

Revision ID: 0ec1c67a9b31
Revises: 3a883d3ec0f6
Create Date: 2026-04-13 15:53:10.328616

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy.orm as orm
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0ec1c67a9b31"
down_revision: Union[str, None] = "3a883d3ec0f6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    azure_id = session.execute(
        sa.text("SELECT id FROM platforms WHERE name = 'Azure'")
    ).scalar_one()

    session.execute(
        sa.text(
            """
            INSERT INTO platform_services (name, platform_id, result_string_template, technical_info_template)
            VALUES ('azureapi', :platform_id, :result_template, :technical_info_template)
            """
        ),
        {
            "platform_id": azure_id,
            "result_template": "Azure API",
            "technical_info_template": "https://portal.azure.com/#@ImecInternational.onmicrosoft.com/resource/subscriptions/{subscription_id}/resourceGroups/rg-adp-common/providers/Microsoft.ApiManagement/service/{api_manager}/overview",
        },
    )
    session.commit()


def downgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    session.execute(
        sa.text(
            """
            DELETE FROM platform_services WHERE name = 'azureapi'
            """
        )
    )

    session.commit()
