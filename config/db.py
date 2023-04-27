from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/PruebaFastAPI")

conn = engine.connect()

Meta_data = MetaData()