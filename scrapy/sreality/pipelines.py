from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from .models.models import Estate, Image, Base



class PostgreSQLPipeline:
    def __init__(self):
        self.engine = create_engine("postgresql://myuser:mypassword@postgresql:5432/mydb", echo=True)
        Base.metadata.bind = self.engine
        self.Session = sessionmaker(bind=self.engine)
        
        Base.metadata.create_all(self.engine)

        try:
            session = self.Session()
            if session.query(func.count(Estate.id)).scalar() > 0:
                session.query(Image).delete()
                session.query(Estate).delete()
                session.commit()
        except Exception as e:
            print('ERROR in pipeline initialization:', repr(e))
            raise 
        finally:
            session.close()

    def process_item(self, item, spider):
        session = self.Session()

        try:
            
            estate = Estate(title=item['title'])
            session.add(estate)
            session.flush()

            for link in item['links']:
                link = Image(link=link['href'], estate_id=estate.id)
                session.add(link)

            session.commit()
        except Exception as e:
            session.rollback()
            print('ERROR in process_item:', repr(e))
            raise 
        finally:
            session.close()

    
        return item

    