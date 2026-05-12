import csv

qa_data = [
    # --- General Field Preparation & Sowing ---
    ("What type of soil is best for cultivating maize in Pakistan?", "Maize performs best in deep, fertile, well-drained loamy to silty loam soils with good organic matter. It cannot tolerate waterlogging or severe salinity.", "Field Preparation"),
    ("How should the field be prepared for sowing maize?", "Deep ploughing with a chisel plow is recommended, followed by 2-3 passes of a cultivator and planking to create a fine, weed-free seedbed.", "Field Preparation"),
    ("What is the recommended sowing method for maize?", "Ridge sowing (planting on raised beds) is highly recommended over flat sowing. It saves water, prevents seed rot, and protects the stem base from water.", "Field Preparation"),
    ("What is the optimal row-to-row spacing for hybrid maize?", "The recommended row-to-row distance is 2.5 feet (75 cm) on ridges.", "Field Preparation"),
    ("What is the optimal plant-to-plant distance for maize?", "A plant-to-plant distance of 7 to 9 inches is maintained to achieve the optimum plant population of 28,000 to 32,000 plants per acre.", "Field Preparation"),
    ("What causes poor germination in maize?", "Poor germination can result from planting seeds too deep, sowing in dry soil, using old/poor-quality seeds, or severe soil crusting after rain.", "Field Preparation"),
    ("At what depth should maize seeds be planted?", "Seeds should be planted at a depth of 1.5 to 2 inches in moist soil.", "Field Preparation"),
    ("Can maize be planted using the 'dry sowing' method?", "Yes, seeds can be dry-sown on ridges, followed immediately by irrigation. However, water must not submerge the seed to prevent rotting.", "Field Preparation"),

    # --- Seed Selection & Varieties ---
    ("What is the recommended seed rate per acre for hybrid maize?", "For grain purpose, the seed rate for hybrid maize is 8 to 10 kg per acre. For fodder/silage, a higher rate of 30-35 kg per acre is used.", "Seed & Varieties"),
    ("Why is hybrid maize highly preferred over synthetic/open-pollinated varieties in Pakistan?", "Hybrid maize yields 2 to 3 times more than traditional varieties, has high vigor, uniform maturity, and is highly responsive to fertilizers.", "Seed & Varieties"),
    ("What are some popular hybrid maize varieties available in Pakistan?", "Popular hybrids include Pioneer (e.g., 30Y87, 31P41), Dekalb/Monsanto (DK-6789), Syngenta (NK-8441), and local hybrids like YH-1898 and FH-1046.", "Seed & Varieties"),
    ("Can farmers save seed from their hybrid maize crop for the next year?", "No, seeds saved from a hybrid crop (F2 generation) will segregate, leading to uneven growth, poor ear formation, and a massive drop in yield.", "Seed & Varieties"),
    ("Why is seed treatment necessary for maize?", "Treating seeds with an insecticide (like Imidacloprid) and a fungicide protects young seedlings from early pests like shoot flies and soil-borne fungal rots.", "Seed & Varieties"),

    # --- Provincial: Punjab ---
    ("Which province is the leading producer of maize in Pakistan?", "Punjab is the largest producer, contributing over 80% of the country's total maize production.", "Provincial: Punjab"),
    ("What are the core maize-producing districts in Punjab?", "The core 'maize belt' comprises Sahiwal, Okara, Pakpattan, Kasur, Vehari, and Faisalabad.", "Provincial: Punjab"),
    ("How many maize crops are grown annually in Punjab?", "Two main crops are grown: Spring Maize (sown Feb-March, harvested June) and Autumn Maize (sown July-August, harvested Oct-Nov).", "Provincial: Punjab"),
    ("Why is Spring Maize highly profitable in Punjab?", "The longer growing period and high solar radiation during spring result in massive grain yields, often exceeding 100-120 maunds per acre.", "Provincial: Punjab"),
    ("What is the major challenge for the Autumn maize crop in Punjab?", "High temperatures during sowing, monsoon rains causing waterlogging, and extreme pest pressure (like Fall Armyworm) are major challenges.", "Provincial: Punjab"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) ---
    ("How significant is maize in KPK's agriculture?", "Maize is the second most important crop in KPK after wheat. It is a staple food in many rural and mountainous areas.", "Provincial: KPK"),
    ("Where is maize primarily grown in KPK?", "It is grown in the plains (Mardan, Swabi, Peshawar) and heavily in the mountainous regions (Swat, Dir, Hazara division).", "Provincial: KPK"),
    ("What is the sowing time for maize in the hilly areas of KPK?", "In high-altitude areas, maize is sown as a summer crop from April to May and harvested in September-October.", "Provincial: KPK"),
    ("Why do many farmers in KPK still use open-pollinated (synthetic) varieties?", "In remote hilly areas, farmers often lack access to expensive hybrid seeds and fertilizers, so they rely on local or synthetic varieties like 'Azam' and 'Babar'.", "Provincial: KPK"),

    # --- Provincial: Sindh ---
    ("Is maize a major crop in Sindh?", "Maize is cultivated on a much smaller scale in Sindh compared to Punjab and KPK, primarily due to extreme summer heat and water scarcity.", "Provincial: Sindh"),
    ("When is maize sown in Sindh?", "It is sown slightly earlier than Punjab, usually in late January to February for the spring crop, and July for the autumn crop.", "Provincial: Sindh"),
    ("What is the primary use of maize in Sindh?", "A significant portion of maize in Sindh is grown as green fodder for livestock rather than for commercial grain production.", "Provincial: Sindh"),
    
    # --- Provincial: Balochistan ---
    ("Where is maize cultivated in Balochistan?", "It is grown in limited quantities in the plain areas adjacent to Sindh and Punjab (like Nasirabad) and some highland valleys.", "Provincial: Balochistan"),
    ("What restricts extensive maize farming in Balochistan?", "Maize is a highly water-intensive crop, making it unsuitable for the severe drought conditions and water scarcity prevalent in most of Balochistan.", "Provincial: Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("What is the general fertilizer requirement for hybrid maize?", "Hybrid maize is a heavy feeder. A general dose per acre is 2 bags of DAP, 3 to 4 bags of Urea, and 1 to 2 bags of SOP/MOP.", "Fertilizer Management"),
    ("When should Phosphorus (DAP) be applied?", "The entire dose of DAP and Potash should be applied as a basal dose at the time of field preparation/sowing.", "Fertilizer Management"),
    ("How and when should Nitrogen (Urea) be top-dressed in maize?", "Urea should be split: applied at the 4-5 leaf stage, the knee-high stage (top dressing), and just before tasseling (flowering).", "Fertilizer Management"),
    ("Why is top dressing crucial in maize?", "Maize grows rapidly. Top dressing Urea at the knee-high and tasseling stages ensures the plant has enough nitrogen for stem elongation and large cob formation.", "Fertilizer Management"),
    ("What is the role of Zinc in maize cultivation?", "Maize is highly sensitive to Zinc deficiency. Applying 10 kg of 33% Zinc Sulphate per acre improves grain filling and prevents 'white bud' disease.", "Fertilizer Management"),
    ("What happens if Potash is not applied to maize?", "Lack of Potash leads to weak stalks (causing lodging/falling over), small cobs, shriveled grains at the tip of the cob, and high susceptibility to diseases.", "Fertilizer Management"),
    ("How does heat stress affect maize pollination?", "Temperatures above 38-40°C during tasseling can kill the pollen or dry out the silks, leading to barren cobs or poor seed setting.", "Fertilizer Management"),

    # --- Irrigation & Weed Management ---
    ("How many irrigations are required for the maize crop?", "Depending on the season and weather, maize requires 8 to 12 irrigations.", "Irrigation & Weeds"),
    ("What are the most critical stages for irrigation in maize?", "The flowering (tasseling/silking) and grain-filling stages are the most critical. Water stress during this period drastically reduces yield.", "Irrigation & Weeds"),
    ("How should maize be irrigated to prevent collar rot?", "Irrigate only within the furrows. Water should not cross the top of the ridges or touch the stem base, as it causes collar rot and stalk rot.", "Irrigation & Weeds"),
    ("What are the common weeds in a maize field?", "Common weeds include Deela (Nutsedge), Itsit (Trianthema), and Swanki grass.", "Irrigation & Weeds"),
    ("Which pre-emergence herbicides are recommended for maize?", "Atrazine + Metolachlor (e.g., Primextra Gold) should be sprayed on moist soil within 24 hours of sowing to prevent weed germination.", "Irrigation & Weeds"),
    ("Can post-emergence weedicides be used in standing maize?", "Yes, herbicides like Nicosulfuron or Mesotrione can be sprayed at the 3-4 leaf stage to control emerged weeds.", "Irrigation & Weeds"),

    # --- Pest Management ---
    ("What is the Fall Armyworm (FAW) and why is it so dangerous to maize?", "FAW is a highly destructive, invasive caterpillar that feeds deep inside the maize whorl, rapidly destroying the leaves and the growing point.", "Pest Management"),
    ("How can Fall Armyworm be controlled?", "Early detection is key. Spray targeted insecticides like Emamectin Benzoate, Spinetoram, or Chlorantraniliprole (Coragen) directing the nozzle into the whorl.", "Pest Management"),
    ("What is the Maize Stem Borer and how does it damage the plant?", "The stem borer larva enters the stem, feeding internally and creating 'dead hearts' (drying of the central shoot), which kills young plants.", "Pest Management"),
    ("What is the control measure for the Stem Borer in maize?", "Apply granular insecticides like Carbofuran (Furadan) or Fipronil into the plant whorls at the knee-high stage, or mix with irrigation.", "Pest Management"),
    ("How does the Shoot Fly damage maize seedlings?", "The shoot fly attacks young seedlings within the first two weeks of emergence, causing dead hearts. Seed treatment with Imidacloprid prevents this.", "Pest Management"),
    ("What damage do soil insects like cutworms and termites cause to maize?", "They cut young seedlings at the base or eat the roots. Treat the soil before sowing with Chlorpyrifos or flush it with early irrigation.", "Pest Management"),
    ("How to protect maize from bird attacks during cob maturation?", "Birds, particularly crows and parrots, damage the cobs. Use reflective ribbons, scarecrows, or manual drumming to deter them.", "Pest Management"),

    # --- Disease Management ---
    ("What causes Stalk Rot in maize?", "Stalk rot is caused by fungi or bacteria entering through roots or borer holes, often triggered by waterlogging and high nitrogen. The stalk becomes hollow and rots.", "Disease Management"),
    ("How to manage Collar Rot and Stalk Rot?", "Avoid over-irrigation, ensure balanced potash application, control stem borers, and treat seeds with fungicides before planting.", "Disease Management"),
    ("What is Leaf Blight (Fungal Spot) in maize?", "It appears as long, elliptical, grayish-brown necrotic spots on leaves. It thrives in high humidity and moderate temperatures.", "Disease Management"),
    ("How to control Fungal Spots/Leaf Blight in maize?", "Grow resistant hybrids and spray broad-spectrum fungicides like Mancozeb, Propiconazole, or Azoxystrobin as soon as spots appear.", "Disease Management"),
    ("What is Maize Smut?", "Smut is a fungal disease that causes massive, ugly, swollen galls (tumors) filled with black spores on the cobs, tassels, or stalks.", "Disease Management"),
    ("How to control Maize Smut?", "There is no chemical cure. Use resistant hybrids, practice crop rotation, and physically remove and burn the galls before they burst.", "Disease Management"),

    # --- Harvesting, Storage & Silage ---
    ("When is maize ready for grain harvest?", "The crop is ready when the cob husks dry up and turn brown, and a 'black layer' forms at the base of the kernel, indicating physiological maturity.", "Harvesting & Storage"),
    ("What is the ideal moisture content for harvesting and storing maize?", "Maize is harvested at 20-25% moisture but must be sun-dried or mechanically dried to 12-14% moisture before safe storage.", "Harvesting & Storage"),
    ("What pests attack maize during storage?", "The Grain Weevil (Suri) and Grain Moth are the primary storage pests, completely hollowing out the grains.", "Harvesting & Storage"),
    ("How to control pests in maize storage?", "Store dried grain in airtight bins or sealed bags and fumigate using Aluminum Phosphide (Phostoxin) tablets for 7-10 days.", "Harvesting & Storage"),
    ("What is Maize Silage?", "Silage is high-quality fermented fodder made by chopping the entire green maize plant (stalks, leaves, and milky cobs) and storing it in anaerobic (air-tight) conditions.", "Harvesting & Storage"),
    ("Why has maize silage become a booming industry in Pakistan?", "Silage provides highly nutritious, digestible, and year-round green fodder for dairy farms, significantly increasing milk production.", "Harvesting & Storage"),
    ("At what stage is maize harvested for making silage?", "It is harvested at the 'dough' or 'milky' stage, when the grain is soft but formed, and the plant moisture is around 65-70%.", "Harvesting & Storage"),

    # --- FAQs: Economics & Usage ---
    ("What is the average yield of hybrid maize per acre in Pakistan?", "Progressive farmers routinely achieve 100 to 120 maunds (4 to 4.8 tons) per acre, making it one of the highest-yielding cereal crops.", "FAQs"),
    ("What is the primary commercial use of maize grain in Pakistan?", "About 60-65% of the maize grain produced in Pakistan is consumed by the rapidly growing poultry feed industry.", "FAQs"),
    ("What is 'wet milling' of maize?", "Wet milling is an industrial process that separates maize into starch, corn oil, gluten (for animal feed), and sweeteners (like corn syrup).", "FAQs"),
    ("Why is maize considered a highly profitable cash crop?", "The short crop duration (100-120 days), massive yields from hybrid seeds, and guaranteed demand from the poultry sector ensure high returns.", "FAQs"),
    ("What is a 'bigha' in Pakistani land measurement?", "A bigha is a traditional unit of land measurement. In Punjab, it is generally considered as 4 kanals (half an acre), though exact sizes vary regionally.", "FAQs"),
    # --- Advanced Maize Agronomy & Silage ---
    ("Why is Fall Armyworm (FAW) so difficult to control?", "FAW caterpillars hide deep inside the maize whorl, protecting themselves from contact sprays. They also develop rapid resistance to chemicals if the same active ingredient is used repeatedly.", "Pest Management"),
    ("What are the best chemical rotations for Fall Armyworm?", "Farmers must rotate chemistries like Emamectin Benzoate, Spinetoram, Chlorantraniliprole, and Lufenuron, applying sprays specifically directed into the whorl.", "Pest Management"),
    ("What is the difference between grain maize and silage maize?", "Grain maize is harvested when fully dry and mature. Silage maize is harvested while still green (dough stage) and chopped entirely (stalk, leaves, and cob) for livestock feed.", "Advanced Agronomy"),
    ("What happens during the silage fermentation process?", "When chopped maize is packed tightly and sealed in a bunker, lactic acid bacteria anaerobically ferment the sugars, dropping the pH and preserving the feed for over a year.", "Advanced Agronomy"),
    ("Why do exporters strictly test maize for Aflatoxins?", "Aflatoxins are lethal toxins produced by Aspergillus fungi when maize is stored at high moisture in warm conditions. High Aflatoxin levels cause total rejection of export shipments.", "Export & Post-Harvest"),
    ("How does plant density affect maize cob size?", "Excessively high plant density creates competition for light and nutrients, resulting in barren plants (no cobs) or very small cobs. Precision spacing using pneumatic planters is vital.", "Advanced Agronomy"),
    ("What is 'Tasseling' and 'Silking' in maize?", "Tasseling is the emergence of the male flower at the top of the plant. Silking is the emergence of the female silks from the ear. Severe heat/drought during this synchronization period causes massive grain failure.", "Advanced Agronomy")
]

filename = 'Pakistan_Maize_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality maize queries successfully!")
