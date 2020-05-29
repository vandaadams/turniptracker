class VillagersController < ApplicationController
  def index
    @villagers = Villager.all
  end

  private

  def villager_params
  params.require(:villager).permit(:name, :catch_phrase, :image)
  end
end
