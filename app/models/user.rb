class User < ApplicationRecord
  has_many :items, through: :user_items
  has_many :events
  has_many :villagers, through: :user_villagers
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
end
