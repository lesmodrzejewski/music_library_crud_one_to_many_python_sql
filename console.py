import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Hey")
artist_repository.save(artist_1)
artist_2 = Artist("Voo Voo")
artist_repository.save(artist_2)

album_1 = Album("samo voo voo", "rock", artist_2)
album_repository.save(album_1)
album_2 = Album("ho", "hard rock", artist_1)
album_repository.save(album_2)

pdb.set_trace()