class TestHelloWorld(object):

    def test_helloworld_response(self, app, client):
        response = client.get('/helloworld')

        assert response.json is not None
        assert response.status_code == 200
        assert response.json['msg'] == 'Hello World!'
