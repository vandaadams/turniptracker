class Villager < ApplicationRecord
  has_many :users, through: :user_villagers
end
