from auth.jwt_decoder import JWTDecoder


def test_decode_encdoded_token():
    email = "sample@email.com"
    token = JWTDecoder.encode(email)
    assert {"sub": email} == JWTDecoder.decode(token)


def test_decode_invalid_token():
    assert {} == JWTDecoder.decode(None)
