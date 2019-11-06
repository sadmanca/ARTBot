"""empty message

Revision ID: fca4d39d6f19
Revises: 8386df60ac9f
Create Date: 2019-10-31 13:06:26.681806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca4d39d6f19'
down_revision = '8386df60ac9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site_vars')
    # ### end Alembic commands ###
    op.create_table('new_artpieces',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('title', sa.String(50), nullable=False),
            sa.Column('email', sa.String(50), nullable=False),
            sa.Column('submit_date', sa.DateTime(), nullable=False),
            sa.Column('art_encoding', sa.JSON(), nullable=False),
            sa.Column('submission_status'
            , sa.Enum('Submitted', 'Processing', 'Processed', name='submissionstatus')
            , nullable=False),
            sa.Column('raw_image', sa.LargeBinary(), nullable=False),
            sa.PrimaryKeyConstraint('id')
            )
    op.execute(("INSERT INTO "
                "new_artpieces(id, title, email, submit_date, art_encoding, submission_status, raw_image) "
                "SELECT id, title, email, submit_date, art, status, picture "
                "FROM artpieces"))
    op.drop_table('artpieces')
    op.execute("ALTER TABLE new_artpieces RENAME TO artpieces")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site_vars',
    sa.Column('var', sa.VARCHAR(), nullable=False),
    sa.Column('val', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('var')
    )
    # ### end Alembic commands ###
    op.create_table('new_artpieces',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('title', sa.String(), nullable=True),
            sa.Column('email', sa.String(), nullable=False),
            sa.Column('submit_date', sa.DateTime(), nullable=True),
            sa.Column('art', sa.String(), nullable=True),
            sa.Column('status', sa.String(), nullable=True),
            sa.Column('picture', sa.LargeBinary(), nullable=True),
            sa.PrimaryKeyConstraint('id')
            )
    op.execute(("INSERT INTO new_artpieces(id, title, email, submit_date, art, status, picture) "
                "SELECT "
                "id, title, email, submit_date, art_encoding, submission_status, raw_image "
                "FROM artpieces"))
    op.drop_table('artpieces')
    op.execute("ALTER TABLE new_artpieces RENAME TO artpieces")
