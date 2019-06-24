import csv
import os
import pandas as pd
import re

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
        if row[5] != "Field Tech":
            if row[7] == "Mission & 7th" and row[12] == "false":
                mission_and_seventh.append(row[0])
            if row[7] == "Lusk & Townsend" and row[12] == "false":
                lusk_and_townsend.append(row[0])
            if row[7] == "16th Ave & Geary" and row[12] == "false":
                sixteenth_and_geary.append(row[0])
            if row[7] == "5th & Brannan" and row[12] == "false":
                fifth_and_brannan.append(row[0])
            if row[7] == "Lombard & Fillmore" and row[12] == "false":
                lombard_and_fillmore.append(row[0])
            if row[7] == "Mariposa & Potrero" and row[12] == "false":
                mariposa_and_potrero.append(row[0])
            if row[7] == "3rd & Folsom" and row[12] == "false":
                third_and_folsom.append(row[0])
            if row[7] == "Pine & Montgomery (Russ Building)" and row[12] == "false":
                pine_and_montgomery.append(row[0])
            if row[7] == "Beach & Colombus" and row[12] == "false":
                beach_and_colombus.append(row[0])
            if row[7] == "Minna & 5th" and row[12] == "false":
                minna_and_fifth.append(row[0])
            if row[7] == "Union Square" and row[12] == "false":
                union_square.append(row[0])
            if row[7] == "Laguna&Haight" and row[12] == "false":
                laguna_and_haight.append(row[0])
            if row[7] == "Judah & 12th Ave" and row[12] == "false":
                judah_and_twelfth.append(row[0])
            if row[7] == "Pine & Montgomery (Russ Building)" and row[12] == "false":
                pine_and_montgomery.append(row[0])
            if row[7] == "Beach & Colombus" and row[12] == "false":
                beach_and_colombus.append(row[0])
            if row[7] == "UCSF Mission Bay" and row[12] == "false":
                ucsf_mission_bay.append(row[0])
            if row[7] == "UCSF Parnassus" and row[12] == "false":
                ucsf_parnassus.append(row[0])
            if row[7] == "Clay & Front" and row[12] == "false":
                clay_and_front.append(row[0])
            if row[7] == "16th & Mission" and row[12] == "false":
                sixteenth_and_mission.append(row[0])
            if row[7] == "Stockton & Bush" and row[12] == "false":
                stockton_and_bush.append(row[0])
            if row[7] == "California & Jones" and row[12] == "false":
                california_and_jones.append(row[0])
            if row[7] == "Civic Center" and row[12] == "false":
                civic_center.append(row[0])
            if row[7] == "Vallejo & Stockton" and row[12] == "false":
                vallejo_and_stockton.append(row[0])
            if row[7] == "Fillmore & Post" and row[12] == "false":
                fillmore_and_post.append(row[0])
            if row[7] == "Folsom & Spear" and row[12] == "false":
                folsom_and_spear.append(row[0])
            if row[7] == "Beale & Folsom" and row[12] == "false":
                beale_and_folsom.append(row[0])    
            if row[7] == "21st & Valencia" and row[12] == "false":
                twentyfirst_and_valencia.append(row[0])
            if row[7] == "Fell & Broderick" and row[12] == "false":
                fell_and_broderick.append(row[0])
            if row[7] == "10th & Market" and row[12] == "false":
                tenth_and_market.append(row[0])
            if row[7] == "Mission Rock & 4th" and row[12] == "false":
                mission_rock_and_fourth.append(row[0])
            if row[7] == "Kearny & Pine" and row[12] == "false":
                kearny_and_pine.append(row[0])
            if row[7] == "Castro & Market" and row[12] == "false":
                castro_and_market.append(row[0])
            if row[7] == "Francisco & Van Ness" and row[12] == "false":
                francisco_and_van_ness.append(row[0])
            if row[7] == "24th & Utah" and row[12] == "false":
                twentyfourth_and_utah.append(row[0])
            if row[7] == "Grove & Gough" and row[12] == "false":
                grove_and_gough.append(row[0])

mission_and_seventh_dict = {"Mission & 7th": mission_and_seventh}
fell_and_broderick_dict = {"Fell & Broderick": fell_and_broderick}
lusk_and_townsend_dict = {"Lusk & Townsend": lusk_and_townsend}
fifth_and_brannan_dict = {"5th & Brannan": fifth_and_brannan}
lombard_and_fillmore_dict = {"Lombard & Fillmore": lombard_and_fillmore}
sixteenth_and_geary_dict = {"16th & Geary": sixteenth_and_geary}
mariposa_and_potrero_dict = {"Mariposa & Potrero": mariposa_and_potrero}
third_and_folsom_dict = {"3rd & Folsom": third_and_folsom}
laguna_and_haight_dict = {"Laguna & Haight": laguna_and_haight}
judah_and_twelfth_dict = {"Judah & 12th": judah_and_twelfth}
pine_and_montgomery_dict = {"Pine & Montgomery": pine_and_montgomery}
beach_and_colombus_dict = {"Beach & Colombus": beach_and_colombus}
seventh_and_bryant_dict = {"7th & Bryant": seventh_and_bryant} 
minna_and_fifth_dict = {"Minna & 5th": minna_and_fifth}
union_square_dict = {"Union Square": union_square}
ucsf_mission_bay_dict = {"UCSF Mission Bay": ucsf_mission_bay}
ucsf_parnassus_dict = {"UCSF Parnassus": ucsf_parnassus}
clay_and_front_dict = {"Clay & Front": clay_and_front}
sixteenth_and_mission_dict = {"16th & Mission": sixteenth_and_mission}
stockton_and_bush_dict = {"Stockton & Bush": stockton_and_bush}
california_and_jones_dict = {"California & Jones": california_and_jones}
civic_center_dict = {"Civic Center": civic_center}
vallejo_and_stockton_dict = {"Vallejo & Stockton": vallejo_and_stockton}
fillmore_and_post_dict = {"Fillmore & Post": fillmore_and_post}
folsom_and_spear_dict = {"Folsom & Spear": folsom_and_spear}
beale_and_folsom_dict = {"Beale & Folsom": beale_and_folsom}
twentyfirst_and_valencia_dict = {"21st & Valenica": twentyfirst_and_valencia}
fell_and_broderick_dict = {"Fell & Broderick": fell_and_broderick}
tenth_and_market_dict = {"10th & Market": tenth_and_market}
mission_rock_and_fourth_dict = {"Mission Rock & 4th": mission_rock_and_fourth}
kearny_and_pine_dict = {"Kearny & Pine": kearny_and_pine}
castro_and_market_dict = {"Castro & Market": castro_and_market}
francisco_and_van_ness_dict = {"Francisco & Van Ness": francisco_and_van_ness}
twentyfourth_and_utah_dict = {"24th and Utah": twentyfourth_and_utah}
grove_and_gough_dict = {"Grove & Gough": grove_and_gough}     


garage_dict = {mission_and_seventh_dict == {"Mission & 7th": mission_and_seventh},
fell_and_broderick_dict == {"Fell & Broderick": fell_and_broderick},
lusk_and_townsend_dict == {"Lusk & Townsend": lusk_and_townsend},
fifth_and_brannan_dict == {"5th & Brannan": fifth_and_brannan},
lombard_and_fillmore_dict == {"Lombard & Fillmore": lombard_and_fillmore},
sixteenth_and_geary_dict == {"16th & Geary": sixteenth_and_geary},
mariposa_and_potrero_dict == {"Mariposa & Potrero": mariposa_and_potrero},
third_and_folsom_dict == {"3rd & Folsom": third_and_folsom},
laguna_and_haight_dict == {"Laguna & Haight": laguna_and_haight},
judah_and_twelfth_dict == {"Judah & 12th": judah_and_twelfth},
pine_and_montgomery_dict == {"Pine & Montgomery": pine_and_montgomery},
beach_and_colombus_dict == {"Beach & Colombus": beach_and_colombus},
seventh_and_bryant_dict == {"7th & Bryant": seventh_and_bryant} ,
minna_and_fifth_dict == {"Minna & 5th": minna_and_fifth},
union_square_dict == {"Union Square": union_square},
ucsf_mission_bay_dict == {"UCSF Mission Bay": ucsf_mission_bay},
ucsf_parnassus_dict == {"UCSF Parnassus": ucsf_parnassus},
clay_and_front_dict == {"Clay & Front": clay_and_front},
sixteenth_and_mission_dict == {"16th & Mission": sixteenth_and_mission},
stockton_and_bush_dict == {"Stockton & Bush": stockton_and_bush},
california_and_jones_dict == {"California & Jones": california_and_jones},
civic_center_dict == {"Civic Center": civic_center},
vallejo_and_stockton_dict == {"Vallejo & Stockton": vallejo_and_stockton},
fillmore_and_post_dict == {"Fillmore & Post": fillmore_and_post},
folsom_and_spear_dict == {"Folsom & Spear": folsom_and_spear},
beale_and_folsom_dict == {"Beale & Folsom": beale_and_folsom},
twentyfirst_and_valencia_dict == {"21st & Valenica": twentyfirst_and_valencia},
fell_and_broderick_dict == {"Fell & Broderick": fell_and_broderick},
tenth_and_market_dict == {"10th & Market": tenth_and_market},
mission_rock_and_fourth_dict == {"Mission Rock & 4th": mission_rock_and_fourth},
kearny_and_pine_dict == {"Kearny & Pine": kearny_and_pine},
castro_and_market_dict == {"Castro & Market": castro_and_market},
francisco_and_van_ness_dict == {"Francisco & Van Ness": francisco_and_van_ness},
twentyfourth_and_utah_dict == {"24th and Utah": twentyfourth_and_utah},
grove_and_gough_dict == {"Grove & Gough": grove_and_gough}}


if len(grove_and_gough) > 0:
    print(grove_and_gough_dict)
if len(twentyfourth_and_utah) > 0:
    print(twentyfourth_and_utah_dict)    
if len(francisco_and_van_ness) > 0:
    print(francisco_and_van_ness_dict)
if len(castro_and_market) > 0:
    print(castro_and_market_dict)    
if len(kearny_and_pine) > 0:
    print(kearny_and_pine_dict)
if len(mission_rock_and_fourth) > 0:
    print(mission_rock_and_fourth_dict)    
if len(tenth_and_market) > 0:
    print(tenth_and_market_dict)
if len(fell_and_broderick) > 0:
    print(fell_and_broderick_dict)  
if len(twentyfirst_and_valencia) > 0:
    print(twentyfirst_and_valencia_dict)
if len(beale_and_folsom) > 0:
    print(beale_and_folsom_dict)    
if len(folsom_and_spear) > 0:
    print(folsom_and_spear_dict)
if len(fillmore_and_post) > 0:
    print(fillmore_and_post_dict)    
if len(vallejo_and_stockton) > 0:
    print(vallejo_and_stockton_dict)
if len(civic_center) > 0:
    print(civic_center_dict)    
if len(california_and_jones) > 0:
    print(california_and_jones_dict)
if len(stockton_and_bush) > 0:
    print(stockton_and_bush_dict)  
if len(sixteenth_and_mission) > 0:
    print(sixteenth_and_mission_dict)
if len(clay_and_front) > 0:
    print(clay_and_front_dict)    
if len(ucsf_parnassus) > 0:
    print(ucsf_parnassus_dict)
if len(ucsf_mission_bay) > 0:
    print(ucsf_mission_bay_dict)   
if len(union_square) > 0:
    print(union_square_dict)
if len(minna_and_fifth) > 0:
    print(minna_and_fifth_dict)    
if len(beach_and_colombus) > 0:
    print(beach_and_colombus_dict)
if len(pine_and_montgomery) > 0:
    print(pine_and_montgomery_dict)  
if len(judah_and_twelfth) > 0:
    print(judah_and_twelfth_dict)
if len(laguna_and_haight) > 0:
    print(laguna_and_haight_dict)    
if len(third_and_folsom) > 0:
    print(third_and_folsom_dict)
if len(mariposa_and_potrero) > 0:
    print(mariposa_and_potrero_dict)    
if len(sixteenth_and_geary) > 0:
    print(sixteenth_and_geary_dict)
if len(lombard_and_fillmore) > 0:
    print(lombard_and_fillmore_dict)    
if len(fifth_and_brannan) > 0:
    print(fifth_and_brannan_dict)
if len(lusk_and_townsend) > 0:
    print(lusk_and_townsend_dict)  
if len(fell_and_broderick) > 0:
    print(fell_and_broderick_dict)
if len(mission_and_seventh) > 0:
    print(mission_and_seventh_dict)
