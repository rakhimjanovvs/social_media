from fastapi import APIRouter
from api.comment.schemas import CommentSchema
from database.commentservice import create_comment_db, get_all_or_exact_comments_db, delete_comment_db, update_comment_db


comment_router = APIRouter(prefix="/comment", tags=["CommentAPI"])


@comment_router.post("/create_comment", response_model=CommentSchema)
async def create_comment(comment: CommentSchema):
    result = create_comment(comment)
    return {"status": 1, "message": result}

@comment_router.get("/get_comments", response_model=list[CommentRead])
async def get_comments(comment: CommentSchema = Depends(create_comment_db)):
    result = get_all_or_exact_comments_db(comment)
    return {"status": 1, "message": result}

@comment_router.get("/get_comment/{comment_id}", response_model=CommentRead)
async def get_comment(comment_id: int):
    result = get_comment(comment_id)
    return {"status": 1, "message": result}

@comment_router.delete("/delete_comment/{comment_id}", response_model=CommentRead)
async def delete_comment(comment_id: int):
    result = delete_comment(comment_id)
    return {"status": 1, "message": result}

@comment_router.put("/update_comment/{comment_id}", response_model=CommentRead)
async def update_comment(comment_id: int, comment: CommentSchema):
    result = update_comment(comment_id, comment)
    return {"status": 1, "message": result}