import csv

qa_data = [
    # --- Nursery Preparation & Sowing ---
    ("What is the most suitable soil for cultivating rice in Pakistan?", "Rice performs best in heavy clay or clay-loam soils that have high water retention capacity, which is essential for maintaining standing water.", "Nursery & Sowing"),
    ("What is the traditional method of establishing a rice crop?", "The traditional method involves raising seedlings in a nursery for 25-35 days and then manually transplanting them into a puddled (flooded and tilled) field.", "Nursery & Sowing"),
    ("What is the recommended seed rate for raising a rice nursery for one acre?", "For Basmati varieties, 5 to 6 kg of healthy seed is required. For coarse (IRRI) varieties, 8 to 10 kg of seed is needed per acre.", "Nursery & Sowing"),
    ("Why is seed treatment important before sowing rice in the nursery?", "Soaking seeds in a fungicide solution (like Thiophanate-methyl) for 24 hours prevents seed-borne diseases like Bakanae (foot rot) and Rice Blast.", "Nursery & Sowing"),
    ("What is the Rab (Dry Nursery) method?", "It is a dry bed nursery method used in areas with water scarcity, where seeds are sown in dry, well-pulverized soil and lightly irrigated.", "Nursery & Sowing"),
    ("What is the Kaddu (Wet Nursery) method?", "It is the most common method in Punjab where seeds are pre-sprouted in gunny bags and then broadcasted over a flooded, puddled nursery bed.", "Nursery & Sowing"),
    ("At what age should rice seedlings be transplanted?", "Seedlings should be transplanted when they are 25 to 35 days old. Older seedlings (40+ days) result in poor tillering and significantly lower yields.", "Nursery & Sowing"),
    ("What is Direct Seeding of Rice (DSR)?", "DSR involves sowing dry rice seeds directly into the field using a drill machine without raising a nursery or puddling the soil. It saves massive amounts of water and labor.", "Nursery & Sowing"),

    # --- Varieties of Pakistan ---
    ("What are the most famous Basmati rice varieties grown in Pakistan?", "Super Basmati, Basmati-515, PK-1121 (Kainat), Kissan Basmati, and Punjab Basmati are the most famous aromatic varieties.", "Varieties"),
    ("What is the specialty of 'PK-1121' (Kainat) Basmati?", "PK-1121 is highly prized for having the longest grain length (up to 8.5 mm before cooking) and excellent elongation after cooking.", "Varieties"),
    ("What are coarse or IRRI rice varieties?", "IRRI-6, IRRI-9, KS-282, and KSK-133 are non-aromatic, high-yielding coarse varieties grown mainly for domestic consumption and export to African markets.", "Varieties"),
    ("Are there any hybrid rice varieties in Pakistan?", "Yes, many Chinese hybrid rice varieties (e.g., Almas, Guard hybrids) are widely grown in Sindh and lower Punjab for massive yields, though they are non-basmati.", "Varieties"),

    # --- Provincial: Punjab ---
    ("What is the 'Kallar Tract' in Punjab?", "The Kallar Tract includes districts like Gujranwala, Hafizabad, Sheikhupura, Sialkot, and Narowal. Its unique soil and climate produce the world's finest aromatic Basmati rice.", "Provincial: Punjab"),
    ("When is Basmati rice nursery typically sown in Punjab?", "The nursery is usually sown from late May to mid-June.", "Provincial: Punjab"),
    ("When is transplanting of Basmati rice done in Punjab?", "Transplanting starts from late June and continues until the end of July, aligning with the monsoon rains.", "Provincial: Punjab"),
    ("Why is early transplanting of Basmati (before June 15) legally prohibited in Punjab?", "Early planting drastically increases the attack of stem borers and exposes the flowering stage to extreme summer heat, which destroys the grain quality and aroma.", "Provincial: Punjab"),

    # --- Provincial: Sindh ---
    ("What types of rice are primarily grown in Sindh?", "Sindh predominantly grows coarse rice varieties (IRRI-6, IRRI-9) and high-yielding Chinese hybrids. Basmati cultivation is negligible.", "Provincial: Sindh"),
    ("When is rice sown in Sindh?", "Due to the earlier onset of summer, rice nurseries in Sindh are sown in April-May, and transplanting occurs in May-June.", "Provincial: Sindh"),
    ("Which districts are the major rice producers in Sindh?", "Larkana, Shikarpur, Jacobabad, Badin, and Thatta are the major rice-producing districts.", "Provincial: Sindh"),
    ("Why is Basmati not successful in Sindh?", "Basmati requires a cooler climate during the grain-filling stage (October) to develop its signature aroma. Sindh's coastal and southern climate remains too warm.", "Provincial: Sindh"),

    # --- Provincial: Khyber Pakhtunkhwa (KPK) & Balochistan ---
    ("Where is rice grown in Khyber Pakhtunkhwa (KPK)?", "Rice is primarily grown in the cooler valleys of Swat, Dir, and Malakand, as well as in the plains of D.I. Khan.", "Provincial: KPK & Balochistan"),
    ("What is unique about Swat's rice?", "Swat grows cold-tolerant, short-duration coarse varieties (like JP-5). The crop is irrigated with cold mountain spring water.", "Provincial: KPK & Balochistan"),
    ("Is rice cultivated in Balochistan?", "Yes, rice is a major crop in the Nasirabad and Jaffarabad districts (the 'Green Belt' of Balochistan), which receive canal water from the Indus system.", "Provincial: KPK & Balochistan"),
    ("What varieties are grown in Balochistan?", "Balochistan primarily grows IRRI varieties and some local coarse types, heavily relying on canal irrigation.", "Provincial: KPK & Balochistan"),

    # --- Fertilizer & Nutrient Management ---
    ("What is the general NPK fertilizer dose for Basmati rice?", "A general dose per acre is 1 bag of DAP, 1.5 to 2 bags of Urea, and 1 bag of SOP (Potash).", "Fertilizer Management"),
    ("When should Urea be applied in a rice field?", "Urea should be applied in 2-3 splits: at the time of transplanting, at active tillering (25-30 days later), and at the panicle initiation stage.", "Fertilizer Management"),
    ("What is 'Khaira' disease in rice and what causes it?", "Khaira is not a pathogen but a physiological disorder caused by severe Zinc deficiency. Leaves develop dusty brown spots and plant growth is stunted.", "Fertilizer Management"),
    ("How to cure Zinc deficiency (Khaira) in rice?", "Apply 10 kg of 33% Zinc Sulphate per acre 10-15 days after transplanting. Never mix Zinc directly with DAP, as they react and become unavailable to the plant.", "Fertilizer Management"),
    ("Why is Potash (SOP) critical for rice?", "Potash thickens the plant stem (preventing lodging), increases resistance to diseases like BLB, and ensures fully filled, heavy grains.", "Fertilizer Management"),

    # --- Water & Weed Management ---
    ("How much standing water is required immediately after transplanting?", "Keep 1.5 to 2 inches of standing water for the first 15-20 days. This suppresses weed germination and helps seedlings establish.", "Water & Weeds"),
    ("What is Alternate Wetting and Drying (AWD) in rice farming?", "AWD is a water-saving technique where the field is allowed to dry out for a few days before re-flooding, reducing water usage by up to 30% without affecting yield.", "Water & Weeds"),
    ("What is 'Puddling'?", "Puddling is the intensive tilling of flooded soil to break soil clods, destroy weeds, and create a hardpan below the surface to stop water percolation.", "Water & Weeds"),
    ("What are the major weeds in Pakistani rice fields?", "Common weeds include Swanki grass (Echinochloa colona), Deela (Cyperus rotundus), and broadleaf weeds like Chhatri Wala Dhela.", "Water & Weeds"),
    ("How are weeds controlled chemically in flooded rice?", "Apply pre-emergence granular weedicides (like Butachlor or Pretilachlor) mixed with sand within 3 to 5 days of transplanting while water is standing in the field.", "Water & Weeds"),

    # --- Pest Management ---
    ("What is the Rice Stem Borer and how does it damage the crop?", "The stem borer larva enters the main stem, eating it from the inside. This causes 'Dead Hearts' in young plants and 'Whiteheads' (empty white panicles) in mature plants.", "Pest Management"),
    ("How to control the Stem Borer?", "Apply granular insecticides like Cartap Hydrochloride, Fipronil, or Carbofuran to the standing water 30-40 days after transplanting.", "Pest Management"),
    ("What is the Rice Leaf Folder?", "The leaf folder caterpillar folds the edges of the rice leaf together using silk threads and feeds on the green tissue inside, turning the field whitish.", "Pest Management"),
    ("What is the Brown Plant Hopper (BPH)?", "BPH is a severe sucking pest that feeds at the base of the plant. A heavy infestation causes the plants to completely dry out and die in circular patches, known as 'Hopper Burn'.", "Pest Management"),
    ("How to control BPH and Leaf Folders?", "Spray systemic insecticides like Nitenpyram or Pymetrozine targeting the base of the plant for BPH. Use Emamectin Benzoate for Leaf Folders.", "Pest Management"),
    ("Why is the destruction of rice stubble important after harvest?", "Destroying stubble with a rotavator kills the overwintering pupae of the stem borer, drastically reducing pest pressure for the next year's crop.", "Pest Management"),

    # --- Disease Management ---
    ("What is Bacterial Leaf Blight (BLB) in rice?", "BLB is a devastating bacterial disease where leaves turn yellow and then grayish-white from the tips downwards, drying up completely.", "Disease Management"),
    ("How to manage Bacterial Leaf Blight?", "There is no highly effective chemical cure. Avoid excessive Urea, ensure Potash application, use resistant varieties, and apply Copper-based fungicides to slow the spread.", "Disease Management"),
    ("What is Rice Blast disease?", "Rice Blast is a fungal disease that causes spindle-shaped spots with grey centers on the leaves. It can also attack the 'neck' of the panicle (Neck Blast), causing the whole ear to break off.", "Disease Management"),
    ("How to control Rice Blast?", "Treat seeds with fungicides before sowing. If symptoms appear on leaves, spray systemic fungicides like Tricyclazole, Azoxystrobin, or Difenoconazole.", "Disease Management"),
    ("What is Bakanae (Foot Rot) disease?", "Caused by a fungus, infected plants grow excessively tall, turn pale green, and produce empty grains or die before flowering. It is managed strictly through seed treatment.", "Disease Management"),
    ("What causes False Smut in rice?", "False Smut is a fungal infection that turns individual grains into large, velvety, yellowish-green to black spore balls. Prevent it by spraying Copper Oxychloride before panicle emergence.", "Disease Management"),

    # --- Harvesting, Storage & Export ---
    ("When is rice ready for harvesting?", "Rice is ready when 80-85% of the grains on the panicle turn golden yellow, and the moisture content drops to 20-22%.", "Harvesting & Storage"),
    ("What happens if rice is harvested too late?", "Delayed harvesting causes the grains to dry out too much, leading to massive 'grain shattering' in the field and high breakage during milling.", "Harvesting & Storage"),
    ("Can combine harvesters be used for rice?", "Yes, but specialized combine harvesters with tracks (instead of tires) are preferred to navigate the soft, wet mud of rice fields.", "Harvesting & Storage"),
    ("What is 'Sela' (Parboiled) rice?", "Parboiling involves partially boiling the rice in its husk before milling. It drives nutrients into the grain, makes it harder (reducing breakage during milling), and results in non-sticky cooked rice.", "Harvesting & Storage"),
    ("What is the optimal moisture level for storing milled rice?", "Milled rice should be dried to 12-14% moisture before long-term storage to prevent fungal molding and insect infestations.", "Harvesting & Storage"),
    ("Why is Pakistan's Basmati rice highly demanded globally?", "It is famous for its extra-long slender grains, unique aromatic flavor, fluffy texture after cooking, and significant elongation (grains double in length).", "Harvesting & Storage"),
    ("What is a major threat to Pakistan's rice exports?", "Aflatoxin contamination (due to high moisture storage) and pesticide residue limits (MRLs). Strict adherence to safe pesticide use and proper drying is required for EU and Middle Eastern markets.", "Harvesting & Storage"),

    # --- FAQs ---
    ("What is the average yield of Basmati rice per acre?", "The average yield is 40-50 maunds (1.6 to 2 tons) per acre, though progressive farmers achieve up to 60 maunds.", "FAQs"),
    ("What is the average yield of coarse/hybrid rice per acre?", "Coarse/hybrid varieties yield much higher, typically ranging from 80 to 120 maunds (3.2 to 4.8 tons) per acre.", "FAQs"),
    ("Why are rice crop residues (parali) often burned, and why is it dangerous?", "Farmers burn rice straw to quickly clear the field for wheat sowing. This practice is extremely dangerous as it causes severe winter 'Smog', triggering massive health and environmental crises.", "FAQs"),
    ("What are the alternatives to burning rice stubble?", "Using machines like the 'Happy Seeder' or 'Zero-Tillage Drill' allows farmers to sow wheat directly into the stubble without burning it.", "FAQs"),
    ("What is 'Brown Rice'?", "Brown rice is the whole grain rice with only the inedible outer hull removed. It retains the nutrient-rich bran layer, making it healthier than polished white rice.", "FAQs"),
    # --- Advanced Rice Agronomy & Milling ---
    ("What is Direct Seeded Rice (DSR) technology?", "DSR involves sowing rice seeds directly into the dry field using a drill, completely eliminating the need for nursery raising, puddling, and manual transplanting, saving massive amounts of labor and water.", "Advanced Agronomy"),
    ("What is the biggest challenge in Direct Seeded Rice (DSR)?", "Severe weed competition. Since the field is not flooded from day one, weeds emerge alongside the rice. Precise application of pre-emergence (Pendimethalin) and post-emergence (Bispyribac-sodium) herbicides is critical.", "Advanced Agronomy"),
    ("How does Alternate Wetting and Drying (AWD) save water?", "Instead of keeping the field continuously flooded, AWD involves installing a perforated PVC pipe in the soil. Farmers only irrigate when the water level inside the pipe drops to 15 cm below the soil surface, saving 30% water without yield penalty.", "Advanced Agronomy"),
    ("What is Bakanae (Foolish Seedling) disease?", "A seed-borne fungal disease (Gibberella fujikuroi) that causes infected seedlings to grow abnormally tall, thin, and pale, eventually dying before producing grain. It is controlled entirely by seed treatment.", "Disease Management"),
    ("What is 'Hopperburn' in rice?", "Hopperburn is the rapid yellowing, browning, and collapse of entire patches of the rice crop caused by massive infestations of the Brown Plant Hopper (BPH) sucking sap from the base of the stems.", "Pest Management"),
    ("How to control the Brown Plant Hopper (BPH)?", "Avoid excessive Urea (which attracts them), drain the field for a few days to disrupt their habitat, and spray Pymetrozine or Dinotefuran directed specifically at the base of the plants.", "Pest Management"),
    ("What causes 'Chalkiness' in rice grains?", "Chalkiness is an opaque, white spot in the grain that reduces its market value and causes it to break during milling. It is primarily caused by unusually high night temperatures during the grain-filling stage.", "Milling & Quality"),
    ("What is Head Rice Yield (HRY)?", "HRY is the percentage of intact, whole grains recovered after the milling process. Pakistani Basmati commands premium prices globally due to its high HRY and exceptional aroma.", "Milling & Quality"),
    ("Why is Zinc application absolutely essential for rice in Punjab?", "Rice grown in continuously flooded, alkaline soils frequently suffers from severe Zinc deficiency (Khaira disease), appearing as rusty brown spots on older leaves. Zinc Sulphate application is mandatory.", "Advanced Agronomy")
]

filename = 'Pakistan_Rice_QA_Extended.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Answer", "Category"])
    for row in qa_data:
        writer.writerow(row)

print(f"Generated {len(qa_data)} high-quality rice queries successfully!")
