def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_home(client):
    response = client.get('')
    assert response.status_code == 200
    response = client.get('/info/')
    assert response.status_code == 200
    assert 'info/home.html' in (t.name for t in response.templates)


def test_help(client):
    response = client.get('/help/')
    assert response.status_code == 200
    response = client.get('/info/help/')
    assert response.status_code == 200
    assert 'info/help.html' in (t.name for t in response.templates)


def test_about(client):
    response = client.get('/about/')
    assert response.status_code == 200
    response = client.get('/info/about/')
    assert response.status_code == 200
    assert 'info/about.html' in (t.name for t in response.templates)
