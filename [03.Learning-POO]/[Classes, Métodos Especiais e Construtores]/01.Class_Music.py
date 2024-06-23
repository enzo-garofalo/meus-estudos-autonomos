class Music:
  musics = []

  def __init__(self, name, artist, time):
      self.name = name
      self.artist = artist
      self.time = time
      Music.musics.append(self)

  def __str__(self):
      return f'{self. name}\n \
               {self.artist}\n \
               {self.time}'
  def show():
      for music in Music.musics:
          print(music)
  
song1 = Music('Gold digger', 'Kanye West', '3.10')
song2 = Music('Not Like Us', 'Kendrick Lamar', '5.50')
song3 = Music('Without Me', 'Eminem', '4.18')

Music.show()