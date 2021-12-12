from infrastructure.db.course_module_schema import CourseModule
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)

class CourseModuleRepositoryPostgres():

    def add_module(self, db, payload):
        db.add(payload)
        db.commit()
        logger.info("New module added")
        logger.debug("title of the new module: %s", payload.title)


    def get_module(self, db, module_id):
        module = db.query(CourseModule).filter(CourseModule.id == module_id).first()
        logger.debug("Get module with id %s", module_id)
        return module

    
    def delete_module(self, db, module):
        db.delete(module)
        db.commit()
        logger.debug("Delete module with id %s", module.id)
        logger.info("Module deleted")


    def update_module(self, db):
        db.commit()