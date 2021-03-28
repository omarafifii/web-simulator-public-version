"""empty message

Revision ID: adb97ce7c8ee
Revises: 081e8b4dab01
Create Date: 2021-01-27 17:48:28.883456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adb97ce7c8ee'
down_revision = '081e8b4dab01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('zero_price_level')
    op.drop_table('sqlite_stat4')
    # op.drop_table('hbu_algeria')
    # op.drop_table('hbu_saudi')
    op.drop_table('sqlite_stat1')
    # with op.batch_alter_table('init_data', schema=None) as batch_op:
    #     batch_op.add_column(sa.Column('base_cogs_sku', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('base_distributor_margin', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('base_gross_net', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('base_retailer_margin', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('group_sub_brand', sa.Text(), nullable=True))
    #     batch_op.add_column(sa.Column('new_cogs_sku', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('new_distributor_margin', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('new_gross_net', sa.Float(), nullable=True))
    #     batch_op.add_column(sa.Column('new_retailer_margin', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('init_data', schema=None) as batch_op:
        batch_op.drop_column('new_retailer_margin')
        batch_op.drop_column('new_gross_net')
        batch_op.drop_column('new_distributor_margin')
        batch_op.drop_column('new_cogs_sku')
        batch_op.drop_column('group_sub_brand')
        batch_op.drop_column('base_retailer_margin')
        batch_op.drop_column('base_gross_net')
        batch_op.drop_column('base_distributor_margin')
        batch_op.drop_column('base_cogs_sku')

    op.create_table('sqlite_stat1',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('stat', sa.NullType(), nullable=True)
    )
    op.create_table('hbu_saudi',
    sa.Column('RespondentID', sa.BIGINT(), nullable=True),
    sa.Column('RespondentWeight', sa.BIGINT(), nullable=True),
    sa.Column('ALMARAI  TR.P  480GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI  TR.P  120GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI  TR.P  240GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI  TR.P  360GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI SQ 108GX3 (2+1 FR)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI  SQ.P 432GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI SQ 216GX3 (SP.PR)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAISQ 108G BOX', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI  SQ.P  216GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI BLU 500GX2 GLASS L/C(SP', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI BLU 900GX2 GLASS(SP.PR)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI GOLD 500GX2 GLASS (SP.PR)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI GOLD 900GX2 GLASS (SP.PR)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI GLASS BLU  500GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI GLASS BLU  900GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI GLASS GOLD  500GR', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI SQ 432G (SP.PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI SQ 432GX2 (SP.PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI TR 120GX5 (1 Fr', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI TR 480GX2 (SP)', sa.FLOAT(), nullable=True),
    sa.Column('ALMARAI BLU 500GX2 GLASS(SP.PR)', sa.FLOAT(), nullable=True),
    sa.Column('LVQR  TR.P 120GR', sa.FLOAT(), nullable=True),
    sa.Column('LVQR  TR.P 480GR', sa.FLOAT(), nullable=True),
    sa.Column('LVQR  TR.P 360GR', sa.FLOAT(), nullable=True),
    sa.Column('LVQR  TR.P 240GR', sa.FLOAT(), nullable=True),
    sa.Column('LVQR TR 120GX5 (4+1 FR)', sa.FLOAT(), nullable=True),
    sa.Column('LVQR TR 480GX2(SP.PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('LVQR  TUB 200GR', sa.FLOAT(), nullable=True),
    sa.Column('LVQR  TUB 500GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW  TUB480GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW  TR.P 480GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW  TR.P 120GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW  TR.P 240GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW TR 120GX4 (S.P)', sa.FLOAT(), nullable=True),
    sa.Column('JAW TR 120GX5 (8PO)(SP)', sa.FLOAT(), nullable=True),
    sa.Column('PUCK  SQ.P 108GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK  SQ.P 216GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK  SQ.P 432GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK 500GX2 GLASS BLUE(SP.PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('PUCK 910GX2 JAR BLUE (SP.PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('PUCK GLASS BLU  240GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK GLASS BLU  500GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK GLASS BLU  910GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK GLASS BLU  1100GR', sa.FLOAT(), nullable=True),
    sa.Column('PUCK TR 120GX5 (4+1 FREE)', sa.FLOAT(), nullable=True),
    sa.Column('PUCK 650GR JAR(30% EXTR A) (BLUE)', sa.FLOAT(), nullable=True),
    sa.Column('SALIM  TR.P 120GR', sa.FLOAT(), nullable=True),
    sa.Column('PRESIDENT TR 120GX5 (4+1FR)', sa.FLOAT(), nullable=True),
    sa.Column('NADEC  TR.P 120GR', sa.FLOAT(), nullable=True),
    sa.Column('NADEC 500GX2 GLASS BLUE (SP.PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('NADEC 500GX2 GLASS GOLD (SP PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('NADEC GLASS BLU  500GR', sa.FLOAT(), nullable=True),
    sa.Column('NADEC TR 120GX5 (4+1 FREE)', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SQ 216GX3 (SP. PRICE)', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SQ 432GX2 (SP.P)', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SQ 108GX5 (SP.P)', sa.FLOAT(), nullable=True),
    sa.Column('KIRI  SQ.P 324GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI  SQ.P 432GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI  SQ.P 108GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI  SQ.P 216GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI  TUB 350GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI  TUB 500GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SQ 108GX5 (1 FREE)', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SQ 432GX3(24P)(SP.P)', sa.FLOAT(), nullable=True),
    sa.Column('KRAFT GLASS480GX2 GOLD JAR(SP)', sa.FLOAT(), nullable=True),
    sa.Column('KRAFT 870GX2GOLD JAR(SP)', sa.FLOAT(), nullable=True),
    sa.Column('PHILADELPHIA  TUB 200GR', sa.FLOAT(), nullable=True),
    sa.Column('PHILADELPHIA  TUB 300GR', sa.FLOAT(), nullable=True),
    sa.Column('PHILADELPHIA  TUB  300GR', sa.FLOAT(), nullable=True),
    sa.Column('PHILADELPHIA  TUB 500GR', sa.FLOAT(), nullable=True),
    sa.Column('PHILADELPHIA  TUB 1650GR', sa.FLOAT(), nullable=True),
    sa.Column('PHILADELPHIA  TUB  200GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW 8 PIECES 120 GR', sa.FLOAT(), nullable=True),
    sa.Column('JAW 480X2 32X2', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SP Greek Style 6p', sa.FLOAT(), nullable=True),
    sa.Column('KIRI SP Greek style 24p', sa.FLOAT(), nullable=True),
    sa.Column('KIRI Jars 240g', sa.FLOAT(), nullable=True),
    sa.Column('KIRI Jars 440g', sa.FLOAT(), nullable=True),
    sa.Column('KIRI Jars 600g', sa.FLOAT(), nullable=True),
    sa.Column('KIRI Tubs Greek style 200g', sa.FLOAT(), nullable=True),
    sa.Column('KIRI Tubs Greek style 500g', sa.FLOAT(), nullable=True),
    sa.Column('JAW Jar 240g', sa.FLOAT(), nullable=True),
    sa.Column('JAW Jar 500g', sa.FLOAT(), nullable=True),
    sa.Column('JAW Jar 900g', sa.FLOAT(), nullable=True),
    sa.Column('LVQR TR.P Organic 8p', sa.FLOAT(), nullable=True),
    sa.Column('-0.4', sa.FLOAT(), nullable=True),
    sa.Column('-0.35', sa.FLOAT(), nullable=True),
    sa.Column('-0.3', sa.FLOAT(), nullable=True),
    sa.Column('-0.25', sa.FLOAT(), nullable=True),
    sa.Column('-0.2', sa.FLOAT(), nullable=True),
    sa.Column('-0.15', sa.FLOAT(), nullable=True),
    sa.Column('-0.1', sa.FLOAT(), nullable=True),
    sa.Column('-0.05', sa.FLOAT(), nullable=True),
    sa.Column('0', sa.FLOAT(), nullable=True),
    sa.Column('0.05', sa.FLOAT(), nullable=True),
    sa.Column('0.1', sa.FLOAT(), nullable=True),
    sa.Column('0.15', sa.FLOAT(), nullable=True),
    sa.Column('0.2', sa.FLOAT(), nullable=True),
    sa.Column('0.25', sa.FLOAT(), nullable=True),
    sa.Column('0.3', sa.FLOAT(), nullable=True),
    sa.Column('0.35', sa.FLOAT(), nullable=True),
    sa.Column('0.4', sa.FLOAT(), nullable=True)
    )
    op.create_table('hbu_algeria',
    sa.Column('Respondent', sa.BIGINT(), nullable=True),
    sa.Column('RLH', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF 960G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF 600G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF MOZZARELLA 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF NOIRES OLIVES 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF CAMEMBERT300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF GREEN OLIVES 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF AIL/HERBES 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR EMTL 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF GRILLE 300G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF Nat 450G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF fromages 450G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF 3poivres 450G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF fromages 200G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR CHEF 3poivres 200G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR ORG 8TP 120G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR ORG 24P 360G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR ORG 16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR ORG 32P 480G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR EMTL 16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR EMTL 8P 120G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR EDAM 16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR EDAM 8P 120G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR SIMPLY 8P 110G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR SIMPLY 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR SIMPLY 24P 330G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR SIMPLY 32P 440G', sa.FLOAT(), nullable=True),
    sa.Column('LVQR koul youm 200G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY  8P 110G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY EDAM 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY CHED 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY  24P 330G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY  900G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY 320G', sa.FLOAT(), nullable=True),
    sa.Column('CHEEZY 480G', sa.FLOAT(), nullable=True),
    sa.Column('EL MOUTAMAYEZ 16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('EL MOUTAMAYEZ  24P 360G', sa.FLOAT(), nullable=True),
    sa.Column('EL MOUTAMAYEZ  8P 120G', sa.FLOAT(), nullable=True),
    sa.Column('LA NOUVELLE VACHE 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('LA NOUVELLE VACHE 24P 330G', sa.FLOAT(), nullable=True),
    sa.Column('LA NOUVELLE VACHE 8P 110G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE ORG  8P 120G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE ORG 16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE ORG 24P 360G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE MON FRMG Nat 150G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE  300G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE  600G', sa.FLOAT(), nullable=True),
    sa.Column('LE BERBERE  1.8KG', sa.FLOAT(), nullable=True),
    sa.Column('OKIDS  16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('OKIDS  600G', sa.FLOAT(), nullable=True),
    sa.Column('PICON  8P 110G', sa.FLOAT(), nullable=True),
    sa.Column('PICON 16P 200G', sa.FLOAT(), nullable=True),
    sa.Column('PICON 24P 330G', sa.FLOAT(), nullable=True),
    sa.Column('PICON 32P 440G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO 320G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO GOUDA 320G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO FRMG Rouge 320G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO JUNIOR 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO JUNIOR 24P 330G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO EXC. CHED 16P 240G', sa.FLOAT(), nullable=True),
    sa.Column('TARTINO EXC. CHED 24P 360G', sa.FLOAT(), nullable=True),
    sa.Column('WALID 270G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI CREME 4P 64G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI CREME 6P 96G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI CREME 12P 192G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI DELICE 350G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI DELICE 190G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI TARTINE Nat 120G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI TARTINE AIL/HERBES 120G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI GREEK 6P 90GR', sa.FLOAT(), nullable=True),
    sa.Column('KIRI GREEK BRQT 190G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI YAOUMI 6P 90G', sa.FLOAT(), nullable=True),
    sa.Column('KIRI YAOUMI 4P 60G', sa.FLOAT(), nullable=True),
    sa.Column('DIALNA 16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('TOP SOUMA16P 220G', sa.FLOAT(), nullable=True),
    sa.Column('FONDELICE CHED 125G', sa.FLOAT(), nullable=True),
    sa.Column('FONDELICE Alg. 125G', sa.FLOAT(), nullable=True),
    sa.Column('FONDELICE GRILLE 125G', sa.FLOAT(), nullable=True),
    sa.Column('FONDELICE EMTL 340G', sa.FLOAT(), nullable=True),
    sa.Column('FONDELICE Nat 340G', sa.FLOAT(), nullable=True),
    sa.Column('FONDELICE AIL/Herbes 340G', sa.FLOAT(), nullable=True),
    sa.Column('-0.5', sa.FLOAT(), nullable=True),
    sa.Column('-0.45', sa.FLOAT(), nullable=True),
    sa.Column('-0.4', sa.FLOAT(), nullable=True),
    sa.Column('-0.35', sa.FLOAT(), nullable=True),
    sa.Column('-0.3', sa.FLOAT(), nullable=True),
    sa.Column('-0.25', sa.FLOAT(), nullable=True),
    sa.Column('-0.2', sa.FLOAT(), nullable=True),
    sa.Column('-0.15', sa.FLOAT(), nullable=True),
    sa.Column('-0.1', sa.FLOAT(), nullable=True),
    sa.Column('-0.05', sa.FLOAT(), nullable=True),
    sa.Column('0', sa.FLOAT(), nullable=True),
    sa.Column('0.05', sa.FLOAT(), nullable=True),
    sa.Column('0.1', sa.FLOAT(), nullable=True),
    sa.Column('0.15', sa.FLOAT(), nullable=True),
    sa.Column('0.2', sa.FLOAT(), nullable=True),
    sa.Column('0.25', sa.FLOAT(), nullable=True),
    sa.Column('0.3', sa.FLOAT(), nullable=True),
    sa.Column('0.35', sa.FLOAT(), nullable=True),
    sa.Column('0.4', sa.FLOAT(), nullable=True),
    sa.Column('0.45', sa.FLOAT(), nullable=True),
    sa.Column('0.5', sa.FLOAT(), nullable=True)
    )
    op.create_table('sqlite_stat4',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('neq', sa.NullType(), nullable=True),
    sa.Column('nlt', sa.NullType(), nullable=True),
    sa.Column('ndlt', sa.NullType(), nullable=True),
    sa.Column('sample', sa.NullType(), nullable=True)
    )
    op.create_table('zero_price_level',
    sa.Column('sku_name', sa.TEXT(), nullable=True),
    sa.Column('zero_percent', sa.FLOAT(), nullable=True),
    sa.Column('project_id', sa.BIGINT(), nullable=True)
    )
    # ### end Alembic commands ###
