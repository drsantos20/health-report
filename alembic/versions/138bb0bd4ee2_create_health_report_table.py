"""create health report table

Revision ID: 138bb0bd4ee2
Revises: 
Create Date: 2022-10-13 15:33:14.967126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '138bb0bd4ee2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('covid_report', sa.Column('state', sa.String))


def downgrade() -> None:
    pass
