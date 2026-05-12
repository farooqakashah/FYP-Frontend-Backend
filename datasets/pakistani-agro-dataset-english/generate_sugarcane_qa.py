import csv

qa_data = [
    # Field Preparation & Planting Method
    ("What is the optimal time for Autumn planting of sugarcane in Pakistan?", "The optimal time for Autumn sowing is from September to mid-October. This planting gives 25-30% higher yield compared to Spring planting.", "Sowing & Field Preparation"),
    ("What is the optimal time for Spring planting of sugarcane in Pakistan?", "The optimal time for Spring planting is from mid-February to the end of March.", "Sowing & Field Preparation"),
    ("How deep should sugarcane trenches be in Punjab?", "For trench planting, the trenches should be 1.5 to 2 feet deep. This helps in better root development and prevents lodging.", "Sowing & Field Preparation"),
    ("What is the recommended planting distance for sugarcane?", "The recommended row-to-row distance is 2.5 to 3 feet for flat planting, and 3.5 to 4 feet if trench planting is used.", "Sowing & Field Preparation"),
    ("Can sugarcane be intercropped during Autumn planting?", "Yes, Autumn-planted sugarcane is widely intercropped with wheat, mustard, garlic, or winter vegetables in Pakistan to maximize land use.", "Sowing & Field Preparation"),
    ("What is the 'pit planting' method?", "Pit planting involves digging circular pits and planting setts inside them. It saves water and allows maximum tillering, yielding highly.", "Sowing & Field Preparation"),
    ("How many ploughings are required for sugarcane field preparation?", "The field requires 3-4 deep ploughings followed by planking to create a fine tilth, as sugarcane has a deep root system.", "Sowing & Field Preparation"),
    ("Is deep ploughing necessary for sugarcane?", "Yes, deep ploughing using a chisel plough breaks the hardpan of the soil, promoting deeper root penetration and better nutrient uptake.", "Sowing & Field Preparation"),
    ("What is the seed rate for sugarcane planting per acre?", "For optimum plant population, use 30,000 to 40,000 setts per acre, which is roughly 80-100 maunds (3200-4000 kg) of sugarcane.", "Sowing & Field Preparation"),
    ("Should we use double-bud or triple-bud setts?", "Double-bud or triple-bud setts are highly recommended as they have a higher germination rate compared to single-bud setts.", "Sowing & Field Preparation"),
    ("How to select healthy setts for sugarcane?", "Select setts from the upper 1/3rd to 1/2 portion of an immature, healthy, and disease-free cane, as the top portion has higher glucose and moisture.", "Sowing & Field Preparation"),
    ("Why is dry planting done in some areas?", "Dry planting is done in heavy clay soils where moisture retention is high. Setts are placed in dry soil and irrigated immediately.", "Sowing & Field Preparation"),
    ("How to manage soil moisture before planting (rauni)?", "Apply a heavy pre-sowing irrigation (Rauni). When the soil reaches workable moisture (Watter condition), plough the field to prepare the seedbed.", "Sowing & Field Preparation"),
    ("What is the advantage of trench planting over flat planting?", "Trench planting saves up to 30% irrigation water, prevents lodging (falling over) of tall canes, and makes earthing up easier.", "Sowing & Field Preparation"),
    ("How to do blind hoeing in sugarcane?", "Blind hoeing is done a few days after planting before the shoots emerge. It breaks the surface crust, conserves moisture, and removes early weeds.", "Sowing & Field Preparation"),

    # Sett Treatment
    ("Why is sett treatment necessary in sugarcane?", "Sett treatment protects the sugarcane buds from soil-borne diseases (like smut and wilt) and pests (like termites) during the early germination phase.", "Seed Treatment"),
    ("What fungicide should be used for sugarcane sett treatment?", "A solution containing Thiophanate Methyl or Carbendazim (at 2 to 2.5 grams per liter of water) is highly recommended for sett dipping.", "Seed Treatment"),
    ("How long should setts be dipped in the fungicide solution?", "Setts should be dipped in the fungicidal solution for 5 to 10 minutes before planting.", "Seed Treatment"),
    ("Can we mix insecticide in sett treatment to prevent termites?", "Yes, mixing Chlorpyrifos or Imidacloprid with the fungicide solution provides excellent early protection against termites.", "Seed Treatment"),
    ("What is hot water treatment for sugarcane setts?", "Hot water treatment (50°C for 2 hours) is used by research stations and progressive farmers to eliminate internal seed-borne diseases like Grassy Shoot Virus and Ratoon Stunting Disease.", "Seed Treatment"),

    # Fertilizer Management
    ("What is the recommended NPK dose for sugarcane in Pakistan?", "A general recommendation per acre is 2.5 bags of DAP, 3 to 4 bags of Urea, and 2 bags of SOP (Sulphate of Potash).", "Fertilizer Management"),
    ("When should DAP be applied to sugarcane?", "The entire dose of Phosphorus (DAP) should be applied as a basal dose at the time of sowing in the furrows/trenches.", "Fertilizer Management"),
    ("How should Urea be split for spring sugarcane?", "Urea should be applied in 3 to 4 equal splits. The first split at germination, and subsequent splits after every 30 days, finishing before the monsoon starts.", "Fertilizer Management"),
    ("Is Potash (SOP) necessary for sugarcane?", "Yes, Potash is critical as it improves cane girth, enhances sugar recovery, and increases the plant's resistance to diseases and drought.", "Fertilizer Management"),
    ("Can we use Farm Yard Manure (FYM) for sugarcane?", "Yes, applying 3-4 trolleys of well-rotted FYM per acre about a month before sowing greatly improves soil organic matter and water retention.", "Fertilizer Management"),
    ("How to correct Zinc deficiency in sugarcane?", "Zinc deficiency causes stunted growth and broad yellowish bands on leaves. Apply 10 kg of 33% Zinc Sulphate per acre during the first or second irrigation.", "Fertilizer Management"),
    ("When to apply micronutrients to sugarcane?", "Micronutrient cocktails (containing Zinc, Iron, Boron) are best applied as foliar sprays 45-60 days after planting.", "Fertilizer Management"),
    ("How does Sulphur benefit sugarcane?", "Sulphur aids in the efficient uptake of nitrogen and helps in the accumulation of sucrose in the cane. Using SOP or Ammonium Sulphate fulfills this requirement.", "Fertilizer Management"),
    ("Should we apply fertilizer during the monsoon?", "Avoid surface broadcasting of Urea during heavy monsoon rains as it washes away. If necessary, use banding (placing near roots) when rain stops.", "Fertilizer Management"),
    ("What is the role of Phosphorous in root development of sugarcane?", "Phosphorous ensures rigorous early root development, which is essential for the crop to anchor firmly and absorb nutrients throughout its long lifecycle.", "Fertilizer Management"),
    ("How to apply liquid fertilizers in sugarcane?", "Liquid fertilizers or fertigation can be applied efficiently through drip irrigation systems, feeding nutrients directly to the root zone.", "Fertilizer Management"),
    ("What happens if excessive Urea is applied late in the season?", "Late application of Urea promotes vegetative growth at the expense of sugar accumulation. It lowers sugar recovery and makes the cane prone to lodging.", "Fertilizer Management"),
    ("Is it advisable to use bio-fertilizers in sugarcane?", "Yes, bio-fertilizers like Acetobacter or Phospho-bacteria can save up to 20% of chemical fertilizers and improve soil health.", "Fertilizer Management"),
    ("Can we top-dress Potash?", "Potash is best applied as a basal dose, but if missed, it can be top-dressed during earthing-up (Mitti charhana) stage in May or June.", "Fertilizer Management"),
    ("How to manage iron deficiency (yellowing of young leaves) in sugarcane?", "Iron deficiency (chlorosis) turns young leaves completely white/yellow. Spray 1% Iron Sulphate (Ferrous Sulphate) solution 2-3 times at weekly intervals.", "Fertilizer Management"),

    # Weed Management
    ("What is the critical period for weed competition in sugarcane?", "The first 90 to 120 days after planting are critical. Weeds must be controlled during this formative phase to avoid severe yield losses.", "Weed Management"),
    ("What pre-emergence herbicides are recommended for sugarcane?", "Spray Ametryn + Atrazine or Pendimethalin within 72 hours of planting on moist soil to prevent weed seeds from germinating.", "Weed Management"),
    ("How many days after planting should pre-emergence herbicides be sprayed?", "They must be sprayed within 2 to 3 days (48-72 hours) of planting and irrigation.", "Weed Management"),
    ("What to use for controlling broadleaf weeds in sugarcane?", "For broadleaf weeds like Bathu or Itsit, post-emergence application of 2,4-D or Dicamba 30-40 days after sowing is effective.", "Weed Management"),
    ("How to control Dila (Cyperus rotundus) in sugarcane?", "Dila (Purple Nutsedge) is a stubborn weed. Spraying Halosulfuron-methyl when Dila is in the 3-4 leaf stage provides excellent control.", "Weed Management"),
    ("What is the benefit of manual hoeing (Godi) in sugarcane?", "Hoeing not only removes weeds but also breaks soil crust, improves root aeration, and conserves moisture.", "Weed Management"),
    ("How to control grasses like Khabbal (Cynodon dactylon) in sugarcane?", "Deep ploughing during summer, manual extraction of stolons, and directed sprays of Glyphosate in severe patches (avoiding crop contact) help control Khabbal.", "Weed Management"),
    ("Can we do inter-row cultivation with tractors for weed control?", "Yes, using tractor-mounted cultivators between the wide rows (in trench planting) is an effective and fast way to control weeds.", "Weed Management"),
    ("Does trash mulching help in weed control?", "Yes, spreading dried sugarcane leaves (trash) between the rows in ratoon crops suppresses weed emergence and conserves soil moisture.", "Weed Management"),
    ("Is post-emergence weedicide effective in the rainy season?", "It is less effective if rain washes it off immediately. Ensure there is a clear window of at least 6-8 hours without rain after spraying.", "Weed Management"),

    # Irrigation Management
    ("How many total irrigations does a sugarcane crop need in Pakistan?", "In the canal-irrigated plains of Punjab and Sindh, sugarcane requires 16 to 20 irrigations throughout its lifecycle.", "Irrigation Management"),
    ("What is the critical irrigation stage for sugarcane?", "The formative phase (tillering, 60-120 days) and the grand growth phase (summer months) are highly critical for irrigation.", "Irrigation Management"),
    ("How frequently should sugarcane be irrigated in summer (May-June)?", "During peak summer (May and June), the crop should be irrigated every 10 to 12 days to prevent drought stress.", "Irrigation Management"),
    ("How to manage irrigation during the monsoon?", "Stop canal irrigation. Instead, ensure field drains are open to quickly remove excess stagnant water, which can trigger diseases.", "Irrigation Management"),
    ("What happens if sugarcane faces drought stress during tillering?", "Drought stress during tillering drastically reduces the number of tillers per plant, leading to a thin crop stand and poor yield.", "Irrigation Management"),
    ("Can sugarcane be grown on drip irrigation in Pakistan?", "Yes, drip irrigation is highly successful for sugarcane. It saves 40-50% water, allows precise fertigation, and increases yield by 20-30%.", "Irrigation Management"),
    ("How many days before harvesting should irrigation be stopped?", "Irrigation should be stopped 25 to 30 days prior to harvesting. This forces the plant to accumulate sucrose, increasing the sugar recovery rate.", "Irrigation Management"),
    ("Does waterlogging cause red rot in sugarcane?", "While it doesn't cause it directly, waterlogged conditions weaken the plant and create high humidity, which rapidly accelerates the spread of Red Rot.", "Irrigation Management"),
    ("How to practice furrow irrigation in sugarcane?", "In trench/furrow planting, water is applied only in the furrows while the ridges remain dry. This saves water and reduces weed growth on ridges.", "Irrigation Management"),
    ("Can we use brackish tube well water for sugarcane?", "Sugarcane is moderately sensitive to salinity. If brackish water must be used, mix it with canal water or apply agricultural gypsum to the soil.", "Irrigation Management"),

    # Pest Management
    ("How to control early shoot borer in sugarcane?", "Early shoot borer causes 'dead hearts'. Control it by applying granular insecticides like Furadan, Cartap, or Fipronil near the roots at 40-45 days of sowing.", "Pest Management"),
    ("What are the symptoms of stem borer in sugarcane?", "Stem borer creates holes in the internodes and tunnels inside the cane, causing red frass to fall out. The cane quality and sugar content plummet.", "Pest Management"),
    ("How to manage top borer in sugarcane?", "Top borer causes 'bunchy top' symptoms. Apply Carbofuran or Fipronil granules in the soil during June and July, followed by light irrigation.", "Pest Management"),
    ("How to control root borer in sugarcane?", "Root borer attacks underground parts. Apply Chlorpyrifos liquid with irrigation water (fertigation) as soon as symptoms appear.", "Pest Management"),
    ("What is the biological control for sugarcane borers in Pakistan?", "The release of *Trichogramma chilonis* egg parasitoid cards in the field from April to October is a highly effective, eco-friendly biological control for borers.", "Pest Management"),
    ("How to protect sugarcane from termite attack?", "Termites attack setts and roots. Treat setts with Chlorpyrifos before sowing. If attacked later, flush Chlorpyrifos or Bifenthrin with irrigation water.", "Pest Management"),
    ("How to control Pyrilla (leaf hopper) in sugarcane?", "Pyrilla sucks sap, causing leaves to yellow and excrete honeydew. It is best controlled naturally by the parasitoid *Epiricania melanoleuca*. In severe cases, spray Imidacloprid.", "Pest Management"),
    ("What is the remedy for wooly aphid in sugarcane?", "Wooly aphids appear as white fuzzy masses on leaves. Spray systemic insecticides like Thiamethoxam, Acetamiprid, or Flonicamid immediately.", "Pest Management"),
    ("How to manage scale insects in sugarcane?", "Scale insects stick to the internodes under the leaf sheath. Remove dry lower leaves (detrashing) and spray Malathion or Dimethoate.", "Pest Management"),
    ("What are the signs of pink borer in sugarcane?", "Pink borer larvae have pink bands. They attack in the later stages, boring into the stalk and making tunnels, similar to stem borers.", "Pest Management"),
    ("How to control rats/rodents in sugarcane?", "Rats destroy mature canes. Clean the field bunds and use Zinc Phosphide baits. Fumigating active burrows with Aluminum Phosphide tablets is very effective.", "Pest Management"),
    ("What causes white grubs in sugarcane and how to control them?", "White grubs live in the soil and feed on roots. Deep ploughing exposes them to birds. Apply Chlorpyrifos or Imidacloprid to the soil to kill larvae.", "Pest Management"),
    ("How to manage mite infestation on sugarcane leaves?", "Mites cause red/brown speckling on leaves during dry periods. Spray acaricides like Abamectin or Dicofol to control them.", "Pest Management"),
    ("Are pheromone traps effective for sugarcane borers?", "Yes, installing 6-8 pheromone traps per acre helps in mass trapping male borer moths and monitoring their population.", "Pest Management"),
    ("Why is trash burning discouraged for pest control?", "Burning trash kills beneficial insects (farmer friends) like Trichogramma and ladybird beetles, and destroys organic matter. Mulching is better.", "Pest Management"),
    ("How to prevent red ants in the sugarcane field?", "Red ants can damage buds. Dusting Sevin (Carbaryl) powder or applying Chlorpyrifos during field preparation prevents ant attacks.", "Pest Management"),
    ("What to do if there is a severe attack of leaf miner?", "Leaf miners create white zig-zag trails on leaves. Spray systemic insecticides like Emamectin Benzoate or Abamectin.", "Pest Management"),
    ("How to use light traps in sugarcane fields?", "Set up light traps (a bulb over a tub of soapy water) at night during April-June to attract and kill adult moths of borers.", "Pest Management"),
    ("How does crop rotation break the pest cycle of sugarcane?", "Rotating sugarcane with non-host crops like sunflower or cotton breaks the lifecycle of specialized pests like borers and soil nematodes.", "Pest Management"),
    ("Can we mix insecticides with fertilizer during top dressing?", "Yes, granular insecticides (like Fipronil or Cartap) can be mixed with Urea or sand and broadcasted near the roots during top dressing.", "Pest Management"),

    # Disease Management
    ("What is Red Rot in sugarcane and why is it dangerous?", "Red Rot is a fungal disease known as the 'cancer of sugarcane'. It completely destroys the crop, turning the inner cane red with a sour alcoholic smell.", "Disease Management"),
    ("What are the symptoms of Red Rot?", "Leaves wither from top to bottom. Splitting the cane reveals red tissues with white crossbands and it smells like fermented alcohol.", "Disease Management"),
    ("How to control Red Rot disease?", "There is no chemical cure. Grow resistant varieties (e.g., CPF-246), use healthy seed, uproot and burn infected clumps, and avoid ratooning infected fields.", "Disease Management"),
    ("What causes sugarcane smut (whip smut)?", "It is a fungal disease where the growing tip turns into a long, black, whip-like structure covered in black powdery spores.", "Disease Management"),
    ("How to control smut in sugarcane?", "Carefully cover the smut whip with a plastic bag, cut it, and burn it outside the field. Use hot water seed treatment before planting.", "Disease Management"),
    ("What is Pokkah Boeng disease in sugarcane?", "It is an airborne fungal disease causing twisted, wrinkled, and shortened leaves at the top. Spray Copper Oxychloride or Mancozeb as a preventive measure.", "Disease Management"),
    ("How to manage sugarcane rust?", "Rust causes tiny, elongated orange/brown pustules on leaves. Grow resistant varieties and spray Propiconazole or Triadimefon if symptoms appear.", "Disease Management"),
    ("What is yellow leaf disease in sugarcane?", "It is a viral disease spread by aphids, causing the midrib of the leaf to turn intense yellow. Use virus-free seed and control aphids.", "Disease Management"),
    ("How to manage Fusarium wilt in sugarcane?", "Wilt causes the cane to hollow out and dry. Ensure proper drainage, treat setts with fungicide, and do not take a ratoon from a wilt-affected crop.", "Disease Management"),
    ("What causes fruit rot or stem rot in sugarcane?", "Rotting is usually a secondary infection caused by red rot, borer holes, or prolonged waterlogging. Improve drainage and manage borers.", "Disease Management"),
    ("What is ratoon stunting disease (RSD)?", "RSD is a bacterial disease causing severely stunted growth in ratoon crops. Hot water sett treatment is the only effective control.", "Disease Management"),
    ("How to prevent red stripe disease?", "Red stripe is a bacterial infection causing long red streaks on leaves. Ensure good aeration, avoid excessive nitrogen, and remove infected canes.", "Disease Management"),
    ("Does excessive nitrogen application attract diseases?", "Yes, too much Urea makes the cane succulent and lowers immunity, making it highly susceptible to diseases like rust and pests like Pyrilla.", "Disease Management"),
    ("Can we use the same field for sugarcane every year?", "Monocropping builds up soil-borne pathogens like wilt and smut. Practice a 3-year crop rotation to keep the soil disease-free.", "Disease Management"),
    ("How does sett treatment help against red rot?", "Sett dipping in Thiophanate Methyl kills the red rot fungus on the surface of the seed, preventing early field infection.", "Disease Management"),

    # Cultural Practices & Harvesting
    ("What is 'earthing up' (Mitti charhana) in sugarcane?", "Earthing up involves transferring soil from the ridges to the base of the cane. Done in May-June, it provides support to prevent lodging.", "Cultural Practices"),
    ("Why is propping/tying of sugarcane recommended?", "Sugarcane grows tall and becomes heavy. Tying canes from adjacent rows together prevents them from lodging (falling) during heavy winds and rains.", "Cultural Practices"),
    ("When should propping be done in Pakistan?", "Propping should be carried out in August or September when the crop has gained maximum height and before the strong monsoon winds.", "Cultural Practices"),
    ("How many ratoons (muddhi) can we keep for sugarcane?", "In Pakistan, it is economically viable to keep only one ratoon crop. Keeping multiple ratoons leads to poor yields and severe pest/disease buildup.", "Cultural Practices"),
    ("How to manage a ratoon crop effectively?", "After harvesting, do stubble shaving (cut close to the ground), fill the gaps with new setts, apply fertilizer early, and irrigate promptly.", "Cultural Practices"),
    ("Why should we remove late water shoots/suckers?", "Late water shoots (suckers) emerge near harvest time. They don't mature, consume nutrients, and significantly reduce the overall sugar recovery at the mill.", "Cultural Practices"),
    ("When is the right time to harvest autumn-planted sugarcane?", "Autumn-planted sugarcane takes about 14-15 months and is fully mature and ready for harvest from November to December.", "Cultural Practices"),
    ("When is the right time to harvest spring-planted sugarcane?", "Spring-planted sugarcane matures in 10-12 months and is usually harvested from December to February.", "Cultural Practices"),
    ("How to know if sugarcane is mature for harvesting?", "Check with a hand refractometer; a Brix reading above 18-20% indicates maturity. Also, a mature cane produces a metallic sound when tapped.", "Cultural Practices"),
    ("How soon should harvested cane reach the mill?", "Harvested cane must reach the sugar mill and be crushed within 24 to 48 hours to prevent drying and major loss of sucrose content.", "Cultural Practices"),
    
    # Value Addition, Varieties & Miscellaneous
    ("What are the recommended early maturing sugarcane varieties for Punjab?", "In Punjab, early maturing varieties like CPF-243, HSF-240, and CP-77-400 are recommended. They yield well if planted timely.", "Varieties Selection"),
    ("Which sugarcane varieties are suitable for the Sindh province?", "For Sindh, varieties like Thatta-10, Thatta-300, and CPF-234 are well-suited due to their tolerance to the hotter climate.", "Varieties Selection"),
    ("How to extract high-quality jaggery (Gur) from sugarcane?", "Boil the juice and use natural clarificants like wild okra (bhindi) root mucilage or a pinch of sodium bicarbonate to remove impurities.", "Miscellaneous"),
    ("How does frost affect sugarcane in Punjab?", "Severe frost kills the growing tip and ruptures the cells, causing sugar inversion and souring. Frost-affected fields should be harvested immediately.", "Miscellaneous"),
    ("What is the role of Plant Growth Regulators (PGRs) in sugarcane?", "Spraying Gibberellic Acid (GA3) can enhance internode elongation, increasing the overall cane height and yield.", "Miscellaneous"),
    ("Is sugarcane crop insurance available in Pakistan?", "Yes, some banks and agricultural departments offer insurance under the National Crop Insurance Scheme to protect against natural calamities.", "Miscellaneous"),
    ("How to increase the sugar recovery rate at the farm level?", "Stop irrigation 30 days before harvest, avoid lodging by propping, do not apply late nitrogen, and supply fresh canes to the mill immediately.", "Miscellaneous"),
    ("What is the ideal pH of soil for sugarcane cultivation?", "Sugarcane thrives best in slightly acidic to neutral soils with a pH ranging from 6.5 to 7.5, though it tolerates mild alkalinity in Pakistan.", "Sowing & Field Preparation"),
    ("How much water does a sugarcane crop consume?", "Sugarcane is a high water-demanding crop, consuming around 1500 mm to 2000 mm of water throughout its 10-12 month growing season.", "Irrigation Management"),
    ("Can we use sugarcane leaves as cattle fodder?", "Yes, the green tops of sugarcane are an excellent, highly nutritious fodder for livestock during the winter months in Pakistan.", "Miscellaneous"),
    # --- Advanced Sugarcane Agronomy & Pathology ---
    ("What is the Chip Bud (STP) method in sugarcane?", "Sustainable Sugarcane Initiative (SSI) or STP involves planting single bud chips raised in nursery trays instead of large cane setts, saving 80% of seed material and ensuring uniform plant establishment.", "Advanced Agronomy"),
    ("Why is Hot Water Treatment (HWT) mandatory for sugarcane seed?", "HWT (soaking setts at 50°C for 2 hours) is the only effective way to kill seed-borne diseases like Ratoon Stunting Disease (RSD) and Grassy Shoot Disease that are carried internally in the cane.", "Disease Management"),
    ("What is Pokkah Boeng disease?", "It is a fungal disease causing distorted, wrinkled, and twisted young leaves at the top of the cane, often followed by top rot during hot, humid monsoon periods.", "Disease Management"),
    ("How does Trash Mulching benefit the sugarcane ratoon crop?", "Instead of burning the dry leaves (trash) after harvest, spreading it between rows conserves massive amounts of soil moisture, suppresses weeds, and eventually adds organic matter to the soil.", "Advanced Agronomy"),
    ("Why are growth regulators like Ethephon used in sugarcane?", "Ethephon is sprayed to accelerate uniform ripening and increase the sugar accumulation (sucrose content) just before harvest, particularly in late-maturing varieties.", "Advanced Agronomy"),
    ("What is 'Lodging' and how does it ruin sugarcane?", "Lodging is when the tall canes fall over due to high winds and heavy irrigation. It drastically reduces sugar recovery, increases rat damage, and makes harvesting extremely difficult.", "Advanced Agronomy"),
    ("How is lodging prevented?", "By 'Earthing up' (mounding soil around the base) and 'Tying' (tying adjacent cane stools together with dry trash) in August-September.", "Advanced Agronomy"),
    ("What is the Ginning Out-Turn (GOT) equivalent in Sugarcane?", "It is the 'Sugar Recovery Rate' (usually 8-10% in Pakistan). It dictates how many kilograms of sugar are produced per 100 kg of crushed cane.", "Economics & Marketing"),
    ("How does intercropping with wheat work in autumn-planted sugarcane?", "Sugarcane is planted in wide rows (4 feet) in September. Wheat is then drilled in the empty spaces in November. The wheat is harvested in April, leaving the sugarcane to grow through the summer.", "Advanced Agronomy")
]

filename = 'Pakistan_Sugarcane_QA.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} queries successfully!")
