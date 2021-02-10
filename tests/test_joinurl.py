from .commun import get_innov
import innov 


def test_join_url():
    
    def join (base):
        assert innov.util.join_url(base, "/1") == base + "/1"
        assert innov.util.join_url(base, "/1/") == base + "/1/"

        assert innov.util.join_url(base, "1") == base + "/1"
        assert innov.util.join_url(base, "1/") == base + "/1/"

        assert innov.util.join_url(base, "/1", "/2") == base + "/1/2"
        assert innov.util.join_url(base, "/1/", "/2/") == base + "/1/2/"

        assert innov.util.join_url(base, "1", "2") == base + "/1/2"
        assert innov.util.join_url(base, "1/", "2/") == base + "/1/2/"

    join("https://local.host")
    #join("https://local.host/")
    join("local.host")
    #join("local.host/")



test_join_url()