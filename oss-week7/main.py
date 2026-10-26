import tools
print(tools.get_boxoffice_rank_1("20260824"))

from tools import get_movie_audience

print(f"오디세이: {get_movie_audience('20260824', '오디세이')}")
print(f"호프: {get_movie_audience('20260824', '호프')}")
print(f"없는영화: {get_movie_audience('20260824', '없는영화')}")