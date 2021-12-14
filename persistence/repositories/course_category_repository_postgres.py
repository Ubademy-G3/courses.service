from infrastructure.db.course_category_schema import CourseCategory
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)


class CourseCategoryRepositoryPostgres:
    def add_course_category(self, db, payload):
        db.add(payload)
        db.commit()
        logger.info("New category added")
        logger.debug("Name of the new category: %s", payload.name)

    def get_course_category(self, db, category_id):
        category = db.query(CourseCategory).filter(CourseCategory.id == category_id).first()
        logger.debug("Get category with id %s", str(category_id))
        return category

    def get_all_categories(self, db):
        categories = db.query(CourseCategory).all()
        logger.debug("Getting all categories")
        return categories

    def delete_course_category(self, db, category):
        db.delete(category)
        db.commit()
        logger.debug("Delete category with id %s", category.id)
