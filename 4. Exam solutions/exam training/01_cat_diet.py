fats_percent = int(input())
protein_percent = int(input())
carbos_percent = int(input())
total_calories = int(input())
water_percent = int(input())

fat_gram = (fats_percent / 100 * total_calories) / 9
protein_gram = (protein_percent / 100 * total_calories) / 4
carbos_gram = (carbos_percent / 100 * total_calories) / 4
food_grams = fat_gram + protein_gram + carbos_gram
calories_per_gram = total_calories / food_grams
calories_without_water = (100 - water_percent) / 100 * calories_per_gram
print(f"{calories_without_water:.4f}")
