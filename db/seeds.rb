# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

NAMES = ["Apple", "Bamboo", "Tarantula", "Pear", "Shell Rug", "Gold"]
CATEGORIES = ["fruit", "fish", "bug", "recipe", "decoration", "resource"]

puts "Clearing database"
Event.destroy_all
Item.destroy_all
User.destroy_all
Villager.destroy_all

puts "Creating user"
user = User.create!(email: "tester@test.com", password: "123123", username: "Tester", island: "Testland")

puts "Creating items"
10.times do
  Item.create!(name: NAMES.sample, category: CATEGORIES.sample)
end

puts "Creating events"
5.times do
  Event.create!(name: "Test Event", date: "1/5/2020 16:00", description: "This is a description", user: user)
end

require 'json'
require 'open-uri'

url = 'http://acnhapi.com/v1/villagers'
buffer = open(url).read
result = JSON.parse(buffer)

puts "Creating villagers"
villager_names = []
villager_catchphrase = []

result.keys.each do |villager|
  villager_names << result[villager]['name']['name-EUen']
  villager_catchphrase << result[villager]['catch-phrase']
end

for i in 0...villager_names.count
  Villager.create!(name: villager_names[i], catch_phrase: villager_catchphrase[i])
end
