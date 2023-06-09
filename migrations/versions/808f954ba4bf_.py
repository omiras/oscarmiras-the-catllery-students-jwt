"""empty message

Revision ID: 808f954ba4bf
Revises: a7e42cbcecb0
Create Date: 2023-05-20 12:24:28.158115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '808f954ba4bf'
down_revision = 'a7e42cbcecb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cat')
    # ### end Alembic commands ###
