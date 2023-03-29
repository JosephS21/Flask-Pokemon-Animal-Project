"""Pokemon table

Revision ID: 0b444a8731e6
Revises: cfa020f2d371
Create Date: 2023-03-04 20:27:33.113107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b444a8731e6'
down_revision = 'cfa020f2d371'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pokemon_name', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('ability', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('pokemon_name_key', type_='unique')
        batch_op.create_unique_constraint(None, ['pokemon_name'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('name')
        batch_op.drop_column('description')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('pokemon_name_key', ['name'])
        batch_op.drop_column('user_id')
        batch_op.drop_column('ability')
        batch_op.drop_column('pokemon_name')

    # ### end Alembic commands ###