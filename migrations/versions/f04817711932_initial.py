"""initial

Revision ID: f04817711932
Revises: 61e242ebafb4
Create Date: 2023-08-20 10:07:18.696463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f04817711932'
down_revision: Union[str, None] = '61e242ebafb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
