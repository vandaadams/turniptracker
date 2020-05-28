class CreateVillagers < ActiveRecord::Migration[6.0]
  def change
    create_table :villagers do |t|
      t.string :name
      t.string :catch_phrase

      t.timestamps
    end
  end
end
