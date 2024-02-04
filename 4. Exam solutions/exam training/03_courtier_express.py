kg_delivery = float(input())
type_of_delivery = input()
distance_in_km = int(input())
cent = 0
price = 0
extra_kg = 0
extra_km = 0
total_extra = 0
if kg_delivery < 1:
    cent = 3
elif 1 <= kg_delivery < 10:
    cent = 5
elif 10 <= kg_delivery < 40:
    cent = 10
elif 40 <= kg_delivery < 90:
    cent = 15
elif 90 <= kg_delivery < 150:
    cent = 20

if type_of_delivery == "standard":
    price = distance_in_km * (cent / 100)
    print(f"The delivery of your shipment with weight of {kg_delivery:.3f} kg. would cost {price:.2f} lv.")
elif type_of_delivery == "express":
    if kg_delivery < 1:
        extra_kg = 0.8 * cent / 100
        extra_km = extra_kg * kg_delivery
        total_extra = distance_in_km * extra_km
    elif 1 <= kg_delivery < 10:
        extra_kg = 0.4 * cent / 100
        extra_km = extra_kg * kg_delivery
        total_extra = distance_in_km * extra_km
    elif 10 <= kg_delivery < 40:
        extra_kg = 0.05 * cent / 100
        extra_km = extra_kg * kg_delivery
        total_extra = distance_in_km * extra_km
    elif 40 <= kg_delivery < 90:
        extra_kg = 0.02 * cent / 100
        extra_km = extra_kg * kg_delivery
        total_extra = distance_in_km * extra_km
    elif 90 <= kg_delivery < 150:
        extra_kg = 0.01 * cent / 100
        extra_km = extra_kg * kg_delivery
        total_extra = distance_in_km * extra_km

    price = distance_in_km * (cent / 100) + total_extra
    print(f"The delivery of your shipment with weight of {kg_delivery:.3f} kg. would cost {price:.2f} lv.")
