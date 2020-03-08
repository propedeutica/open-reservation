def test_passing():
    assert (1,2,3) == (1,2,3)

def test_info(client):
    response = client.get('/')
    assert response.status_code == 200
    response = client.get('/info')
    assert response.status_code == 200


def test_help(client):
    response = client.get('/help')
    assert response.status_code == 301
