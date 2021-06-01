class AddSlugToRestaurant < ActiveRecord::Migration[6.1]
  def change
    add_column :restaurants, :slug, :string
    add_index :restaurants, :slug
  end
end
