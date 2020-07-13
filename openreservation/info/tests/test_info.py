import pytest

def test_passing():
    assert (1, 2, 3) == (1, 2, 3)



# Testing that home works in basic and under /info and that the page is using the proper templates
def test_home(client):
    response = client.get('')
    assert response.status_code == 200

    response = client.get('/info/')
    assert response.status_code == 200
    assert 'info/home.html' in (t.name for t in response.templates)
    assert 'layout.html' in (t.name for t in response.templates)

# Testing that help works in basic and under /info and that the page is using the proper templates
def test_help(client):
    response = client.get('/help/')
    assert response.status_code == 200

    response = client.get('/info/help/')
    assert response.status_code == 200
    assert 'info/help.html' in (t.name for t in response.templates)
    assert 'layout.html' in (t.name for t in response.templates)


# Testing that about works in basic and under /info and that the page is using the proper templates
def test_about(client):
    response = client.get('/about/')
    assert response.status_code == 200
    response = client.get('/info/about/')
    assert response.status_code == 200
    assert 'info/about.html' in (t.name for t in response.templates)
    assert 'layout.html' in (t.name for t in response.templates)
