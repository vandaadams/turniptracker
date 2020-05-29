class VillagersController < ApplicationController
  def index
    @villagers = Villager.all
  end

  private def serialize_villager(villager)
   {
     villager: {
       id: villager.id,
       image_url: villager.get_image_url(),
       name: villager.name,
       catch_phrase: villager.catch_phrase
     }
   }
 end
end
