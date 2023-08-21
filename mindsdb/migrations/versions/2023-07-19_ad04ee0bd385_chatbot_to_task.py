"""chatbot_to_task

Revision ID: ad04ee0bd385
Revises: a57506731839
Create Date: 2023-07-19 16:18:14.791761

"""
from alembic import op
import sqlalchemy as sa
import mindsdb.interfaces.storage.db # noqa

# revision identifiers, used by Alembic.
revision = 'ad04ee0bd385'
down_revision = 'a57506731839'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat_bots', schema=None) as batch_op:
        batch_op.drop_column('chat_engine')
        batch_op.drop_column('user_class')
        batch_op.drop_column('company_id')
        batch_op.drop_column('is_running')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat_bots', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_running', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('company_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('user_class', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('chat_engine', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###