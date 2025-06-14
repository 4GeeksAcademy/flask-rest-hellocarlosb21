"""empty message

Revision ID: 4cc4a1658e74
Revises: e0cc4d174882
Create Date: 2025-06-13 23:15:59.771286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cc4a1658e74'
down_revision = 'e0cc4d174882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adjunto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publicacionId', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'publicacion', ['publicacionId'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adjunto', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('publicacionId')

    # ### end Alembic commands ###
