from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

class Usuario(BaseModel):
  cpf: int
  nome: str
  data_nascimento: date


app = FastAPI()


banco = [Usuario(cpf=1234,nome="Julia",data_nascimento="1998-09-09")]

#incio
@app.get("/")
async def index():
  return {"message": "Inicio"}


#Retorna todos os usuários cadastrados
@app.get("/banco")
async def get_banco():
  return banco


#Adiciona um novo usuário e checa se ele já não pertence ao banco
@app.post("/banco")
async def up_usuario(usuario: Usuario):
  for u in banco:
    if u.cpf == usuario.cpf:
      return {"message": f"{usuario.cpf} já está cadastrado"}
  banco.append(usuario)
  return usuario

#Retorna o usuario especifico get by cpf
@app.get("/banco/{cpf}")
async def chec_usuario(cpf: int):
      for u in banco:
        if u.cpf == cpf:
          return u
        else:
          return "Usuario não pertence ao banco"