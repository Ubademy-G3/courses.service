from fastapi import HTTPException
from domain.course_model import Course
from application.use_cases.create import *
from application.use_cases.get import *
from application.use_cases.update import *

class CourseController:
    @classmethod
    async def create_course(self,args):

        new_course = Course(
            id = args.id,
            name = args.name,
            description = args.description,
            hashtags = args.hashtags,
            kind = args.kind,
            subscription_type = args.subscription_type,
            location = args.location
        )
        await add_course(new_course)
        return {
            "id": args.id,
            "name": args.name,
            "description": args.description,
            "hashtags": args.hashtags,
            "kind": args.kind,
            "subscription_type": args.subscription_type,
            "location": args.location
        }

    @classmethod
    async def get_all_courses(self):
        return await get_all_courses()

    @classmethod
    async def update_course(self, course_id, update_args):
        course_to_update = await get_course_by_id(course_id)
        if not course_to_update:
            raise HTTPException(status_code=404, detail="Course {course_id} not found")
        update_data = update_args.dict(exclude_unset=True)
        course_in_db = Course(**course_to_update)

        updated_course = course_in_db.copy(update=update_data)
        return await update_course(course_id, updated_course)
        