import csv

qa_data = [
    # --- General Field Preparation & Sowing ---
    ("What is the optimal sowing time for barley (Jau) in Pakistan?", "Barley is a Rabi crop. The optimal sowing time is from mid-October to mid-November across most plains.", "Field Preparation"),
    ("What type of soil is most suitable for barley cultivation?", "Barley is highly adaptable and can grow in sandy to medium loamy soils. It performs significantly better than wheat in poor, saline, and alkaline soils.", "Field Preparation"),
    ("Why is barley preferred over wheat in marginal lands?", "Barley has a shorter growing season, requires less water, and is highly tolerant to drought and soil salinity compared to wheat.", "Field Preparation"),
    ("How many ploughings are needed to prepare the field for barley?", "Being a hardy crop, 1 to 2 deep ploughings followed by a planking (Suhaga) are sufficient to prepare a standard seedbed.", "Field Preparation"),
    ("Can barley be grown under zero-tillage?", "Yes, in rice-wheat cropping zones, barley can be sown with a zero-tillage drill directly into rice stubble to save time and preserve soil moisture.", "Field Preparation"),
    ("What is the recommended row-to-row spacing for barley?", "When drill-sown, the row-to-row distance is typically kept at 9 inches (22.5 cm).", "Field Preparation"),
    ("Is broadcasting a recommended method for sowing barley?", "Drill sowing is always preferred for uniform germination, but broadcasting is commonly practiced in highly uneven rainfed (Barani) areas.", "Field Preparation"),
    ("What depth should barley seeds be planted?", "Seeds should be planted at a depth of 1.5 to 2.5 inches. Deeper sowing results in poor and delayed emergence.", "Field Preparation"),

    # --- Seed Selection & Treatment ---
    ("What is the recommended seed rate per acre for irrigated barley?", "For irrigated areas, a seed rate of 30 to 35 kg per acre is recommended.", "Seed Treatment"),
    ("What is the recommended seed rate per acre for rainfed (Barani) barley?", "In rainfed areas, the seed rate is increased to 40 to 45 kg per acre to compensate for lower germination due to moisture stress.", "Seed Treatment"),
    ("Why is seed treatment essential for barley?", "Seed treatment is critical to protect the crop against seed-borne fungal diseases like Covered Smut and Loose Smut.", "Seed Treatment"),
    ("Which fungicides are recommended for barley seed treatment?", "Systemic fungicides like Vitavax, Thiophanate-methyl, or Tebuconazole are used at the rate of 2 to 2.5 grams per kg of seed.", "Seed Treatment"),
    ("Can barley seeds from the previous year be reused?", "Yes, but they should be properly cleaned, graded to remove shriveled grains, and treated with fungicide before sowing.", "Seed Treatment"),
    ("What is the difference between hulled and hull-less barley?", "Hulled barley has a tough outer husk attached to the grain (mainly used for animal feed), whereas hull-less (naked) barley loses its husk easily and is preferred for human consumption.", "Seed Treatment"),

    # --- Varieties of Pakistan ---
    ("What are some prominent approved varieties of barley in Pakistan?", "Approved varieties include Jau-83, Jau-87, Haider-93, Soorab-96, Sanober-96, and Awaran-2002.", "Varieties"),
    ("Which barley varieties are well-suited for the Punjab province?", "Jau-83 and Jau-87 are well-adapted to the plains and rainfed areas of Punjab.", "Varieties"),
    ("Which varieties are specifically developed for highland and arid regions?", "Soorab-96 and Awaran-2002 were specifically developed for the arid and highland conditions of Balochistan.", "Varieties"),
    ("Are there dual-purpose barley varieties?", "Yes, many local landraces and varieties are used as dual-purpose: cut once for green fodder early in the season, and then left to produce grain.", "Varieties"),

    # --- Provincial: Punjab ---
    ("Where is barley primarily grown in Punjab?", "In Punjab, barley is primarily grown in the Barani (rainfed) tract, including districts like Chakwal, Attock, Rawalpindi, and Jhelum.", "Provincial: Punjab"),
    ("Why do farmers in central Punjab rarely grow barley?", "In irrigated central Punjab, wheat and maize are far more profitable cash crops. Barley is only grown on highly saline patches where wheat fails.", "Provincial: Punjab"),
    ("What is the main use of barley in Punjab?", "It is largely used as concentrated animal feed for livestock and poultry, and minimally for human consumption (like Sattu).", "Provincial: Punjab"),
    ("When is barley harvested in Punjab?", "Harvesting typically begins in early to mid-April, slightly earlier than wheat.", "Provincial: Punjab"),

    # --- Provincial: Sindh ---
    ("How is barley cultivated in Sindh?", "In Sindh, it is often grown on residual moisture (Dobari) immediately after the rice harvest in districts like Larkana and Shikarpur.", "Provincial: Sindh"),
    ("Why is barley important in the coastal and lower regions of Sindh?", "Lower Sindh suffers from high soil salinity and waterlogging. Barley is one of the few winter cereals that can survive and yield in these harsh conditions.", "Provincial: Sindh"),
    ("When is barley sown in Sindh?", "Due to the warmer climate, it is sown from late October to November.", "Provincial: Sindh"),
    ("When is barley harvested in Sindh?", "The harvest in Sindh is early, usually concluding by late March to early April.", "Provincial: Sindh"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) ---
    ("What role does barley play in KPK's agriculture?", "Barley is a vital crop in both the plains (D.I. Khan, Kohat) and the northern mountainous regions, serving as food and essential winter fodder.", "Provincial: KPK"),
    ("How does barley cultivation in hilly areas of KPK differ from the plains?", "In high-altitude areas that experience heavy snow, barley may be sown as a spring crop (March-April) instead of a winter crop.", "Provincial: KPK"),
    ("Why is barley preferred over wheat in the mountainous regions of KPK?", "Barley matures faster than wheat, allowing it to complete its life cycle before the onset of harsh conditions or within a short summer window.", "Provincial: KPK"),
    ("Is barley used for human consumption in KPK?", "Yes, barley flour is still mixed with wheat flour to make traditional breads in remote and mountainous communities.", "Provincial: KPK"),

    # --- Provincial: Balochistan ---
    ("How significant is barley in Balochistan?", "Barley is extremely significant. It is a staple grain and the primary winter fodder for the massive sheep and goat populations in the province.", "Provincial: Balochistan"),
    ("Where is barley grown in Balochistan?", "It is grown in the highland valleys (Quetta, Kalat, Ziarat) and the arid plains (Nasirabad, Sibi).", "Provincial: Balochistan"),
    ("How is 'dual-purpose' barley utilized by nomadic herders in Balochistan?", "Herders allow their livestock to graze the green barley shoots in early winter when fodder is scarce, then let the crop regenerate to harvest the grain in spring.", "Provincial: Balochistan"),
    ("What is the main challenge for barley farmers in Balochistan?", "Severe drought and lack of winter rainfall (Kushkaba farming) drastically limit yields.", "Provincial: Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("Does barley require heavy fertilization?", "No, barley is a low-input crop. It requires significantly less fertilizer than wheat to produce a decent yield.", "Fertilizer Management"),
    ("What is the general NPK recommendation for irrigated barley?", "A standard dose is 1 bag of DAP and 1 bag of Urea per acre.", "Fertilizer Management"),
    ("What is the fertilizer recommendation for rainfed (Barani) barley?", "In rainfed areas, half a bag of DAP and half a bag of Urea is applied at sowing, depending entirely on available soil moisture.", "Fertilizer Management"),
    ("What happens if excessive Nitrogen (Urea) is applied to barley?", "Excessive Nitrogen causes the plant to grow too tall, leading to severe lodging (falling over) and increased susceptibility to rust diseases.", "Fertilizer Management"),
    ("When should DAP be applied?", "Phosphorus (DAP) must be applied as a basal dose at the time of field preparation and sowing.", "Fertilizer Management"),
    ("When should Urea be applied in irrigated fields?", "Urea can be applied in two splits: half at sowing and half during the first irrigation (25-30 days later).", "Fertilizer Management"),

    # --- Irrigation & Weed Management ---
    ("How many irrigations does barley need?", "Barley is highly drought-tolerant. In irrigated plains, 1 to 2 irrigations are usually sufficient to achieve maximum yield.", "Irrigation & Weeds"),
    ("When is the most critical stage for irrigating barley?", "The tillering stage (30-35 days after sowing) and the booting/heading stage (70-80 days) are the most critical times for moisture.", "Irrigation & Weeds"),
    ("What happens if barley faces terminal drought (stress at grain filling)?", "The grains become shriveled and lightweight, significantly reducing both yield and market value.", "Irrigation & Weeds"),
    ("What are the major weeds in a barley field?", "Major weeds are similar to wheat, including broadleaf weeds like Bathu (Chenopodium) and grassy weeds like Wild Oats (Jangli Jai).", "Irrigation & Weeds"),
    ("How are weeds controlled in barley?", "In irrigated fields, post-emergence weedicides like Bromoxynil + MCPA (for broadleaf) or Clodinafop (for grasses) can be used 30-40 days after sowing.", "Irrigation & Weeds"),
    ("Why is manual weeding common in rainfed barley?", "In barani areas, chemical weedicides are ineffective due to dry soil, so manual uprooting or feeding weeds to livestock is preferred.", "Irrigation & Weeds"),

    # --- Pest Management ---
    ("What are the major insect pests of barley in Pakistan?", "The primary pests are Aphids, Armyworms, and occasionally Termites.", "Pest Management"),
    ("How do aphids damage the barley crop?", "Aphids cluster on the leaves and emerging ears, sucking sap. This weakens the plant and secretes honeydew, which attracts fungal molds.", "Pest Management"),
    ("When do aphids typically attack barley?", "The attack usually occurs in late February to March when temperatures begin to rise.", "Pest Management"),
    ("How to control an aphid attack on barley?", "If the population crosses the economic threshold (10-15 aphids per ear), spray systemic insecticides like Imidacloprid or Flonicamid.", "Pest Management"),
    ("What damage do armyworms cause to barley?", "Armyworms are caterpillars that rapidly eat the leaves and can strip a field of foliage. They feed primarily at night.", "Pest Management"),
    ("How to control armyworms?", "Spray Emamectin Benzoate or Lufenuron in the late afternoon or evening for effective control.", "Pest Management"),
    ("How to manage termites in a dry barley field?", "Termites attack roots in sandy, dry soils. Seed treatment with Imidacloprid is the best preventive measure.", "Pest Management"),
    ("Are birds a threat to the barley crop?", "Yes, sparrows and other birds can cause significant grain loss during the dough stage, requiring manual scaring techniques.", "Pest Management"),

    # --- Disease Management ---
    ("What is Covered Smut in barley?", "It is a seed-borne fungal disease where the grain kernels are replaced by masses of black fungal spores, which remain covered by a thin membrane until harvest.", "Disease Management"),
    ("How to control Covered Smut?", "Since it is seed-borne, the only effective control is treating the seed with fungicides like Vitavax or Thiophanate-methyl before planting.", "Disease Management"),
    ("What is Loose Smut of barley?", "Similar to covered smut, but the black spore masses are exposed and blow away in the wind, leaving only a bare stalk.", "Disease Management"),
    ("What is Stripe Rust (Yellow Rust) in barley?", "It appears as yellow, powdery stripes on the leaves. It thrives in cool, humid conditions and destroys the leaf's ability to photosynthesize.", "Disease Management"),
    ("How to manage barley rusts?", "Plant approved rust-resistant varieties. If the disease appears early, spray broad-spectrum fungicides like Propiconazole or Tebuconazole.", "Disease Management"),
    ("What causes Leaf Blotch in barley?", "Fungal pathogens (like Helminthosporium) cause brown, necrotic spots on leaves. It is managed by crop rotation and avoiding excessive seed rates.", "Disease Management"),
    ("Can infected barley straw be fed to livestock?", "Straw infected with rusts can be fed, but grains heavily infected with smut should be avoided as they lack nutritional value and may cause respiratory issues in animals.", "Disease Management"),

    # --- Harvesting & Storage ---
    ("How to tell when barley is ready for harvest?", "The crop is ready when the straw turns completely yellow/golden, the ears droop, and the grain is hard with moisture below 12-14%.", "Harvesting & Storage"),
    ("What happens if barley is harvested too late?", "Barley is highly prone to 'shattering' (grains falling out of the ear). A delayed harvest causes massive yield loss due to wind or birds.", "Harvesting & Storage"),
    ("Can combine harvesters be used for barley?", "Yes, combine harvesters used for wheat are easily adjusted and widely used to harvest barley in the plains.", "Harvesting & Storage"),
    ("What is the optimal grain moisture level for safe storage?", "Barley must be sun-dried to bring the moisture content down to 10-12% before storage to prevent mold and insect attacks.", "Harvesting & Storage"),
    ("How to protect stored barley from grain weevils and the Khapra beetle?", "Store in airtight bins and fumigate using Aluminum Phosphide (Phostoxin) tablets. Keep the bins sealed for at least 7-10 days.", "Harvesting & Storage"),
    ("Is it safe to use chemical fumigants on barley meant for animal feed?", "Yes, Phosphine gas (from Aluminum Phosphide) leaves no toxic residue once the grain is properly aerated before feeding or milling.", "Harvesting & Storage"),

    # --- FAQs: Market, Usage, & Economics ---
    ("What is the average yield of barley per acre in Pakistan?", "In rainfed areas, the yield is 10-15 maunds/acre. In irrigated areas, progressive farmers can achieve 25-35 maunds/acre.", "FAQs"),
    ("What is the primary commercial use of barley grain in Pakistan?", "The majority of barley grain is used in the formulation of commercial poultry feed and concentrated livestock rations.", "FAQs"),
    ("What is 'Sattu'?", "Sattu is a traditional, highly popular summer drink in Pakistan made from roasted and ground barley flour mixed with water and sugar/jaggery. It is known for its cooling properties.", "FAQs"),
    ("What is 'Talbina'?", "Talbina is a traditional porridge made from barley flour, milk, and honey, highly regarded in Islamic tradition for its nutritional and healing properties.", "FAQs"),
    ("Why is the market price of barley usually lower than wheat?", "Barley lacks gluten, making it unsuitable for making standard Roti (bread). Its demand is largely restricted to the animal feed sector.", "FAQs"),
    ("What is the malting industry's role in barley farming in Pakistan?", "Due to religious and legal prohibitions on alcohol, there is no brewing/malting industry for beer in Pakistan. However, a very small amount is malted for food extracts and non-alcoholic beverages.", "FAQs"),
    ("How does barley compare to wheat as a fodder crop?", "Barley produces highly nutritious green fodder much earlier in the winter than wheat, making it invaluable for livestock farmers facing winter feed shortages.", "FAQs"),
    ("Why do farmers mix barley and berseem (clover) seeds when sowing?", "Barley grows rapidly and provides the first cut of green fodder while the slower-growing berseem establishes itself. It also protects the berseem from severe frost.", "FAQs"),
    ("Can humans eat barley every day?", "Yes, barley is a highly nutritious whole grain, rich in dietary fiber (beta-glucan), which helps lower cholesterol and regulate blood sugar.", "FAQs"),
    # --- Advanced Barley Agronomy ---
    ("What is the difference between Malting Barley and Feed Barley?", "Malting barley (used for beverages/extracts) requires low grain protein (below 11.5%) for proper germination. Feed barley prioritizes high protein for livestock nutrition.", "Advanced Agronomy"),
    ("Why must Nitrogen fertilizer be restricted for Malting Barley?", "Applying too much Nitrogen late in the season increases the grain protein beyond acceptable limits, ruining its malting quality and causing rejection by buyers.", "Fertilizer Management"),
    ("What is the difference between covered and hull-less barley?", "Covered barley has a tough, inedible hull firmly attached to the grain. Hull-less (naked) barley sheds its hull during threshing, making it ideal for direct human consumption.", "Advanced Agronomy"),
    ("What makes Barley more salt-tolerant than Wheat?", "Barley can actively sequester toxic sodium ions into the cell vacuoles in older leaves, protecting the young, growing tissue from salt damage.", "Soil & Nutrition"),
    ("What is Net Blotch disease in Barley?", "Net Blotch (caused by Pyrenophora teres) appears as brown, net-like lesions on the leaves. It thrives in cool, humid conditions and requires fungicide intervention if severe.", "Disease Management"),
    ("Why is barley straw highly valued by dairy farmers?", "Barley straw is softer, more palatable, and slightly more digestible for cattle compared to the stiff, highly lignified wheat straw.", "Harvest & Post-Harvest")
]

filename = 'Pakistan_Barley_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality barley queries successfully!")
