from fastapi import HTTPException
from domain.course_media_model import CourseMedia
from application.use_cases.create import *
from application.use_cases.get import *
from application.use_cases.update import *
from application.use_cases.delete import *

class CourseMediaController:
    @classmethod
    async def create_course_media(self,args):

        new_course_media = CourseMedia(
            id = args.id,
            course_id = args.course_id,
            url = args.url
        )
        await add_course_media(new_course_media)
        return {
            "id": args.id,
            "course_id": args.course_id,
            "url": args.url
        }

    @classmethod
    async def get_all_courses_media(self):
        return await get_all_courses_media()

    @classmethod
    async def update_course_media(self, course_media_id, update_args):
        media_to_update = await get_course_media_by_id(course_media_id)
        if not media_to_update:
            raise HTTPException(status_code=404, detail="Media {course_media_id} not found")
        
        course_media_in_db = CourseMedia(**media_to_update)
        if update_args.url is not None:
            course_media_in_db.url = update_args.url
                
        update_data = course_media_in_db.dict(exclude_unset=True)
        updated_course_media = course_media_in_db.copy(update=update_data)
        return await update_course_media(course_media_id, updated_course_media)

    @classmethod
    async def delete_course_media_by_id(self, media_id):
        return await delete_course_media_by_id(media_id)
        
    @classmethod
    async def delete_all_courses_media(self):
        return await delete_all_courses_media()