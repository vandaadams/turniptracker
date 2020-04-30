class DropUserItemsTable < ActiveRecord::Migration[6.0]
  def up
    drop_table :user_items
  end

  def down
    raise ActiveRecord::IrreversibleMigration
  end
end
