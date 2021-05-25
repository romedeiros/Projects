class CreateRestaurantRates < ActiveRecord::Migration[6.1]
  def change
    create_table :restaurant_rates do |t|
      t.integer :rate
      t.references :restaurant, null: false, foreign_key: true
      

      t.timestamps
    end
  end
end
