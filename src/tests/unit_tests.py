from ..monster_icon import render, hash_name

def test_render():
    template = '''
    <html>
    <h1>{title}<h1>
    visites: {visits}
    </html>
    '''
    values = {
        'title': 'Pytest!',
        'visits': 32
    }
    result = render(template, values)

    assert result
    assert str(values['visits']) in result


def test_hash_name():
    name = "Jacques"
    salt = "lesel"
    salt2 = "leselbis"
    result = hash_name(name, salt)
    result2 = hash_name(name, salt2)

    assert result
    assert result != result2
