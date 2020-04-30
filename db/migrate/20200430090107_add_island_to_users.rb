class AddIslandToUsers < ActiveRecord::Migration[6.0]
  def change
    add_column :users, :island, :string
  end
end
