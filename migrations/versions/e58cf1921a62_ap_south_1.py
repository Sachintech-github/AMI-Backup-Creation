"""ap-south-1

Revision ID: e58cf1921a62
Revises: 
Create Date: 2023-11-25 12:40:26.025308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58cf1921a62'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('aws_region', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('retention_period_days', sa.Integer(), nullable=False))

    with op.batch_alter_table('instance', schema=None) as batch_op:
        batch_op.alter_column('ami_name',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('instance', schema=None) as batch_op:
        batch_op.alter_column('ami_name',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_column('retention_period_days')
        batch_op.drop_column('aws_region')

    # ### end Alembic commands ###