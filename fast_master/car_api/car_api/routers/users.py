from fastapi import APIRouter, status


router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
async def list_users():
    return {
        'users': [
            {
                'id': 1,
                'username': 'pycodebr',
                'email': 'pycodebr@gmail.com',
            },
            {
                'id': 2,
                'username': 'joao',
                'email': 'joao@gmail.com',
            },
            {
                'id': 3,
                'username': 'mario',
                'email': 'mario@gmail.com',
            },
        ]
    }

