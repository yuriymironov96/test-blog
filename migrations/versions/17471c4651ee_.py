"""empty message

Revision ID: 17471c4651ee
Revises: 2a3727a88607
Create Date: 2016-08-19 16:01:03.326481

"""

# revision identifiers, used by Alembic.
revision = '17471c4651ee'
down_revision = '2a3727a88607'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###