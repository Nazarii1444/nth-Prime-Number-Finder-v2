from fastapi.routing import APIRouter
auth_router = APIRouter()


SECRET_KEY = "thequickbrownfoxjumpedoverthelazydog"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@auth_router.post('/login')
async def login(request):
    ...
