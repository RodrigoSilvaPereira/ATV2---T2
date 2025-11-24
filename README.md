# FastAPI TDD Project - Phase GREEN

Projeto desenvolvido com FastAPI utilizando Test-Driven Development (TDD).  
**Branch: Main** - Implementação completa das funcionalidades para passar em todos os testes.

## 🚀 Funcionalidades Implementadas

- ✅ `GET /` - Endpoint raiz
- ✅ `GET /items/{item_id}` - Buscar item por ID
- ✅ `GET /items/` - Listar todos os items
- ✅ `POST /items/` - Criar novo item
- ✅ `PUT /items/{item_id}` - Atualizar item existente
- ✅ `DELETE /items/{item_id}` - Deletar item

## 🧪 Testes

Todos os testes implementados na fase RED agora passam:

- Teste de sucesso (status 200)
- Teste de falha (status 404 com mensagem específica)
- Testes CRUD completos

## 📋 Como executar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt