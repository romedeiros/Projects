class Restaurant < ApplicationRecord
  belongs_to :category
  has_many :product_categories
  has_many :orders
  has_many :restaurant_rate
  
  validates :name, :delivery_tax, :city, :neighborhood, :street, :number, presence: true
  
  has_one_attached :image

  extend FriendlyId
  friendly_id :name, use: :slugged
end
