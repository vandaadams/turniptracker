Rails.application.routes.draw do
  devise_for :users
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  root to: 'pages#home'

  resources :users, only: [:show, :edit, :update] do
    resources :items, only: [:new, :create, :update]
    resources :events, only: [:new, :create, :update]
  end

  resources :items, only: :index
  resources :events, only: :index

  get "/profile", to: 'pages#profile'
end
