# from sqlalchemy.types import TypeDecorator, CHAR
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
from . import db
from dataclasses import dataclass

@dataclass
class Project(db.Model):
    id: int
    title: str
    hbu_filename: str
    start_price: str
    end_price: str
    vsu: float
    msu: float
    date: str
    # price_level_zero: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    hbu_filename = db.Column(db.Text, nullable=False, default='')
    start_price = db.Column(db.Text, nullable=False, default='')
    end_price = db.Column(db.Text, default='')
    vsu = db.Column(db.Float, nullable=False, default=0.0)
    msu = db.Column(db.Float, nullable=False, default=0.0)
    date = db.Column(db.Text, default='')
    # price_level_zero = db.Column(db.Text, nullable=False)
    products = db.relationship('InitData', backref='project', lazy=True)
    # zero_price_level = db.relationship('ZeroPriceLevel', backref='project', lazy=True)
    
UserProjects = db.Table('UserProjects',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)    

# A generic user model that might be used by an app powered by flask-praetorian
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    roles = db.Column(db.Text, default='User')
    is_active = db.Column(db.Boolean, default=True, server_default='true')
    projects = db.relationship('Project', secondary=UserProjects, lazy='subquery',
        backref=db.backref('users', lazy=True))

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active

# class ZeroPriceLevel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sku_name = db.Column(db.Text, unique=True, nullable=False)
#     zero_percent = db.Column(db.Float, nullable=False)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

@dataclass
class InitData(db.Model):
    id: int
    sku_name: str
    is_active: bool
    company: bool
    group_brand: str
    group_size: int
    group_segments: str
    group_manufacturer: str
    group_sub_brand: str
    base_sop: float
    old_sop: float
    new_sop: float
    base_volume_share: float
    old_volume_share: float
    new_volume_share: float
    base_wd: float
    # old_wd: float
    new_wd: float
    sales: float
    base_price: float
    new_price: float
    base_size: float
    # old_size: float
    new_size: float
    index_volume_share: float
    base_value_sales: float
    base_value_share: float
    new_value_sales: float
    diff_value_sales: float
    new_value_share: float
    # revenue: float
    project_id: int
    base_vat: float
    new_vat: float
    base_retailer_margin: float
    new_retailer_margin: float
    base_distributor_margin: float
    new_distributor_margin: float
    base_gross_net: float
    new_gross_net: float
    base_cogs_sku: float
    new_cogs_sku: float
    
    id = db.Column(db.Integer, primary_key=True)
    sku_name = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    company = db.Column(db.Boolean)
    group_brand = db.Column(db.Text, nullable=False)
    group_size = db.Column(db.Integer)
    group_segments = db.Column(db.Text, nullable=False)
    group_manufacturer = db.Column(db.Text, nullable=False)
    group_sub_brand = db.Column(db.Text)
    base_sop = db.Column(db.Float)
    old_sop = db.Column(db.Float)
    new_sop = db.Column(db.Float)
    base_volume_share = db.Column(db.Float)
    old_volume_share = db.Column(db.Float)
    new_volume_share = db.Column(db.Float)
    base_wd = db.Column(db.Float)
    # old_wd = db.Column(db.Float)
    new_wd = db.Column(db.Float)
    sales = db.Column(db.Float)
    base_price = db.Column(db.Float, nullable=False)
    new_price = db.Column(db.Float, nullable=False)
    base_size = db.Column(db.Float)
    # old_size = db.Column(db.Float)
    new_size = db.Column(db.Float)
    index_volume_share = db.Column(db.Float)
    base_value_sales = db.Column(db.Float)
    base_value_share = db.Column(db.Float)
    new_value_sales = db.Column(db.Float)
    diff_value_sales = db.Column(db.Float)
    new_value_share = db.Column(db.Float)
    # revenue = db.Column(db.Float)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    base_vat = db.Column(db.Float)
    new_vat = db.Column(db.Float)
    base_retailer_margin = db.Column(db.Float)
    new_retailer_margin = db.Column(db.Float)
    base_distributor_margin = db.Column(db.Float)
    new_distributor_margin = db.Column(db.Float)
    base_gross_net = db.Column(db.Float)
    new_gross_net = db.Column(db.Float)
    base_cogs_sku = db.Column(db.Float)
    new_cogs_sku = db.Column(db.Float)



# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sku_name = db.Column(db.Text, unique=True, nullable=False)
#     company = db.Column(db.Integer)
#     group_brand = db.Column(db.Text, nullable=False)
#     group_size = db.Column(db.Integer)
#     group_segments = db.Column(db.Text, nullable=False)
#     group_manufacturer = db.Column(db.Text, nullable=False)
#     market_share = db.Column(db.Float)
#     wd = db.Column(db.Float)
#     sales = db.Column(db.Float)
#     base_price = db.Column(db.Text, nullable=False)
#     base_size = db.Column(db.Float)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

# class hbu_saudi(db.Model):
#     __tablename__ = 'hbu_saudi'

#     id = db.Column(db.Integer, primary_key=True)
    
#     # id = db.Column(db.Integer, primary_key=True, nullable=False)
    


# PriceLevels = db.Table('price_levels')

# hbuSaudi = db.Table('hbu_saudi')
