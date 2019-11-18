import csv
import os

unplugged_vehicle_id = []
unplugged_vehicle_location = []
unplugged_vehicle_access_group = []
unplugged_vehicle = []

csvpath = os.path.join("scooterdata.csv")

garage_list = mission_and_seventh, lusk_and_townsend, fifth_and_brannan, lombard_and_fillmore, sixteenth_and_geary, mariposa_and_potrero, third_and_folsom, laguna_and_haight, judah_and_twelfth, pine_and_montgomery, beach_and_colombus, seventh_and_bryant, minna_and_fifth, union_square, ucsf_mission_bay, ucsf_parnassus, clay_and_front, sixteenth_and_mission,stockton_and_bush, california_and_jones, civic_center, vallejo_and_stockton, fillmore_and_post, folsom_and_spear, beale_and_folsom, twentyfirst_and_valencia, fell_and_broderick, tenth_and_market, mission_rock_and_fourth, kearny_and_pine, castro_and_market, francisco_and_van_ness, twentyfourth_and_utah, grove_and_gough = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvreader)

    for row in csvreader:
        if row[5] != "Field Tech" or "RTB - Needs Truck" or "RTB - Battery":
            charge_string = row[16]
            if row[12] == "false" and charge_string != "":
                charge = float(charge_string[:3])
                if charge < 50:
                    garage = row[7]
                    vehicle_id = row[0]
                    if garage == "Mission & 7th":
                        mission_and_seventh.append(vehicle_id)
                    elif garage == "Lusk & Townsend":
                        lusk_and_townsend.append(vehicle_id)
                    elif garage == "16th Ave & Geary":
                        sixteenth_and_geary.append(vehicle_id)
                    elif garage == "5th & Brannan":
                        fifth_and_brannan.append(vehicle_id)
                    elif garage == "Lombard & Fillmore":
                        lombard_and_fillmore.append(vehicle_id)
                    elif garage == "Mariposa & Potrero":
                        mariposa_and_potrero.append(vehicle_id)
                    elif garage == "3rd & Folsom":
                        third_and_folsom.append(vehicle_id)
                    elif garage == "Pine & Montgomery (Russ Building)":
                        pine_and_montgomery.append(vehicle_id)
                    elif garage == "Beach & Colombus":
                        beach_and_colombus.append(vehicle_id)
                    elif garage == "Minna & 5th":
                        minna_and_fifth.append(vehicle_id)
                    elif garage == "Union Square":
                        union_square.append(vehicle_id)
                    elif garage == "Laguna&Haight":
                        laguna_and_haight.append(vehicle_id)
                    elif garage == "Judah & 12th Ave":
                        judah_and_twelfth.append(vehicle_id)
                    elif garage == "Beach & Colombus":
                        beach_and_colombus.append(vehicle_id)
                    elif garage == "UCSF Mission Bay":
                        ucsf_mission_bay.append(vehicle_id)
                    elif garage == "UCSF Parnassus":
                        ucsf_parnassus.append(vehicle_id)
                    elif garage == "Clay & Front":
                        clay_and_front.append(vehicle_id)
                    elif garage == "16th & Mission":
                        sixteenth_and_mission.append(vehicle_id)
                    elif garage == "Stockton & Bush":
                        stockton_and_bush.append(vehicle_id)
                    elif garage == "California & Jones":
                        california_and_jones.append(vehicle_id)
                    elif garage == "Civic Center":
                        civic_center.append(vehicle_id)
                    elif garage == "Vallejo & Stockton":
                        vallejo_and_stockton.append(vehicle_id)
                    elif garage == "Fillmore & Post":
                        fillmore_and_post.append(vehicle_id)
                    elif garage == "Folsom & Spear":
                        folsom_and_spear.append(vehicle_id)
                    elif garage == "Beale & Folsom":
                        beale_and_folsom.append(vehicle_id)    
                    elif garage == "21st & Valencia":
                        twentyfirst_and_valencia.append(vehicle_id)
                    elif garage == "Fell & Broderick":
                        fell_and_broderick.append(vehicle_id)
                    elif garage == "10th & Market":
                        tenth_and_market.append(vehicle_id)
                    elif garage == "Mission Rock & 4th":
                        mission_rock_and_fourth.append(vehicle_id)
                    elif garage == "Kearny & Pine":
                        kearny_and_pine.append(vehicle_id)
                    elif garage == "Castro & Market":
                        castro_and_market.append(vehicle_id)
                    elif garage == "Francisco & Van Ness":
                        francisco_and_van_ness.append(vehicle_id)
                    elif garage == "24th & Utah":
                        twentyfourth_and_utah.append(vehicle_id)
                    elif garage == "Grove & Gough":
                        grove_and_gough.append(vehicle_id)
print("Unplugged Vehicles\n")

print("North")
print("---------------------------------") 
if len(lombard_and_fillmore) > 0:
    print("Lombard & Fillmore: " + ', '.join(map(str, lombard_and_fillmore)))
if len(francisco_and_van_ness) > 0:    
    print("Francisco & Van Ness: " + ', '.join(map(str, francisco_and_van_ness)))
if len(beach_and_colombus) > 0:    
    print("Beach & Columbus: " + ', '.join(map(str, beach_and_colombus)))
if len(vallejo_and_stockton) > 0:    
    print("Vallejo & Stockton: " + ', '.join(map(str, vallejo_and_stockton)))

print("\n")

print("West/Central")
print("---------------------------------") 
if len(fillmore_and_post) > 0:
    print("Fillmore & Post: " + ', '.join(map(str, fillmore_and_post)))
if len(fell_and_broderick) > 0:    
    print("Fell & Broderick: " + ', '.join(map(str, fell_and_broderick)))
if len(judah_and_twelfth) > 0:    
    print("Judah & 12th: " + ', '.join(map(str, judah_and_twelfth)))
if len(ucsf_parnassus) > 0:    
    print("UCSF Parnassus: " + ', '.join(map(str, ucsf_parnassus)))

print("\n")

print("Mission/Dogpatch/Mission Bay")
print("---------------------------------") 
if len(sixteenth_and_mission) > 0:
    print("16th & Mission: " + ', '.join(map(str, sixteenth_and_mission)))
if len(twentyfirst_and_valencia) > 0:    
    print("21st & Valencia: " + ', '.join(map(str, twentyfirst_and_valencia)))
if len(twentyfourth_and_utah) > 0:    
    print("24th & Utah: " + ', '.join(map(str, twentyfourth_and_utah)))
if len(ucsf_mission_bay) > 0:    
    print("UCSF Mission Bay: " + ', '.join(map(str, ucsf_mission_bay)))
if len(mission_rock_and_fourth) > 0:    
    print("Mission Rock & 4th: " + ', '.join(map(str, mission_rock_and_fourth)))            

print("\n")

print("Financial District")
print("---------------------------------") 
if len(california_and_jones) > 0:
    print("California & Jones: " + ', '.join(map(str, california_and_jones)))
if len(clay_and_front) > 0:    
    print("Clay & Front: " + ', '.join(map(str, clay_and_front)))
if len(pine_and_montgomery) > 0:    
    print("Pine & Montgomery: " + ', '.join(map(str, pine_and_montgomery)))
if len(kearny_and_pine) > 0:    
    print("Kearny & Pine: " + ', '.join(map(str, kearny_and_pine)))
if len(union_square) > 0:    
    print("Union Square " + ', '.join(map(str, union_square)))  
if len(stockton_and_bush) > 0:    
    print("Stockton & Bush: " + ', '.join(map(str, stockton_and_bush)))               

print("\n")

print("SOMA West")
print("---------------------------------") 
if len(tenth_and_market) > 0:
    print("10th & Market: " + ', '.join(map(str, tenth_and_market)))
if len(mission_and_seventh) > 0:    
    print("Mission & 7th: " + ', '.join(map(str, mission_and_seventh)))
if len(fifth_and_brannan) > 0:    
    print("5th & Brannan: " + ', '.join(map(str, fifth_and_brannan)))
if len(minna_and_fifth) > 0:    
    print("Minna & 5th: " + ', '.join(map(str, minna_and_fifth)))

print("\n")

print("SOMA East")
print("---------------------------------") 
if len(folsom_and_spear) > 0:
    print("Folsom & Spear: " + ', '.join(map(str, folsom_and_spear)))
if len(beale_and_folsom) > 0:    
    print("Beale & Folsom: " + ', '.join(map(str, beale_and_folsom)))
if len(third_and_folsom) > 0:    
    print("3rd & Folsom: " + ', '.join(map(str, third_and_folsom)))
if len(lusk_and_townsend) > 0:    
    print("Lusk & Townsend: " + ', '.join(map(str, lusk_and_townsend)))



"""if len(judah_and_twelfth) > 0:    
     for item in map(str, judah_and_twelfth):
        item_padded = item.rjust(4)
        print(item_padded + " : Judah and Twelfth")"""
#checklist formatting           