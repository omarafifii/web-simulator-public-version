"""empty message

Revision ID: f79334ee6bc0
Revises: a0324f1b870d
Create Date: 2020-12-13 18:09:34.169647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f79334ee6bc0'
down_revision = 'a0324f1b870d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hbu_saudi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_hbu_saudi'))
    )
    op.create_table('zero_price_level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku_name', sa.Text(), nullable=False),
    sa.Column('zero_percent', sa.Float(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], name=op.f('fk_zero_price_level_project_id_project')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_zero_price_level')),
    sa.UniqueConstraint('sku_name', name=op.f('uq_zero_price_level_sku_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zero_price_level')
    op.drop_table('hbu_saudi')
    # ### end Alembic commands ###