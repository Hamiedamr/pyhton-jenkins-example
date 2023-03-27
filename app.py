import uvicorn
import fastapi as fa
from models import InputModel
app = fa.FastAPI(title='Python Jenkins Example')

@app.get('/')
async def hello():
    return "Hello"
@app.post('/')
async def post(input: InputModel):
    return input

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True, host='0.0.0.0', port=5050)