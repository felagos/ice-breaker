from engine.engine_search import make_search

def get_profile_url(text: str) -> str:
    """Searches for Linkedin or twitter Profile Page."""
    return make_search(f"{text}")