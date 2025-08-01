"""Initial migration

Revision ID: f7eba18935ea
Revises: 
Create Date: 2025-07-23 21:18:54.368580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7eba18935ea'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=True)
    op.create_index(op.f('ix_Users_id'), 'Users', ['id'], unique=False)
    op.create_table('Records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('record_data', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Records_id'), 'Records', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Records_id'), table_name='Records')
    op.drop_table('Records')
    op.drop_index(op.f('ix_Users_id'), table_name='Users')
    op.drop_index(op.f('ix_Users_email'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###
