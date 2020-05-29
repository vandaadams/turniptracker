class PagesController < ApplicationController
  def home
    @items = Item.all
    @events = Event.all
  end
end
