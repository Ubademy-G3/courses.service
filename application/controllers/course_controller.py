from fastapi import HTTPException
from domain.course_model import (Course, CoursePatch)
from application.serializers.course_serializer import CourseSerializer
from application.use_cases.course import (create,get,update,delete)


class CourseController:
    @classmethod
    async def create_course(self,args):

        new_course = Course(
            id = args.id,
            name = args.name,
            description = args.description,
            category = args.category,
            kind = args.kind,
            subscription_type = args.subscription_type,
            location = args.location
        )
        await create.add_course(new_course)
        return CourseSerializer.serialize(new_course)

    @classmethod
    async def get_all_courses(self):
        return await get.get_all_courses()

    @classmethod
    async def update_course(self, course_id, update_args):
        course_to_update = await get.get_course_by_id(course_id)
        if not course_to_update:
            raise HTTPException(status_code=404, detail="Course {} not found".format(course_id))
        
        course_in_db = Course(**course_to_update)
        if update_args.name is not None:
            course_in_db.name = update_args.name
        
        if update_args.description is not None:
            course_in_db.description = update_args.description

        if update_args.hashtags is not None:
            course_in_db.category = update_args.category
        
        if update_args.kind is not None:
            course_in_db.kind = update_args.kind
        
        if update_args.subscription_type is not None:
            course_in_db.subscription_type = update_args.subscription_type

        if update_args.location is not None:
           course_in_db.location = update_args.location
                
        update_data = course_in_db.dict(exclude_unset=True)
        updated_course = course_in_db.copy(update=update_data)
        await update.update_course(course_id, updated_course)
        return CourseSerializer.serialize(updated_course)

    @classmethod
    async def delete_course_by_id(self, course_id):
        return await delete.delete_course_by_id(course_id)
        
    @classmethod
    async def delete_all_courses(self):
        return await delete.delete_all_courses()