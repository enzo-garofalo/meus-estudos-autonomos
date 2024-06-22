class Car():
  cars = []
  def __init__(self, model, color, year) -> None:
      self.model = model
      self.color = color
      self.year = year
      Car.cars.append(self)
  