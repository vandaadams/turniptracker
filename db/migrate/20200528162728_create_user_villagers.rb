class CreateUserVillagers < ActiveRecord::Migration[6.0]
  def change
    create_table :user_villagers do |t|
      t.references :user, null: false, foreign_key: true
      t.references :villager, null: false, foreign_key: true

      t.timestamps
    end
  end
end
