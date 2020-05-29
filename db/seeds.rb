# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

# fake data for user, items and events

ITEMS = ["Apple", "Bamboo", "Tarantula", "Pear", "Shell Rug", "Gold"]
CATEGORIES = ["fruit", "fish", "bug", "recipe", "decoration", "resource"]

puts "Clearing database"
Villager.destroy_all
Event.destroy_all
Item.destroy_all
User.destroy_all


puts "Creating user"
user = User.create!(email: "tester@test.com", password: "123123", username: "Tester", island: "Testland")

puts "Creating items"
10.times do
  Item.create!(name: ITEMS.sample, category: CATEGORIES.sample)
end

puts "Creating events"
5.times do
  Event.create!(name: "Test Event", date: "1/5/2020 16:00", description: "This is a description", user: user)
end

# gets data from API call to create villagers
require 'json'
require 'open-uri'

url = 'http://acnhapi.com/v1/villagers'
buffer = open(url).read
result = JSON.parse(buffer)

puts "Creating villagers"
names = []
catchphrases = []
images = []

result.keys.each do |villager|
  names << result[villager]['name']['name-EUen']
  catchphrases << result[villager]['catch-phrase']
  images << result[villager]['image_uri']
end

# creates villagers
for i in 0...names.count
  v = Villager.create!(name: names[i], catch_phrase: catchphrases[i])
  v.image.attach(io: URI.open(images[i]), filename: 'image.png', content_type: 'image/png')
  v.save!
end
