class Config:
    DB_NAME = 'blog'
    DB_USER_NAME = 'blog_user'
    DB_PASSWORD = 'blog_password'
    DB_HOST = 'localhost'
    DB_URL = f'postgresql+psycopg2://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
