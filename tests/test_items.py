from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestItems:
    def test_get_existing_item_status_200(self):
        """Teste de sucesso: buscar item existente deve retornar status 200"""
        response = client.get("/items/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "Item 1"
        assert "description" in data

    def test_get_nonexistent_item_status_404(self):
        """Teste de falha: buscar item inexistente deve retornar status 404"""
        response = client.get("/items/999")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Item não existe"

    def test_get_all_items(self):
        """Teste para buscar todos os items"""
        response = client.get("/items/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3

    def test_root_endpoint(self):
        """Teste para o endpoint raiz"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data

    def test_create_item_success(self):
        """Teste para criar um novo item"""
        new_item = {"name": "Novo Item", "description": "Item criado via teste"}
        response = client.post("/items/", json=new_item)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Novo Item"
        assert data["description"] == "Item criado via teste"
        assert "id" in data

    def test_update_item_success(self):
        """Teste para atualizar um item existente"""
        update_data = {"name": "Item Atualizado"}
        response = client.put("/items/2", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Item Atualizado"
        assert data["id"] == 2

    def test_update_nonexistent_item(self):
        """Teste para atualizar um item que não existe"""
        update_data = {"name": "Item Inexistente"}
        response = client.put("/items/999", json=update_data)
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Item não existe"

    def test_delete_item_success(self):
        """Teste para deletar um item existente"""
        response = client.delete("/items/3")
        assert response.status_code == 204

        # Verifica que o item foi realmente removido
        response = client.get("/items/3")
        assert response.status_code == 404

    def test_delete_nonexistent_item(self):
        """Teste para deletar um item que não existe"""
        response = client.delete("/items/999")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Item não existe"
