object SpaceAge {
  def onEarth(age: Double): Double = age / 31557600: Double

  def onVenus(age: Double): Double = onEarth(age) / 0.61519726: Double

  def onMercury(age: Double): Double = onEarth(age) / 0.2408467: Double

  def onMars(age: Double): Double = onEarth(age) / 1.8808158: Double

  def onJupiter(age: Double): Double = onEarth(age) / 11.862615: Double

  def onSaturn(age: Double): Double = onEarth(age) / 29.447498: Double

  def onUranus(age: Double): Double = onEarth(age) / 84.016846: Double

  def onNeptune(age: Double): Double = onEarth(age) / 164.79132: Double
}
