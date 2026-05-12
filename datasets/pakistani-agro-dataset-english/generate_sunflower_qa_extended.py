import csv

qa_data = [
    # --- General Field Preparation & Sowing ---
    ("What type of soil is best for sunflower cultivation in Pakistan?", "Sunflowers grow best in deep, fertile, well-drained loamy soils. They can tolerate mild salinity better than many other cash crops but cannot withstand waterlogging.", "Field Preparation"),
    ("How should land be prepared for sowing sunflowers?", "Deep ploughing with a chisel plow is recommended to break any hardpan, followed by 2-3 cultivations and planking to create a fine, level seedbed.", "Field Preparation"),
    ("What is the optimal row-to-row spacing for sunflowers?", "The recommended row-to-row distance is 2.5 feet (75 cm) on ridges.", "Field Preparation"),
    ("What is the optimal plant-to-plant distance for sunflowers?", "A plant-to-plant distance of 9 to 12 inches is maintained to ensure an optimum plant population of around 22,000 to 24,000 plants per acre.", "Field Preparation"),
    ("What is the recommended seed rate for hybrid sunflower per acre?", "A seed rate of 2 to 2.5 kg per acre is recommended for hybrid varieties, depending on the seed size and germination percentage.", "Field Preparation"),
    ("Why is ridge sowing preferred over flat sowing for sunflowers?", "Ridge sowing saves irrigation water, protects the young seedlings from being submerged, and significantly reduces the incidence of collar rot and lodging.", "Field Preparation"),
    ("At what depth should sunflower seeds be planted?", "Seeds should be planted at a depth of 1.5 to 2 inches (4-5 cm). Sowing too deep delays emergence and reduces plant vigor.", "Field Preparation"),

    # --- Seasons & Varieties ---
    ("What are the two main seasons for growing sunflowers in Pakistan?", "Sunflowers are grown in two seasons: Spring (sown in Jan-Feb, harvested in May-June) and Autumn (sown in July-Aug, harvested in Oct-Nov).", "Seasons & Varieties"),
    ("Why is the Spring sunflower crop generally more successful than the Autumn crop?", "The Spring crop receives progressively warmer weather and longer days during its growth, leading to larger heads, higher yields, and better oil content compared to the Autumn crop.", "Seasons & Varieties"),
    ("What are some popular high-yielding sunflower hybrids in Pakistan?", "Popular imported and local hybrids include Hysun-33, NK-278, Parsun-3, Agora, and HO-1.", "Seasons & Varieties"),
    ("Can farmers save seeds from their hybrid sunflower crop for the next season?", "No. Saving seeds from a hybrid crop (F2 generation) results in massive genetic segregation, extremely poor yields, uneven maturity, and low oil content.", "Seasons & Varieties"),

    # --- Provincial Breakdown ---
    ("Which province is the leading producer of sunflowers in Pakistan?", "Sindh is historically a major producer, particularly in the lower districts, though Punjab also holds a significant share, especially in the southern belt.", "Provincial"),
    ("When is the Spring sunflower crop sown in Sindh?", "Due to the earlier onset of spring and warmer coastal climate, sowing in lower Sindh (Badin, Thatta) begins early in December and January.", "Provincial: Sindh"),
    ("When is the Spring sunflower crop sown in Punjab?", "In Punjab, sowing begins slightly later, typically from late January to mid-February, to avoid the severe winter frost.", "Provincial: Punjab"),
    ("Are sunflowers cultivated in Khyber Pakhtunkhwa (KPK)?", "Yes, they are cultivated in the plains (like D.I. Khan and Mardan) and valleys, usually sown in February-March for the spring crop.", "Provincial: KPK"),
    ("How does sunflower farming fit into Balochistan's agriculture?", "In Balochistan's canal-irrigated areas (Nasirabad division), sunflowers are grown successfully. Their relative drought tolerance makes them suitable for areas with marginal water availability compared to rice.", "Provincial: Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("What is the standard NPK fertilizer recommendation for sunflowers?", "A general recommendation is 1-1.5 bags of DAP, 2-3 bags of Urea, and 1 bag of SOP (Potash) per acre.", "Fertilizer Management"),
    ("When should Phosphorus (DAP) and Potash (SOP) be applied?", "The entire dose of DAP and SOP must be applied as a basal dose at the time of field preparation and sowing.", "Fertilizer Management"),
    ("How should Nitrogen (Urea) be split for sunflowers?", "Urea should be applied in 2 or 3 splits: at the first irrigation (20 days), at the star-bud stage (40 days), and just before flowering.", "Fertilizer Management"),
    ("Why is Boron crucial for sunflower cultivation?", "Sunflowers are highly sensitive to Boron deficiency. Boron is essential for pollen viability; its deficiency causes hollow/empty seeds in the center of the sunflower head.", "Fertilizer Management"),
    ("How and when should Boron be applied?", "Apply 1 kg of Borax (or equivalent) per acre to the soil at sowing, or spray a 0.2% Boric acid solution at the star-bud stage.", "Fertilizer Management"),
    ("What is the symptom of Nitrogen deficiency in sunflowers?", "Older leaves turn uniformly pale green and then yellow, leading to stunted growth and very small flower heads.", "Fertilizer Management"),

    # --- Irrigation & Weed Management ---
    ("How many irrigations are required for a sunflower crop?", "Typically, 4 to 6 irrigations are required depending on soil type and seasonal rainfall.", "Irrigation & Weeds"),
    ("What are the most critical stages for irrigation in sunflowers?", "The star-bud stage (button stage), full flowering (anthesis), and seed filling stages are extremely critical. Water stress here drastically cuts yield and oil content.", "Irrigation & Weeds"),
    ("Why should irrigation be managed carefully during high winds?", "Sunflowers have large, heavy heads. Irrigating during strong winds or storms causes severe 'lodging' (plants falling over), which destroys the crop.", "Irrigation & Weeds"),
    ("What are the common weeds in a sunflower field?", "Common weeds include Itsit, Deela (Nutsedge), and Bathu (in spring).", "Irrigation & Weeds"),
    ("How are weeds controlled chemically in sunflowers?", "Pre-emergence herbicides like Pendimethalin or S-Metolachlor should be sprayed on moist soil within 24 hours of sowing to prevent weed germination.", "Irrigation & Weeds"),

    # --- Pest Management ---
    ("What is the Sunflower Head Moth and how does it damage the crop?", "The caterpillar of the head moth feeds on the floral parts and developing seeds inside the sunflower head, creating webbing and exposing the head to fungal rot.", "Pest Management"),
    ("How to control the Sunflower Head Moth?", "Spray insecticides like Emamectin Benzoate or Lufenuron when the pest is first noticed, but avoid spraying during peak foraging hours of honeybees.", "Pest Management"),
    ("How do sucking pests like Whitefly and Jassid affect sunflowers?", "They suck sap from the leaves, causing them to turn yellow, cup, and dry up. A severe attack stunts the plant before the bud stage.", "Pest Management"),
    ("What is the control for sucking pests in sunflowers?", "Use systemic insecticides like Imidacloprid, Thiamethoxam, or Flonicamid if the population crosses the economic threshold.", "Pest Management"),
    ("What are Armyworms and how to manage them?", "Armyworms voraciously eat the foliage. They can be controlled by spraying Emamectin Benzoate or Match in the late afternoon.", "Pest Management"),
    ("Are birds a serious pest for sunflowers?", "Yes, parrots, crows, and sparrows cause massive damage by eating the maturing seeds directly from the heads. Bird scaring (using reflective ribbons or noise) is mandatory during the seed-filling stage.", "Pest Management"),

    # --- Disease Management ---
    ("What is Charcoal Rot in sunflowers?", "It is a soil-borne fungal disease that thrives in high soil temperatures and drought stress. The lower stem turns ashy grey/black, and the plant wilts and dies rapidly.", "Disease Management"),
    ("How to manage Charcoal Rot?", "Avoid moisture stress during flowering/grain filling, do not over-fertilize with Nitrogen, use Potash to strengthen the stem, and practice crop rotation.", "Disease Management"),
    ("What is Head Rot disease?", "Head rot (caused by Rhizopus or Sclerotinia) occurs when continuous rains or high humidity hit during the flowering/maturing stage. The back of the head becomes soft, brown, and rots.", "Disease Management"),
    ("How to prevent Head Rot?", "Control the head moth (whose damage opens wounds for the fungus), avoid over-irrigation during flowering, and use wider plant spacing to improve aeration.", "Disease Management"),
    ("What is Downy Mildew in sunflowers?", "A fungal disease causing stunted plants with thick, downward-curled leaves and a white cottony growth on the underside. Controlled by treating seeds with Metalaxyl.", "Disease Management"),

    # --- Pollination ---
    ("Why are honeybees incredibly important for sunflower farming?", "Sunflowers are highly cross-pollinated crops. Honeybees transferring pollen between flowers can increase seed yield by 25-30% and significantly improve oil content.", "Pollination"),
    ("How can farmers protect honeybees while managing pests?", "Never spray broad-spectrum insecticides during full bloom. If spraying is absolutely necessary, do it in the late evening when bees have returned to their hives.", "Pollination"),
    ("Should farmers rent beehives for their sunflower fields?", "Yes, placing 1 to 2 strong honeybee colonies per acre during the flowering period is highly recommended for optimal pollination.", "Pollination"),

    # --- Harvesting, Storage & FAQs ---
    ("When is a sunflower crop ready for harvest?", "The crop is ready when the back of the sunflower head turns yellow/brown, the bracts dry up, and the moisture content of the seed drops to about 15-20%.", "Harvest & Post-Harvest"),
    ("How are sunflowers harvested in Pakistan?", "They are mostly harvested manually by cutting the heads, drying them in the sun for a few days, and then using a mechanical thresher to separate the seeds.", "Harvest & Post-Harvest"),
    ("What is the optimal moisture level for storing sunflower seeds?", "Sunflower seeds must be thoroughly sun-dried to a moisture level of 8-10% before storage. High moisture causes the seeds to heat up, rot, and lose oil quality rapidly.", "Harvest & Post-Harvest"),
    ("What is the average yield of hybrid sunflowers per acre in Pakistan?", "A well-managed hybrid crop yields between 25 to 35 maunds (1,000 to 1,400 kg) per acre.", "FAQs"),
    ("What is the average oil content in hybrid sunflower seeds?", "Good quality hybrid seeds contain 40% to 45% premium edible oil.", "FAQs"),
    ("What is sunflower meal/cake?", "After the oil is extracted, the remaining solid residue is called sunflower meal. It is an excellent, protein-rich ingredient used in poultry and livestock feed.", "FAQs"),
    ("Why does the government encourage sunflower cultivation in Pakistan?", "Pakistan imports massive amounts of edible oil, spending billions of dollars annually. Growing sunflowers locally helps reduce this severe import bill and ensures food security.", "FAQs"),
    ("How do sunflower prices work in the local market?", "Prices are largely determined by the international edible oil market and local solvent extraction plants (oil mills). The government occasionally announces indicative prices to encourage farmers.", "FAQs")
]

filename = 'Pakistan_Sunflower_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality sunflower queries successfully!")
