from .commun import get_innov, response_keys

api = get_innov()


class TestAuth(object):
    def test_sign_in(self):
        assert len(api.get_token_hash()) == 498, "Fail authentication"

    def test_token_refresh(self):
        assert len(api.get_refresh_token()) == 498, "Fail token refresh"

    def test_logout(self):
        response = api.logout()
        assert response['Success']