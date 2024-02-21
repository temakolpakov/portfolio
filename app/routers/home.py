from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request
from templates import templates
from core.models import models
from messages import ru_messages as msgs

router = APIRouter()


@router.get("/")
async def home(request: Request, ):
    projects = await models.Projects.all().order_by("-ordering")
    projects_ = []
    for project in projects:
        images = await models.Images.filter(project=project, title=False).order_by("ordering")
        image_title = await models.Images.filter(project=project, title=True).first()
        if image_title:
            image_title = image_title.path
        else:
            image_title = None
        images = [image.path for image in images]
        projects_.append({
            "id": project.id,
            "name": project.name,
            "brief_description": project.brief_description,
            "description": project.description,
            "image_title": image_title,
            "images": images,

        })

    about_me = msgs.about_me

    context = {
        "request": request,
        "projects": projects_,
        "about_me": about_me
    }

    return templates.TemplateResponse(
        "home.html",
        context=context,
        status_code=200
    )
