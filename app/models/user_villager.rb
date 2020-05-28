class UserVillager < ApplicationRecord
  belongs_to :user
  belongs_to :villager
end
